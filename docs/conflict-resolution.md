# 충돌 해결 기록 (conflict-resolution.md)

Phase 3에서 의도적으로 발생시킨 충돌 2건 이상(비자명 1건 이상)의 해결 과정을 기록합니다.

> 작성: 팀원1 · 검토: 팀원2, 팀원3

---

## 충돌 A — `__init__.py` 인접 hunk

> Phase 1 PR#2·PR#3 머지 시 export 블록 충돌 ([plan.md](plan.md) §6)

### 발생 상황

Phase 1에서 세 멤버가 동시에 `src/utils/__init__.py` export 블록을 수정했다 ([phase1-coordination.md](phase1-coordination.md) 합의).

1. **PR#1** (`feature/1-text-utils`, 팀원1) — `text_utils` import 먼저 머지
2. **PR#2** (`feature/2-date-utils`, 팀원2) — `date_utils` import 추가 후 머지 (GitHub PR [#8](https://github.com/CodysseyBMB/02.02-Git_Collaboration/pull/8))
3. **PR#3** (`feature/3-number-utils`, 팀원3) — `number_utils` import 추가 시도 (GitHub PR [#5](https://github.com/CodysseyBMB/02.02-Git_Collaboration/pull/5))

PR#1·PR#2가 `main`에 반영된 뒤, 팀원3 브랜치가 최신 `main`을 `git merge main` 하면서 **같은 export 블록 인접 hunk**에서 충돌이 발생했다.

### 충돌 마커 캡처

대표 마커 예시 (`src/utils/__init__.py`):

```python
<<<<<<< HEAD
from .date_utils import days_between, to_iso
from .text_utils import slugify, truncate

__all__ = ["days_between", "to_iso", "slugify", "truncate"]
=======
from .number_utils import format_currency, clamp

__all__ = ["format_currency", "clamp"]
>>>>>>> feature/3-number-utils
```

`git merge` 결과 diff (`4f64cd9`)에서는 양쪽 import가 한 파일에 합쳐졌다:

```python
from .number_utils import format_currency, clamp
from .date_utils import days_between, to_iso
from .text_utils import slugify, truncate

__all__ = ["days_between", "to_iso", "slugify", "truncate", "format_currency", "clamp"]
```

### 마커 의미

- `<<<<<<< HEAD`: 이미 `main`에 반영된 **date·text** utils import/export
- `=======`: 구분선
- `>>>>>>> feature/3-number-utils`: 팀원3 브랜치의 **number** utils import/export

### 해결 선택과 근거

각 PR은 서로 다른 모듈의 공개 함수만 추가했으므로, 한쪽 import를 버리면 해당 모듈을 `from src.utils import ...`로 쓸 수 없다. **date·text·number 세 import를 모두 보존**하고 `__all__`에 6개 함수를 모두 포함하도록 통합했다.

### 결과

- 해결 커밋: `4f64cd9` (Merge branch `main` into `feature/3-number-utils`)
- 머지 PR: `022bf18` — [GitHub PR #5](https://github.com/CodysseyBMB/02.02-Git_Collaboration/pull/5) (`feature/3-number-utils`)
- 작성·기록: 팀원1 (Phase 3 문서), 충돌 해결 당시: 팀원3

---

## 충돌 B — `string_utils` 리네임 vs `word_count` 추가

> Phase 2 PR#5·PR#6 동시 편집 ([plan.md](plan.md) §6) — **비자명 충돌** (rename vs content edit)

### 발생 상황

1. **PR#5** (팀원3): `text_utils.py` → `string_utils.py` 리네임 + `__init__.py`·README 모듈명 변경 — 먼저 머지 ([GitHub PR #10](https://github.com/CodysseyBMB/02.02-Git_Collaboration/pull/10), 커밋 `a0e64d7`)
2. **PR#6** (팀원1): PR#5 머지 **이전** `main`에서 분기, `text_utils.py`에 `word_count` 추가

PR#5가 `main`에 반영된 뒤 PR#6 브랜치를 `git rebase origin/main` 하면서, Git은 **한쪽은 파일 삭제(리네임)·한쪽은 같은 경로 수정**으로 인식했다. GitHub 웹 에디터에서는 "too complex to resolve"로 표시되어 **로컬 rebase**로 해결했다.

### 충돌 마커 캡처

`git status` (요약):

```text
both modified:   README.md
both modified:   src/utils/__init__.py
# text_utils.py — main(HEAD)에서는 삭제·리네임됨, PR#6에서는 수정됨
```

`src/utils/__init__.py`:

```python
<<<<<<< HEAD
from .string_utils import slugify, truncate
=======
from .text_utils import slugify, truncate, word_count
>>>>>>> feat: add word_count to text utils
```

`README.md`: `string_utils` 행(HEAD) vs `text_utils` + `word_count` 행(incoming) 충돌.

### 마커 의미

- `<<<<<<< HEAD`: 리네임이 반영된 `main` — `string_utils`, `collection_utils` 등
- `=======`: 구분선
- `>>>>>>> feat: add word_count to text utils`: PR#6 — 구 파일명 `text_utils` 기준 + `word_count`

### 해결 선택과 근거

팀 합의로 **최종 모듈명은 `string_utils.py` 유지**(PR#5 리네임 존중). PR#6의 `word_count`는 `string_utils.py`에 통합하고 `text_utils.py`는 제거했다. `__init__.py`는 `from .string_utils import slugify, truncate, word_count` 및 `collection_utils` export를 모두 포함하도록 정리했다.

비자명 충돌: 파일명 변경과 내용 수정이 겹쳐 단순 줄 단위 merge만으로는 해결되지 않는다.

로컬 검증:

```bash
python3 -c "from src.utils import slugify, word_count, chunk; print(word_count('hello world'), chunk([1,2,3], 2))"
# 2 [[1, 2], [3]]
```

### 결과

- rebase 해결 커밋: `a41d7a2` (`feat: add word_count to text utils`)
- `main` 머지: `fe04162` — [GitHub PR #14](https://github.com/CodysseyBMB/02.02-Git_Collaboration/pull/14) (`feature/6-text-improve`, Squash merge)
- 작성: 팀원1 · 검토 예정: 팀원2, 팀원3
