# 프로젝트에 설계 주도 작업 문서 구조를 안전하게 초기화한다.
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


DIRECTORIES = (
    Path("docs/superpowers/specs"),
    Path("docs/superpowers/plans"),
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

        for relative_dir in DIRECTORIES:
            target_dir = project / relative_dir
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
            target_file = project / relative_file
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
                shutil.copyfile(templates / template_name, target_file)
    except (FileNotFoundError, NotADirectoryError, OSError) as error:
        print(f"ERROR  {error}", file=sys.stderr)
        return 1

    mode = "DRY-RUN" if args.dry_run else "APPLIED"
    print(f"PASS   workflow bootstrap {mode}: {project}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
