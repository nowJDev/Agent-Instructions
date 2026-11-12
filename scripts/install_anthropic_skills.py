# 고정 원본의 Anthropic 스킬을 검증하고 공급자 이름으로 전역 설치한다.
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import tempfile
from urllib.request import urlopen
import uuid
import zipfile


REPOSITORY = 'https://github.com/anthropics/skills'
DEFAULT_MANIFEST = Path(__file__).resolve().parents[1] / 'references/anthropic-skills.lock.json'
TEXT_SUFFIXES = {'.md', '.txt', '.py', '.js', '.ts', '.tsx', '.jsx', '.json', '.yaml', '.yml', '.sh', '.html', '.css'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def data_directory(home):
    if os.name == 'nt':
        base = Path(os.environ.get('LOCALAPPDATA', home / 'AppData/Local')) if home == Path.home() else home / 'AppData/Local'
    else:
        base = home / '.local/share'
    return base / 'AgentSkills'


def no_links(path):
    for item in (*reversed(path.parents), path):
        try:
            info = item.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & 0x400:
            raise ValueError('Refusing symlink or junction: ' + str(item))


def tree_hashes(directory):
    no_links(directory)
    if not directory.is_dir():
        raise ValueError('Expected package directory: ' + str(directory))
    result = {}
    for path in directory.rglob('*'):
        no_links(path)
        if path.is_file():
            result[path.relative_to(directory).as_posix()] = digest(path.read_bytes())
        elif not path.is_dir():
            raise ValueError('Unsupported file type: ' + str(path))
    return result


def inherit_permissions(path):
    # Windows 임시 폴더의 비공개 ACL을 실행 스킬에 남기지 않고 대상 부모의 규칙을 따른다.
    if os.name == 'nt':
        subprocess.run(['icacls', str(path), '/reset', '/T', '/Q'], check=True, capture_output=True)


def validate_manifest(manifest):
    if (manifest.get('schema_version') != 1 or manifest.get('repository') != REPOSITORY
            or not re.fullmatch('[a-f0-9]{40}', manifest.get('commit', ''))
            or not re.fullmatch('[a-f0-9]{64}', manifest.get('archive_sha256', ''))):
        raise ValueError('Invalid source manifest')
    sources, names = set(), set()
    for entry in manifest['skills']:
        source, name = entry['source'], entry['name']
        if (not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', source)
                or name != 'anthropic-' + source or source in sources or name in names
                or not isinstance(entry['implicit'], bool)
                or ('legacy_license_sha256' in entry and not re.fullmatch('[a-f0-9]{64}', entry['legacy_license_sha256']))
                or entry.get('migrate_from') not in (None, source)
                or (entry.get('migrate_from') and source not in {'frontend-design', 'skill-creator'})):
            raise ValueError('Invalid or duplicate skill name')
        sources.add(source)
        names.add(name)
    if not sources:
        raise ValueError('Empty skill manifest')


def source_packages(manifest, archive):
    validate_manifest(manifest)
    if digest(archive.read_bytes()) != manifest['archive_sha256']:
        raise ValueError('Archive SHA256 mismatch')
    prefix = 'skills-' + manifest['commit']
    packages = {entry['source']: {} for entry in manifest['skills']}
    notices = None
    with zipfile.ZipFile(archive) as bundle:
        seen = set()
        if sum(item.file_size for item in bundle.infolist()) > 512 * 1024 * 1024:
            raise ValueError('Archive is too large')
        for item in bundle.infolist():
            name = item.filename.rstrip('/')
            path = PurePosixPath(name)
            mode = item.external_attr >> 16
            if (not name or '\\' in name or ':' in name or path.is_absolute()
                    or any(part in {'', '.', '..'} or part.endswith((' ', '.')) for part in name.split('/'))
                    or path.parts[0] != prefix or name.casefold() in seen
                    or stat.S_IFMT(mode) not in {0, stat.S_IFREG, stat.S_IFDIR}):
                raise ValueError('Unsafe archive path, duplicate or link type: ' + name)
            seen.add(name.casefold())
            if item.is_dir():
                continue
            relative = path.parts[1:]
            if relative == ('THIRD_PARTY_NOTICES.md',):
                notices = bundle.read(item)
            if len(relative) >= 3 and relative[0] == 'skills' and relative[1] in packages:
                key = '/'.join(relative[2:])
                if key.endswith('/SKILL.md'):
                    raise ValueError('Nested SKILL.md would register an extra skill: ' + key)
                packages[relative[1]][key] = bundle.read(item)
    for source, files in packages.items():
        text = files.get('SKILL.md', b'').decode('utf-8')
        header = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
        if not header or re.findall(r'(?m)^name:\s*([^\r\n]+)', header[1]) != [source]:
            raise ValueError('Missing or invalid root skill name: ' + source)
    return packages, notices


def transform_text(text, entries):
    # 공개 원본 URL은 출처이므로 설치 경로 변환에서 제외한다.
    urls = []

    def protect(match):
        urls.append(match[0])
        return '\x00URL' + str(len(urls) - 1) + '\x00'

    text = re.sub(r'https?://[^\s<>"\x27)]+', protect, text)
    for entry in sorted(entries, key=lambda value: -len(value['source'])):
        source, name = entry['source'], entry['name']
        text = re.sub(r'\$' + re.escape(source) + r'(?![\w-])', '$' + name, text)
        resource = r'(?=[/\\](?:SKILL\.md\b|(?:scripts|references|assets|agents|evals|shared)[/\\]))'
        text = re.sub(r'(?<![\w/\\.-])' + re.escape(source) + resource, name, text)
        for prefix in ('../', 'skills/', 'skills/public/', 'skills/examples/'):
            text = re.sub(re.escape(prefix + source) + resource, prefix + name, text)
    for index, url in enumerate(urls):
        text = text.replace('\x00URL' + str(index) + '\x00', url)
    return text


def prepared_packages(manifest, packages, notices):
    prepared = {}
    for entry in manifest['skills']:
        files = dict(packages[entry['source']])
        for relative, content in files.items():
            if Path(relative).suffix.lower() in TEXT_SUFFIXES and not Path(relative).name.startswith(('LICENSE', 'NOTICE')):
                try:
                    text = content.decode('utf-8')
                except UnicodeDecodeError:
                    continue
                text = transform_text(text, manifest['skills'])
                if relative == 'SKILL.md':
                    text = re.sub(r'(?m)^name: ' + re.escape(entry['source']) + r'\r?$',
                                  'name: ' + entry['name'], text, count=1)
                files[relative] = text.encode('utf-8')
        if notices is not None:
            files['UPSTREAM_THIRD_PARTY_NOTICES.md'] = notices
        if not entry['implicit']:
            key = 'agents/openai.yaml'
            if key in files:
                raise ValueError('Review upstream invocation policy before overriding: ' + entry['source'])
            files[key] = b'policy:\n  allow_implicit_invocation: false\n'
        prepared[entry['name']] = files
    return prepared


def install(manifest, archive, home, apply=False):
    home = Path(home).absolute()
    target = home / '.agents/skills'
    data = data_directory(home)
    state_path = data / 'anthropic-skills-state.json'
    no_links(target)
    no_links(data)
    no_links(state_path)
    source, notices = source_packages(manifest, Path(archive))
    prepared = prepared_packages(manifest, source, notices)
    state_before = state_path.read_bytes() if state_path.exists() else None
    state = json.loads(state_before) if state_before is not None else {}
    if state and (state.get('repository') != REPOSITORY or state.get('schema_version') != 1):
        raise ValueError('Unrecognized installation state')
    pending, legacy, observed = [], [], {}
    hashes = {name: {key: digest(value) for key, value in files.items()} for name, files in prepared.items()}
    for entry in manifest['skills']:
        name = entry['name']
        destination = target / name
        no_links(destination)
        observed[name] = tree_hashes(destination) if destination.exists() else None
        if destination.exists():
            managed = state.get('packages', {}).get(name)
            if not managed:
                raise ValueError('Unmanaged existing target: ' + name)
            actual = observed[name]
            if actual != managed['files']:
                raise ValueError('Locally modified managed package: ' + name)
            if actual != hashes[name]:
                pending.append(name)
        else:
            pending.append(name)
        old_name = entry.get('migrate_from')
        if old_name:
            old_path = target / old_name
            no_links(old_path)
            observed[old_name] = tree_hashes(old_path) if old_path.exists() else None
            if old_path.exists():
                original = {key: digest(value) for key, value in source[entry['source']].items()}
                actual = observed[old_name]
                if actual != original and entry.get('legacy_license_sha256'):
                    original['LICENSE.txt'] = entry['legacy_license_sha256']
                if actual != original:
                    raise ValueError('Modified legacy package requires manual comparison: ' + old_name)
                legacy.append(old_name)
    result = {'installed': [], 'pending': pending, 'migrate': legacy, 'backup': None}
    if not apply or not (pending or legacy):
        return result
    no_links(data / 'backups')
    data.mkdir(parents=True, exist_ok=True)
    lock = data / 'anthropic-skills.lock'
    with lock.open('x', encoding='utf-8') as lock_file:
        try:
            target.mkdir(parents=True, exist_ok=True)
            with tempfile.TemporaryDirectory(prefix='stage-', dir=data) as temporary:
                stage = Path(temporary)
                for name in pending:
                    for relative, content in prepared[name].items():
                        path = stage / name / relative
                        path.parent.mkdir(parents=True, exist_ok=True)
                        path.write_bytes(content)
                for name, before in observed.items():
                    current = target / name
                    no_links(current)
                    now = tree_hashes(current) if current.exists() else None
                    if now != before:
                        raise ValueError('Destination changed after preflight: ' + name)
                no_links(state_path)
                if (state_path.read_bytes() if state_path.exists() else None) != state_before:
                    raise ValueError('Installation state changed after preflight')
                backup = data / 'backups' / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8])
                backup.mkdir(parents=True)
                moved, published = [], []
                state_temp = data / ('.state-' + uuid.uuid4().hex + '.json')
                try:
                    for kind, names in [('installed', pending), ('legacy', legacy)]:
                        for name in names:
                            current = target / name
                            if current.exists():
                                saved = backup / kind / name
                                saved.parent.mkdir(parents=True, exist_ok=True)
                                os.replace(current, saved)
                                moved.append((current, saved))
                    for name in pending:
                        destination = target / name
                        if destination.exists():
                            raise ValueError('Destination appeared during install: ' + name)
                        os.replace(stage / name, destination)
                        published.append(destination)
                        inherit_permissions(destination)
                    new_state = {'schema_version': 1, 'repository': REPOSITORY, 'commit': manifest['commit'],
                                 'packages': {**state.get('packages', {}), **{
                                     entry['name']: {'source': entry['source'], 'files': hashes[entry['name']]}
                                     for entry in manifest['skills']}}}
                    with state_temp.open('x', encoding='utf-8') as output:
                        output.write(json.dumps(new_state, ensure_ascii=False, indent=2) + '\n')
                    inherit_permissions(state_temp)
                    if state_path.exists():
                        (backup / 'previous-state.json').write_bytes(state_path.read_bytes())
                    os.replace(state_temp, state_path)
                except BaseException:
                    for path in reversed(published):
                        failed = backup / 'failed-new' / path.name
                        failed.parent.mkdir(parents=True, exist_ok=True)
                        os.replace(path, failed)
                    for current, saved in reversed(moved):
                        os.replace(saved, current)
                    raise
                finally:
                    state_temp.unlink(missing_ok=True)
                result.update(installed=pending, pending=[], migrate=[], migrated=legacy, backup=str(backup))
        finally:
            lock_file.close()
            lock.unlink()
    return result


def main():
    parser = argparse.ArgumentParser(description='Check or install pinned Anthropic skills; existing personal changes are preserved.')
    parser.add_argument('--apply', action='store_true', help='Install after all preflight checks pass; default only checks.')
    parser.add_argument('--archive', type=Path, help='Use an existing ZIP with the pinned SHA256.')
    parser.add_argument('--home', type=Path, default=Path.home(), help='Target user home; defaults to the current user.')
    arguments = parser.parse_args()
    manifest = json.loads(DEFAULT_MANIFEST.read_text(encoding='utf-8'))
    validate_manifest(manifest)
    archive = arguments.archive or data_directory(arguments.home) / 'anthropic-skills' / (manifest['commit'] + '.zip')
    if not archive.exists():
        if not arguments.apply:
            parser.exit(1, 'Pinned source ZIP is not cached. Run --apply to download and install, or supply --archive.\n')
        no_links(archive)
        archive.parent.mkdir(parents=True, exist_ok=True)
        with urlopen('https://codeload.github.com/anthropics/skills/zip/' + manifest['commit'], timeout=60) as response:
            with tempfile.NamedTemporaryFile(dir=archive.parent, delete=False) as download:
                download_path = Path(download.name)
                try:
                    data = response.read(64 * 1024 * 1024 + 1)
                    if len(data) > 64 * 1024 * 1024 or digest(data) != manifest['archive_sha256']:
                        raise ValueError('Downloaded archive SHA256 or size mismatch')
                    download.write(data)
                except BaseException:
                    download.close()
                    download_path.unlink()
                    raise
        os.replace(download_path, archive)
    result = install(manifest, archive, arguments.home, apply=arguments.apply)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result['pending'] or result['migrate'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
