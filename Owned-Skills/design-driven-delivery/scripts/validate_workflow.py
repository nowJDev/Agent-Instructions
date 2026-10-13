# 설계 주도 작업 문서와 단계별 완료 증거의 누락을 검사한다.
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from workflow_paths import resolve_document_roots


PLACEHOLDER_PATTERN = re.compile(
    r"\[(?:REQUIRED(?:[^\]]*)?|PROJECT_REQUIRED)\]|\b(?:TODO|TBD)\b",
    re.IGNORECASE,
)
INCOMPLETE_CHECKBOX_PATTERN = re.compile(
    r"^\s*-\s+\[(?:\s|-|\?)\]",
    re.MULTILINE,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="설계 주도 작업의 필수 문서와 완료 증거를 검사한다."
    )
    parser.add_argument("--project", required=True, help="대상 프로젝트 루트 경로.")
    parser.add_argument(
        "--stage",
        choices=("bootstrap", "design", "plan", "completion"),
        default="completion",
        help="검사할 작업 단계.",
    )
    for kind in ("spec", "plan", "review"):
        parser.add_argument(
            f"--{kind}", action="append",
            help="현재 작업 문서의 프로젝트 상대경로. 여러 번 지정 가능.",
        )
    return parser.parse_args()


def markdown_files(directory: Path) -> list[Path]:
    if not directory.is_dir():
        return []
    return sorted(path for path in directory.rglob("*.md") if path.is_file())


def add_required_file(errors: list[str], path: Path) -> None:
    if not path.is_file():
        errors.append(f"필수 문서가 없습니다: {path}")


def add_required_collection(
    errors: list[str], label: str, directory: Path,
    selected: list[str] | None, project: Path,
) -> list[Path]:
    if selected:
        files = []
        for relative in selected:
            path = (project / relative).resolve()
            if not path.is_relative_to(project):
                errors.append(f"프로젝트 밖 문서는 검사할 수 없습니다: {path}")
            elif path.suffix.lower() != ".md":
                errors.append(f"Markdown 문서가 아닙니다: {path}")
            else:
                add_required_file(errors, path)
                files.append(path)
        return files
    files = markdown_files(directory)
    if not files:
        errors.append(f"{label} 문서가 없습니다: {directory}")
    return files


def main() -> int:
    args = parse_args()
    project = Path(args.project).expanduser().resolve()
    if not project.is_dir():
        print(f"ERROR  프로젝트 디렉터리가 없습니다: {project}", file=sys.stderr)
        return 1

    specs_root, plans_root = resolve_document_roots(project)
    current_state = project / "docs/current-state.md"
    progress = project / "docs/design-progress-checklist.md"
    review_root = project / "docs/reviews"
    errors: list[str] = []
    evidence_files: list[Path] = [current_state, progress]

    add_required_file(errors, current_state)
    add_required_file(errors, progress)

    if args.stage in {"design", "plan", "completion"}:
        evidence_files.extend(
            add_required_collection(errors, "설계 명세", specs_root, args.spec, project)
        )

    plan_files: list[Path] = []
    if args.stage in {"plan", "completion"}:
        plan_files = add_required_collection(errors, "구현 계획", plans_root, args.plan, project)
        evidence_files.extend(plan_files)

    if args.stage == "completion":
        evidence_files.extend(
            add_required_collection(errors, "코드 리뷰", review_root, args.review, project)
        )

        for path in evidence_files:
            if not path.is_file():
                continue
            content = path.read_text(encoding="utf-8")
            if PLACEHOLDER_PATTERN.search(content):
                errors.append(f"필수 자리표시자가 남아 있습니다: {path}")

        for path in evidence_files:
            if not path.is_file():
                continue
            content = path.read_text(encoding="utf-8")
            if INCOMPLETE_CHECKBOX_PATTERN.search(content):
                errors.append(f"미완료 체크 항목이 남아 있습니다: {path}")

    if errors:
        for error in errors:
            print(f"ERROR  {error}", file=sys.stderr)
        print(
            f"FAIL   workflow validation stage={args.stage}: {project}",
            file=sys.stderr,
        )
        return 1

    print(f"PASS   workflow validation stage={args.stage}: {project}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
