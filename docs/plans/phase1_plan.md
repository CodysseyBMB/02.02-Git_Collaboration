# Phase 1 — 멤버별 유틸 1차 작성 (병렬)

> Parent plan: [`docs/plan.md`](../plan.md) §5 Phase 1
> Subject reference: [`docs/subject.md`](../subject.md) §4.4, §4.5, §4.6, §4.7, §4.11

세 명이 **동시에** 각자 이슈·브랜치·PR을 만든다. `__init__.py`와 README 함수 인덱스를 **의도적으로 동시 편집**해, Phase 2–3에서 충돌 시나리오 A의 전제를 만든다. PR#1을 먼저 머지하고 PR#2·PR#3은 나중에 머지해 충돌을 유발한다.

---

## 1. Goal

- 멤버별 유틸 함수 1차 구현 + `__init__.py` 재노출.
- 이슈 → `feature/*` → PR → 리뷰 → 머지 사이클을 **3회** 완료.
- 멤버별 **머지 PR 1개 / 작성 리뷰 1개** 이상 충족 (Phase 2에서 2개째).
- PR#2·PR#3 머지 시 `__init__.py` **인접 hunk 충돌** 전제 조건 확보.

---

## 2. Scope (In / Out)

**In scope**
- 이슈 #1–#3 생성.
- `text_utils`, `date_utils`, `number_utils` 함수 구현.
- 각 PR에서 `src/utils/__init__.py` export 추가 + README 함수 인덱스 1줄 추가.
- PR 본문 (What · Why · How) + `Closes #N`.
- 리뷰: 구체 코멘트 1개 이상 + 작성자 1라운드 응답.

**Out of scope**
- `collection_utils` (Phase 2, 이슈 #4).
- 모듈 리네임 충돌 (Phase 2, 이슈 #5–#6).
- 충돌 해결 기록 (Phase 3).
- `CONTRIBUTING.md` 본문 완성 (Phase 1 전후 보강).

---

## 3. Tasks

### 3.1 병렬 작업 매트릭스

| 이슈 | 브랜치 | PR | 작성자 | 구현 내용 |
| ---- | ------ | -- | ------ | --------- |
| #1 | `feature/1-text-utils` | PR#1 | **팀원1** | `text_utils.slugify`, `truncate` + `__init__` 재노출 |
| #2 | `feature/2-date-utils` | PR#2 | **팀원2** | `date_utils.days_between`, `to_iso` + `__init__` 재노출 |
| #3 | `feature/3-number-utils` | PR#3 | **팀원3** | `number_utils.format_currency`, `clamp` + `__init__` 재노출 |

### 3.2 함수 구현 가이드

**`text_utils.py` (팀원1)**
- `slugify(text: str) -> str` — 소문자·공백→하이픈 변환.
- `truncate(text: str, max_len: int) -> str` — 초과 시 `...` 접미.

**`date_utils.py` (팀원2)**
- `days_between(a: date, b: date) -> int` — 두 날짜 간 일수.
- `to_iso(d: date) -> str` — `YYYY-MM-DD` 문자열.

**`number_utils.py` (팀원3)**
- `format_currency(amount: float, symbol: str = "$") -> str` — 통화 포맷.
- `clamp(value: float, lo: float, hi: float) -> float` — 범위 제한.

### 3.3 공통 수정 파일 (충돌 유발 지점)

각 PR 작성자는 아래 두 파일을 **동시에** 수정한다:

1. `src/utils/__init__.py` — 자신의 함수를 import·재노출.
2. `README.md` — 함수 인덱스 테이블에 1행 추가.

```python
# __init__.py 예시 (각 PR이 export 블록에 줄 추가)
from .text_utils import slugify, truncate
from .date_utils import days_between, to_iso
from .number_utils import format_currency, clamp

__all__ = ["slugify", "truncate", "days_between", "to_iso", "format_currency", "clamp"]
```

### 3.4 머지 순서 (충돌 전제)

1. **PR#1 (팀원1) 먼저 머지** — 충돌 없음.
2. **PR#2 (팀원2) 머지** — PR#1 반영 후 rebase/merge → 충돌 없을 수 있음.
3. **PR#3 (팀원3) 머지 시도** — PR#2가 이미 `__init__.py` export 블록을 수정했으므로 **인접 hunk 충돌 발생** (= 충돌 A, `plan.md` §6).

> Phase 1에서는 충돌을 **일부러 해결하지 않고** PR#3을 open 상태로 두거나, 로컬 rebase로 충돌을 재현만 한다. 실제 해결·기록은 Phase 3.

### 3.5 PR·리뷰 분배 (Phase 1 구간)

| PR | 작성자 | 리뷰어(승인) | 추가 리뷰어 |
| -- | ------ | ------------ | ----------- |
| PR#1 | 팀원1 | 팀원2 | 팀원3 |
| PR#2 | 팀원2 | 팀원3 | 팀원1 |
| PR#3 | 팀원3 | 팀원1 | 팀원2 |

리뷰 품질: "LGTM" 금지. 예 — PR#1에서 팀원2가 `slugify` 유니코드 처리 누락 지적 → 팀원1 커밋 반영.

---

## 4. Files Touched

| File | PR#1 | PR#2 | PR#3 |
| ---- | ---- | ---- | ---- |
| `src/utils/text_utils.py` | edit | — | — |
| `src/utils/date_utils.py` | — | edit | — |
| `src/utils/number_utils.py` | — | — | edit |
| `src/utils/__init__.py` | edit | edit | edit |
| `README.md` | edit | edit | edit |

---

## 5. Acceptance Criteria

- [ ] 이슈 #1–#3이 생성되고 각 PR에 `Closes #N`이 있다.
- [ ] PR#1이 Squash merge로 `main`에 반영되었다.
- [ ] PR#2·PR#3 브랜치가 `main` rebase 시 `__init__.py`에서 충돌 마커가 나타난다 (충돌 A 재현).
- [ ] 멤버별 Conventional Commits (`feat:`) 커밋 1개 이상.
- [ ] 멤버별 작성 리뷰 1개 이상 (본인 PR 제외).
- [ ] README 함수 인덱스에 6개 함수(각 2개)가 나열되어 있다 (충돌 해결 후).

---

## 6. Commit / PR

```
feat: add <module> utility functions
```

PR 본문 예시 (PR#1):

```
## What
text_utils.slugify, truncate 구현 및 __init__ 재노출.

## Why
Simple Outcome (A) 유틸 함수 모음 — 팀원1 담당 모듈 1차 기여.

## How
python -c "from src.utils import slugify; print(slugify('Hello World'))"
→ hello-world

Closes #1
```

---

## 7. Risks / Notes

- 세 PR을 **동시에 open**한 뒤 PR#1만 먼저 머지해야 충돌 A가 자연스럽게 발생한다.
- PR#3 충돌 해결을 Phase 1에서 하면 Phase 3 기록 대상이 사라진다 — **해결은 Phase 3으로 미룬다**.
- `__init__.py` export 순서는 팀원1→2→3 합의로 알파벳 정렬 등 규칙을 정해 두면 Phase 3 해결이 수월하다.

---

## 8. Definition of Done

- PR#1 머지 완료, PR#2·PR#3 open (또는 충돌 상태 재현 완료).
- 멤버별 함수 2개 + `__init__` 재노출 + README 인덱스 1행 기여.
- Phase 2에서 `collection_utils`·리네임 작업을 시작할 수 있는 `main` 상태 (PR#1 기준).
