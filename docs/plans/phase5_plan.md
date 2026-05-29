# Phase 5 — 마무리 & 제출

> Parent plan: [`docs/plan.md`](../plan.md) §5 Phase 5, §9
> Subject reference: [`docs/subject.md`](../subject.md) §2

모든 PR·충돌·트러블슈팅이 완료된 뒤 **제출물을 한곳에 모으고** Definition of Done 체크리스트를 통과한다. 코드 추가 없이 문서·증거·인덱스 동기화만 수행한다.

---

## 1. Goal

- `git log --oneline --graph --all` 결과 캡처 (텍스트 또는 스크린샷).
- `SUBMISSION.md`에 멤버별 PR/이슈/리뷰/충돌·트러블슈팅 기여 링크 정리.
- README 함수 인덱스 **최종 동기화**.
- `docs/CONTRIBUTING.md` 5개 항목 본문 완성.
- §9 Definition of Done 전항목 통과.

---

## 2. Scope (In / Out)

**In scope**
- Git 히스토리 증거 캡처.
- `SUBMISSION.md` 완성.
- README·CONTRIBUTING 최종 편집.
- DoD 체크리스트 검증 PR (선택).

**Out of scope**
- 새 feature·새 충돌.
- 보너스 (`rebase -i`, CODEOWNERS — §10, DoD 충족 **후**).

---

## 3. Tasks

### 3.1 Git 히스토리 증거

```bash
git log --oneline --graph --all
```

- 출력을 **텍스트**로 `SUBMISSION.md`에 붙이거나 **스크린샷**으로 저장 후 링크.
- subject §2.3: 텍스트 또는 스크린샷 중 1택.

### 3.2 `SUBMISSION.md` 완성

멤버별 아래 항목 링크를 채운다:

| 항목 | 팀원1 | 팀원2 | 팀원3 |
| ---- | ----- | ----- | ----- |
| 머지된 PR (2+) | PR#1, PR#6 | PR#2, PR#4 | PR#3, PR#5 |
| 작성한 리뷰 (2+) | PR#3, PR#4 | PR#1, PR#5 | PR#2, PR#6 |
| 본인 PR 리뷰 반영 | (예: PR#1 slugify 수정) | (예: PR#2) | (예: PR#3) |
| 충돌 해결 기여 | PR#6 (충돌 B) | conflict-resolution.md | PR#3 (충돌 A) |
| 트러블슈팅 작성 | amend, stash | reset | revert |
| GitHub 프로필 | @... | @... | @... |

추가:
- **Org 레포 URL**
- **3개 협업 문서** 링크 (`CONTRIBUTING.md`, `conflict-resolution.md`, `troubleshooting-log.md`)
- **git log 증거** (§3.1)

### 3.3 README 함수 인덱스 최종 동기화

모든 utils 함수가 README 테이블에 반영되어 있는지 확인:

| 모듈 | 함수 | 작성자 |
| ---- | ---- | ------ |
| text_utils | slugify, truncate, word_count | 팀원1 |
| date_utils | days_between, to_iso | 팀원2 |
| number_utils | format_currency, clamp | 팀원3 |
| collection_utils | chunk, unique | 팀원2 |

각 함수에 **한 줄 사용 예시** 포함 (subject §4.11).

### 3.4 `docs/CONTRIBUTING.md` 본문 완성

Phase 0 헤더에 본문을 채운다 (`plan.md` §4):

1. **브랜치 네이밍**: `feature/<issue>-<summary>`
2. **커밋 컨벤션**: Conventional Commits (`feat:`, `fix:`, `docs:`, …)
3. **PR 본문**: What · Why · How + `Closes #N`
4. **코드 리뷰**: 구체 코멘트 1개+, LGTM 금지, 1라운드 응답
5. **충돌 흐름**: rebase → 마커 해석 → `conflict-resolution.md` 기록

### 3.5 Definition of Done 검증

`plan.md` §9 체크리스트를 **한 줄씩** 확인:

- [ ] Org 레포 + `main` 보호 규칙 (Phase 0)
- [ ] `CONTRIBUTING.md` 5항목 완성
- [ ] 모든 작업: 이슈 → feature → PR → `Closes #N`
- [ ] 멤버별 머지 PR 2 / 작성 리뷰 2 / 본인 PR 리뷰 반영 1회
- [ ] 충돌 기록 2건+, 비자명 1건+ → `conflict-resolution.md`
- [ ] 트러블슈팅 4종 → `troubleshooting-log.md`
- [ ] Simple Outcome (A): 멤버별 함수 1+, 사용 예시, 기여 커밋 1+
- [ ] `git log --graph --all` 증거
- [ ] `SUBMISSION.md` 멤버별 링크

### 3.6 마무리 PR (선택)

| 항목 | 값 |
| ---- | -- |
| 브랜치 | `docs/final-submission` |
| PR | `docs: finalize submission index and readme` |
| 내용 | SUBMISSION.md + README + CONTRIBUTING 최종 |

---

## 4. Files Touched

| File | Action |
| ---- | ------ |
| `SUBMISSION.md` | complete (멤버별 링크 + git log 증거) |
| `README.md` | 함수 인덱스·사용 예시 최종 동기화 |
| `docs/CONTRIBUTING.md` | 5항목 본문 완성 |

---

## 5. Acceptance Criteria

- [ ] `SUBMISSION.md`에 Org URL + 멤버별 PR/리뷰/충돌/트러블슈팅 링크.
- [ ] git log `--graph --all` 증거 첨부.
- [ ] README 함수 인덱스가 `src/utils/`와 일치.
- [ ] `CONTRIBUTING.md` 5항목 모두 본문 존재.
- [ ] §9 DoD 전항목 통과.
- [ ] `main` 브랜치가 최종 제출 상태.

---

## 6. Commit / PR

```
docs: finalize submission index, readme, and contributing guide
```

---

## 7. Risks / Notes

- SUBMISSION.md 링크가 **dead link**이면 감점 — PR 머지 후 URL 재확인.
- git log 캡처는 **모든 feature 브랜치 merge/rebase 히스토리**가 보이도록 `--all` 필수.
- 보너스(§10)는 DoD **전부** 통과 후 별도 브랜치로 — 마무리 PR과 섞지 않을 것.

---

## 8. Definition of Done

- subject §2 Final Deliverables 전항목 충족.
- 팀이 PR 기반 협업·충돌 해결·Git 복구 경험을 **기록으로 재현 가능**하게 남김.
- (선택) §10 보너스: `rebase -i` before/after, `.github/CODEOWNERS`.
