# 프로젝트별 검증 Adapter.

## 선택 원칙.

프로젝트 파일, 지침과 기존 명령을 조사한 뒤 해당 Adapter를 선택한다. 여러 유형이 섞인 저장소는 변경 범위별 Adapter를 조합한다. 이 문서의 예시보다 프로젝트의 승인 명령을 우선한다.

## Unity.

- 순수 C# 계약은 EditMode로 검증한다.
- `MonoBehaviour`, Scene, Prefab, UI와 XR은 PlayMode로 검증한다.
- Editor Builder는 반복 실행의 GUID·계층·참조 멱등성을 확인한다.
- 실제 HMD·Controller·성능·가독성은 타깃 기기에서 확인한다.
- Unity가 재직렬화한 테스트 산출물만 정확히 식별해 복원한다.

## Web Frontend.

- unit, component와 E2E 테스트를 구분한다.
- 실제 브라우저에서 레이아웃, 상호작용, 콘솔과 네트워크를 확인한다.
- 키보드, 스크린리더, contrast와 responsive 동작을 확인한다.
- production build와 주요 번들 경고를 확인한다.

## Backend와 API.

- unit, integration, contract와 migration 테스트를 구분한다.
- 인증·인가, idempotency, transaction과 retry 경계를 확인한다.
- Schema와 API 하위 호환성을 확인한다.
- 실제 서비스 변경은 사용자 승인과 rollout·rollback 계획을 요구한다.

## Python과 CLI.

- unit test, type check, lint와 package build를 실행한다.
- 지원 Python 버전과 깨끗한 환경 설치를 확인한다.
- CLI exit code, stdout·stderr와 파일 시스템 부작용을 확인한다.
- 플랫폼별 경로와 인코딩을 확인한다.

## Data와 Analytics.

- Schema, null, 중복, 범위와 참조 무결성을 확인한다.
- 계산식, 분모, 시간대, 단위와 제외 조건을 기록한다.
- 재현 가능한 입력·쿼리·스냅샷을 보존한다.
- 샘플 결과를 전체 데이터 결론으로 과장하지 않는다.

## Mobile과 Desktop.

- unit, integration, emulator와 실제 기기 검증을 구분한다.
- 설치·업데이트·권한·오프라인·백그라운드 복귀를 확인한다.
- release signing과 store·installer 설정을 보호한다.
- 지원 OS와 하드웨어에서 성능과 저장 권한을 확인한다.

## Infrastructure.

- plan·preview 결과를 먼저 검토한다.
- 변경 범위, 비용, 권한, state와 drift를 확인한다.
- 사용자 승인 없이 production apply, destroy와 credential 변경을 수행하지 않는다.
- rollback과 관측 가능성을 준비한다.
