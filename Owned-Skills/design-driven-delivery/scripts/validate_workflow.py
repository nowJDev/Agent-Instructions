# 설계 주도 작업 문서와 단계별 완료 증거의 누락을 검사한다.
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from workflow_paths import project_path, resolve_document_roots


PLACEHOLDER_PATTERN = re.compile(
    r"\[(?:REQUIRED(?:[^\]]*)?|PROJECT_REQUIRED)\]|\b(?:TODO|TBD)\b",
    re.IGNORECASE,
)
INCOMPLETE_CHECKBOX_PATTERN = re.compile(
    r"^\s*[-*+]\s+\[(?:\s|-|\?)\]",
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
    files = []
    try:
        paths = [project / relative for relative in selected] if selected else markdown_files(
            project_path(project, directory)
        )
        if not paths:
            errors.append(f"{label} 문서가 없습니다: {directory}")
        for path in paths:
            resolved = project_path(project, path)
            if resolved.suffix.lower() != ".md":
                errors.append(f"Markdown 문서가 아닙니다: {path}")
            else:
                add_required_file(errors, resolved)
                files.append(resolved)
    except (OSError, ValueError) as error:
        errors.append(str(error))
    return files


def prose_content(content: str) -> str:
    lines = []
    fence = None
    for line in content.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if fence is not None:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
        elif marker and (marker[1][0] != "`" or "`" not in marker[2]):
            fence = marker[1]
        else:
            lines.append(line)
    return re.sub(
        r"(?<!`)(`+)(?!`).*?(?<!`)\1(?!`)", "", "\n".join(lines),
        flags=re.DOTALL,
    )


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

    for path in (current_state, progress):
        try:
            project_path(project, path)
            add_required_file(errors, path)
        except (OSError, ValueError) as error:
            errors.append(str(error))

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
            try:
                resolved = project_path(project, path)
                if not resolved.is_file():
                    continue
                content = prose_content(resolved.read_text(encoding="utf-8"))
                if PLACEHOLDER_PATTERN.search(content):
                    errors.append(f"필수 자리표시자가 남아 있습니다: {path}")
                if INCOMPLETE_CHECKBOX_PATTERN.search(content):
                    errors.append(f"미완료 체크 항목이 남아 있습니다: {path}")
            except (OSError, ValueError) as error:
                errors.append(str(error))

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
