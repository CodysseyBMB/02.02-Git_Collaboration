# Phase 2 — 2차 작업 + 리네임 충돌 유발

> Parent plan: [`docs/plan.md`](../plan.md) §5 Phase 2
> Subject reference: [`docs/subject.md`](../subject.md) §4.6, §4.7, §4.8, §4.11

Phase 1의 1차 유틸 위에 **2차 기능 추가**와 **모듈 리네임 vs 내용 편집** 충돌을 의도적으로 설계한다. PR#5(리네임)와 PR#6(내용 편집)이 같은 파일을 다르게 다루어 **비자명 충돌 B**를 만든다.

---

## 1. Goal

- `collection_utils` 모듈 추가 (팀원2).
- `string_utils.py` → `text_utils.py` **모듈 리네임** (팀원3) + README 인덱스 정리.
- 같은 `text_utils.py` **내용 수정** (팀원1, 함수 추가).
- PR#5·PR#6 머지 타이밍 겹침으로 **rename vs content edit 충돌** 전제 확보.
- 멤버별 **머지 PR 2번째** 완료 (§8 매트릭스 충족).

---

## 2. Scope (In / Out)

**In scope**
- 이슈 #4–#6 생성 및 PR#4–#6.
- `collection_utils.chunk`, `unique` 구현.
- `string_utils.py` → `text_utils.py` 리네임 (또는 역방향 시나리오 — 아래 §3.3 참고).
- `text_utils.py`에 함수 1개 추가 (예: `word_count`).
- PR·리뷰 1라운드 (Phase 1과 동일 규칙).

**Out of scope**
- 충돌 A·B **해결 및 문서화** (Phase 3).
- 트러블슈팅 실습 (Phase 4).
- `SUBMISSION.md` 최종 정리 (Phase 5).

---

## 3. Tasks

### 3.1 작업 매트릭스

| 이슈 | 브랜치 | PR | 작성자 | 내용 |
| ---- | ------ | -- | ------ | ---- |
| #4 | `feature/4-collection-utils` | PR#4 | **팀원2** | `collection_utils.chunk`, `unique` |
| #5 | `feature/5-rename-text` | PR#5 | **팀원3** | `string_utils.py` → `text_utils.py` 리네임 + README 인덱스 |
| #6 | `feature/6-text-improve` | PR#6 | **팀원1** | `text_utils.py` 내용 수정 (함수 추가) |

### 3.2 PR#4 — collection_utils (팀원2)

**`collection_utils.py`**
- `chunk(items: list, size: int) -> list[list]` — 고정 크기 분할.
- `unique(items: list) -> list` — 순서 유지 중복 제거.

- `__init__.py`에 export 추가.
- README 함수 인덱스 2행 추가.

### 3.3 PR#5·PR#6 — 리네임 vs 내용 편집 (충돌 B)

**사전 조건**: Phase 1에서 `text_utils.py`가 이미 존재한다. 충돌 B를 재현하려면 아래 시나리오 중 하나를 선택한다.

**시나리오 (plan.md §6 기준)**
1. 팀원3이 브랜치에서 `text_utils.py`를 `string_utils.py`로 **되돌리는 리네임** PR을 연다 (또는 역사상 `string_utils.py`가 있었다고 가정).
2. 팀원1이 **동시에** `text_utils.py`에 `word_count(text: str) -> int` 함수를 추가하는 PR#6을 연다.
3. **PR#5(리네임)를 먼저 머지** → PR#6 브랜치를 `main`에 rebase.
4. "deleted by us / modified by them" 또는 rename/content 충돌 발생.

**실행 단순화 (권장)**
- PR#5: 파일명 변경 + import 경로·README 일괄 수정.
- PR#6: 변경 전 파일명 기준으로 함수 추가 (리네임 PR과 base가 달라 충돌).
- Phase 3에서 `text_utils.py` 최종명에 PR#6 변경분을 통합.

### 3.4 머지 순서

1. **PR#4 (collection-utils)** — 독립적, 먼저 머지 가능.
2. **Phase 1 충돌 A** — PR#2·PR#3 중 하나 해결 후 머지 (Phase 3와 병행 가능).
3. **PR#5 (rename)** 먼저 머지.
4. **PR#6 (text-improve)** rebase → **충돌 B** 발생, Phase 3에서 해결.

### 3.5 PR·리뷰 분배 (Phase 2 구간)

| PR | 작성자 | 리뷰어(승인) |
| -- | ------ | ------------ |
| PR#4 | 팀원2 | 팀원1 |
| PR#5 | 팀원3 | 팀원2 |
| PR#6 | 팀원1 | 팀원3 |

---

## 4. Files Touched

| File | PR#4 | PR#5 | PR#6 |
| ---- | ---- | ---- | ---- |
| `src/utils/collection_utils.py` | edit | — | — |
| `src/utils/text_utils.py` | — | rename | edit |
| `src/utils/__init__.py` | edit | edit | edit |
| `README.md` | edit | edit | edit |

---

## 5. Acceptance Criteria

- [ ] PR#4 머지 완료, `chunk`·`unique` 사용 예시 README에 반영.
- [ ] PR#5·PR#6 open 상태에서 rebase 시 **비자명 충돌** 재현 (rename/content).
- [ ] 멤버별 머지 PR **2개** 달성 (§8 매트릭스).
- [ ] 멤버별 작성 리뷰 **2개** 달성.
- [ ] 본인 PR에 리뷰 반영 **1회 이상** (Phase 1·2 합산).

---

## 6. Commit / PR

```
feat: add collection chunk and unique helpers     # PR#4
refactor: rename string_utils to text_utils       # PR#5
feat: add word_count to text utils                # PR#6
```

---

## 7. Risks / Notes

- 리네임 PR과 내용 PR의 **base commit**을 맞추지 않으면 충돌이 발생하지 않을 수 있다 — 두 PR을 동시에 open하고 PR#5 먼저 머지할 것.
- Git은 rename을 "삭제 + 추가"로 감지할 수 있어 충돌 마커가 직관적이지 않을 수 있다 — Phase 3 문서에 **마커 의미**를 반드시 기록.
- PR#4는 충돌과 무관하므로 Phase 1 충돌 A 해결 전후 어느 때든 머지 가능.

---

## 8. Definition of Done

- PR#4 머지, PR#5 머지, PR#6 충돌 상태(open 또는 rebase 충돌 재현).
- 충돌 A(Phase 1) + 충돌 B(Phase 2) 두 건 모두 Phase 3 기록 대상으로 준비됨.
- §8 멤버별 PR·리뷰 최소치 충족.
