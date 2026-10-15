# 공개 참고와 작성 범위.

이 패키지는 기존 계약을 파악하고 최소 변경 전후를 검사하는 단순화 절차를 직접 작성했으며 저장소의 MIT License를 따른다. 타사 변환 예제·스킬 본문·라이선스 사본은 포함하지 않는다.

- [Addy Osmani의 코드 단순화 스킬](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/code-simplification/SKILL.md)은 동작 보존과 변경 범위 한정을 이해하는 공개 참고 자료다.
- [Git diff 공식 문서](https://git-scm.com/docs/git-diff)는 자신의 변경과 사용자 변경을 분리해 점검할 때 사용한다.

예제 변환이 현재 코드에서도 동치라고 가정하지 않는다. 실제 예외·부작용 순서·비동기 경계·타입·자원 소유권과 테스트로 판단한다.
