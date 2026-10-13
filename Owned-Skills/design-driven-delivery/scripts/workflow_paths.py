# 초기화와 검증이 같은 기존 작업 문서 구조를 선택하도록 한다.
from __future__ import annotations

from pathlib import Path


def project_path(project: Path, path: Path) -> Path:
    resolved = path.resolve()
    if not resolved.is_relative_to(project):
        raise ValueError(f"프로젝트 밖 경로는 사용할 수 없습니다: {path}")
    return resolved


def resolve_document_roots(project: Path) -> tuple[Path, Path]:
    standard = project / 'docs/superpowers'
    existing = project / 'docs'
    if (standard / 'specs').exists() or (standard / 'plans').exists():
        return standard / 'specs', standard / 'plans'
    if (existing / 'specs').exists() or (existing / 'plans').exists():
        return existing / 'specs', existing / 'plans'
    return standard / 'specs', standard / 'plans'
