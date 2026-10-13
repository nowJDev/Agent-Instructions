# 프로젝트에 설계 주도 작업 문서 구조를 안전하게 초기화한다.
from __future__ import annotations

import argparse
import os
import shutil
import sys
import tempfile
from pathlib import Path
from workflow_paths import project_path, resolve_document_roots


DIRECTORIES = (
    Path("docs/reviews"),
    Path("docs/handovers"),
)

FILES = {
    Path("docs/current-state.md"): "current-state-template.md",
    Path("docs/design-progress-checklist.md"): "progress-checklist-template.md",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="기존 파일을 덮어쓰지 않고 설계 주도 작업 문서 구조를 만든다."
    )
    parser.add_argument("--project", required=True, help="대상 프로젝트 루트 경로.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="생성할 항목만 출력하고 파일 시스템은 변경하지 않는다.",
    )
    return parser.parse_args()


def ensure_project(project: Path) -> None:
    if not project.exists():
        raise FileNotFoundError(f"프로젝트 경로가 없습니다: {project}")
    if not project.is_dir():
        raise NotADirectoryError(f"프로젝트 경로가 디렉터리가 아닙니다: {project}")


def main() -> int:
    args = parse_args()
    project = Path(args.project).expanduser().resolve()
    templates = Path(__file__).resolve().parent.parent / "assets" / "templates"

    try:
        ensure_project(project)
        for template_name in FILES.values():
            template = templates / template_name
            if not template.is_file():
                raise FileNotFoundError(f"템플릿 파일이 없습니다: {template}")

        specs_root, plans_root = resolve_document_roots(project)
        directories = (
            specs_root.relative_to(project), plans_root.relative_to(project), *DIRECTORIES,
        )
        for relative in (*directories, *FILES):
            project_path(project, project / relative)
        for relative_dir in directories:
            target_dir = project_path(project, project / relative_dir)
            if target_dir.exists():
                if not target_dir.is_dir():
                    raise NotADirectoryError(
                        f"문서 디렉터리 경로가 파일입니다: {target_dir}"
                    )
                print(f"KEPT   {relative_dir}")
            else:
                print(f"CREATE {relative_dir}")
                if not args.dry_run:
                    target_dir.mkdir(parents=True, exist_ok=True)

        for relative_file, template_name in FILES.items():
            target_file = project_path(project, project / relative_file)
            if target_file.exists():
                if not target_file.is_file():
                    raise IsADirectoryError(
                        f"문서 파일 경로가 디렉터리입니다: {target_file}"
                    )
                print(f"KEPT   {relative_file}")
                continue

            print(f"CREATE {relative_file}")
            if not args.dry_run:
                target_file.parent.mkdir(parents=True, exist_ok=True)
                temporary_path = None
                with (templates / template_name).open("rb") as source:
                    try:
                        with tempfile.NamedTemporaryFile(
                            dir=target_file.parent, prefix=".workflow-", delete=False
                        ) as destination:
                            temporary_path = Path(destination.name)
                            shutil.copyfileobj(source, destination)
                        os.link(temporary_path, target_file)
                    except FileExistsError:
                        if not target_file.is_file():
                            raise IsADirectoryError(
                                f"문서 파일 경로가 디렉터리입니다: {target_file}"
                            )
                        print(f"KEPT   {relative_file}")
                    finally:
                        if temporary_path is not None:
                            temporary_path.unlink(missing_ok=True)
    except (OSError, ValueError) as error:
        print(f"ERROR  {error}", file=sys.stderr)
        return 1

    mode = "DRY-RUN" if args.dry_run else "APPLIED"
    print(f"PASS   workflow bootstrap {mode}: {project}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
