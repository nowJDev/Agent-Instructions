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
    r"^[ \t]*(?:(?:[-*+]|\d{1,9}[.)])[ \t]+|>[ \t]*)*"
    r"[-*+][ \t]+\[(?:[ \t]|-|\?)\]",
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
    blocks = []
    paragraph = []
    fence = None
    quote_depth = 0
    list_indents = []

    def flush() -> None:
        if paragraph:
            blocks.append(re.sub(
                r"(?<![\\`])((?:\\\\)*)(`+)(?!`).*?(?<!`)\2(?!`)",
                lambda match: match[1], "\n".join(paragraph),
                flags=re.DOTALL,
            ))
            paragraph.clear()

    # shortcut: 일반 문단·목록·인용의 경계만 추적하며 HTML 등 복합 Markdown은 수동 검증한다.
    for original in content.splitlines():
        quote_parts = [original.expandtabs(4)]
        while prefix := re.match(r"^ {0,3}> ?", quote_parts[-1]):
            quote_parts.append(quote_parts[-1][prefix.end():])
        depth = len(quote_parts) - 1

        if fence is not None:
            delimiter, fence_depth, fence_indent, inner_containers = fence
            body = quote_parts[fence_depth] if depth >= fence_depth else ""
            indentation = len(body) - len(body.lstrip(" "))
            outside = depth < fence_depth or (body.strip() and indentation < fence_indent)
            if not outside:
                body = body[fence_indent:]
                for kind, width in inner_containers:
                    if kind == "quote":
                        prefix = re.match(r"^ {0,3}> ?", body)
                        if prefix is None:
                            outside = True
                            break
                        body = body[prefix.end():]
                    else:
                        if body.strip() and len(body) - len(body.lstrip(" ")) < width:
                            outside = True
                            break
                        body = body[width:]
            if outside:
                fence = None
                flush()
            else:
                marker = re.match(r"^ {0,3}(`{3,}|~{3,})([ \t]*)$", body)
                if marker and marker[1][0] == delimiter[0] and len(marker[1]) >= len(delimiter):
                    fence = None
                continue

        line = quote_parts[-1]
        if depth != quote_depth:
            flush()
            list_indents.clear()
            quote_depth = depth
        if not line.strip():
            flush()
            continue

        indentation = len(line) - len(line.lstrip(" "))
        while list_indents and indentation < list_indents[-1]:
            list_indents.pop()
        container_indent = list_indents[-1] if list_indents else 0
        item = re.match(r"^( *)([-*+]|\d{1,9}[.)])( {1,4})(\S.*)$", line)
        if item and indentation <= container_indent + 3:
            flush()
            container_indent = item.start(4)
            list_indents.append(container_indent)
            body = item[4]
        else:
            body = line[container_indent:]

        inner_containers = []
        while True:
            prefix = re.match(r"^ {0,3}> ?", body)
            nested_item = re.match(r"^ {0,3}([-*+]|\d{1,9}[.)])( {1,4})(\S.*)$", body)
            if prefix:
                body = body[prefix.end():]
                inner_containers.append(("quote", 0))
            elif nested_item:
                body = nested_item[3]
                inner_containers.append(("list", nested_item.start(3)))
            else:
                break
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", body)
        if marker and (marker[1][0] != "`" or "`" not in marker[2]):
            flush()
            fence = (marker[1], depth, container_indent, inner_containers)
            continue

        heading = re.match(r"^ {0,3}(?:#{1,6}(?: |$)|(?:=+|-+|(?:\* *){3,}|(?:_ *){3,}) *$)", body)
        if heading:
            flush()
        paragraph.append(line)
        if heading:
            flush()
    flush()
    return "\n".join(blocks)


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
