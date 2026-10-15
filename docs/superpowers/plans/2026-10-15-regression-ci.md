<!-- 자동 회귀 테스트 CI의 구현 순서와 검증 증거를 기록한다. -->
# 자동 회귀 테스트 CI 실행 계획.

For agentic workers: REQUIRED SUB-SKILL: executing-plans. 사용자의 설계안 실행 승인에 따라 진행한다.

Goal: 기존 회귀 테스트를 Ubuntu·Windows의 PR·main push·수동 CI로 실행한다.
Architecture: 표준 unittest와 GitHub 호스트 runner를 사용하며 제품 스크립트와 테스트 계약을 보존한다.
Tech Stack: Python 3.12, GitHub Actions YAML, Bash, PowerShell, Markdown.

## Task 1. 기준선과 최소 호환 수정.

Files: `tests/test_review_regressions.py`.

- [x] 전체 64개를 실행하여 POSIX link 정리 오류 2개와 Windows 전용 skip 4개를 확인했다.
- [x] link_directory의 정리를 플랫폼별로 분리하고 기존 경계 테스트 2개로 GREEN을 확인한다.

```python
self.addCleanup(os.rmdir, link) if os.name == 'nt' else self.addCleanup(link.unlink)
```

실제 구현은 각 OS 분기 안에 정리 등록을 배치한다. 실패 테스트를 제거하거나 skip하지 않는다.

## Task 2. CI와 운영 안내.

Files: `.github/workflows/ci.yml`, `docs/ci.md`, `README.md`, `CHANGELOG.md`.

- [x] PR·main push·수동 트리거, Python 3.12, Ubuntu·Windows, 읽기 권한, SHA 고정, 중복 취소와 timeout을 구현한다.
- [x] Git Bash와 Windows 도구·COM 사전 검사를 추가하고 원래 테스트 종료 코드를 보존한다.
- [x] 운영 안내와 README 상태 배지·링크, 변경 이력을 작성한다.

```bash
python -X utf8 -B -m unittest discover -s tests -v
```

기대 GREEN은 Ubuntu 60개 통과·4개 의도적 skip, Windows 64개 통과·skip 0개다. 테스트 목록 변경 시 실제 수를 기준으로 보고한다.

## Task 3. 검증·리뷰·전달.

Files: 이 계획, `docs/reviews/2026-10-15-regression-ci.md`, `docs/current-state.md`, `docs/design-progress-checklist.md`.

- [x] 전체 회귀와 임시 실패 테스트를 통한 exit 1 검출을 확인한다.
- [x] actionlint·인코딩·문서 링크·git diff --check와 독립 리뷰를 확인한다.
- [ ] 한글 커밋으로 저장하고 작업 브랜치를 PR로 전달하여 GitHub의 OS별 결과를 확인한다. 실제 실행 전에는 원격 검증을 완료로 기록하지 않는다.

```bash
git diff --check
git add .github/workflows/ci.yml README.md CHANGELOG.md tests/test_review_regressions.py docs
git commit -m "Windows와 Linux 자동 회귀 테스트 CI 추가"
```
