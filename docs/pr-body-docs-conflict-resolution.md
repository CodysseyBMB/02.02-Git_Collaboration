## What

`docs/conflict-resolution.md`에 Phase 3 충돌 A(`__init__.py` 인접 hunk)와 충돌 B(`string_utils` 리네임 vs `word_count`) 해결 과정을 기록했습니다.

## Why

과제 §4.8 — 충돌 해결 기록 2건 이상, 비자명 충돌 1건 이상 충족.

## How

- 충돌 A: PR#1→#2→#3 머지 순서, 마커 예시, 커밋 `4f64cd9` / [PR #5](https://github.com/CodysseyBMB/02.02-Git_Collaboration/pull/5)
- 충돌 B: [PR #10](https://github.com/CodysseyBMB/02.02-Git_Collaboration/pull/10) 먼저 머지 후 [PR #14](https://github.com/CodysseyBMB/02.02-Git_Collaboration/pull/14) rebase·`string_utils` 통합, 머지 `fe04162`
- 문서 상단: 작성 팀원1 · 검토 팀원2·3

**팀원2·3**: 사실·링크·마커 설명 확인 후 Approve (LGTM 단독 금지, 구체 코멘트 1개 이상).
