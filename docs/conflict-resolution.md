# 충돌 해결 기록 (conflict-resolution.md)

Phase 3에서 의도적으로 발생시킨 충돌 2건 이상(비자명 1건 이상)의 해결 과정을 기록합니다.

---

## 충돌 A — `__init__.py` 인접 hunk

> Phase 1 PR#2·PR#3 머지 시 export 블록 충돌 (plan.md §6)

### 발생 상황

Phase 1에서 팀원1의 text utils PR(#6), 팀원2의 date utils PR(#8), 팀원3의 number utils PR(#5)가 모두 `src/utils/__init__.py`의 import/export 영역을 수정했다.

팀원1·팀원2 PR이 먼저 `main`에 반영된 뒤, 팀원3의 `feature/3-number-utils` 브랜치가 최신 `main`을 병합하면서 같은 export 블록 근처에서 충돌이 발생했다. 해결 커밋 `4f64cd9`에서 `README.md`와 `src/utils/__init__.py`가 함께 정리되었다.

### 충돌 마커 캡처

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

### 마커 의미

- `<<<<<<< HEAD`: 먼저 반영된 `main` 쪽 내용으로, text/date utils import와 export가 포함되어 있다.
- `=======`: 현재 브랜치 내용과 병합 대상 내용을 나누는 구분선이다.
- `>>>>>>> feature/3-number-utils`: 팀원3 브랜치 쪽 내용으로, number utils import와 export가 포함되어 있다.

### 해결 선택과 근거

각 PR이 서로 다른 담당 모듈의 공개 함수를 추가한 것이므로 한쪽을 버리면 특정 팀원의 기능이 `src.utils`에서 import되지 않는다. 따라서 text/date/number utils import를 모두 보존하고, `__all__`에도 6개 함수를 모두 포함하도록 통합했다.

### 결과

- 해결 커밋: `4f64cd9`
- PR 링크: https://github.com/CodysseyBMB/02.02-Git_Collaboration/pull/5
- 작성자: 팀원3 해결, 팀원2 기록

---

## 충돌 B — `text_utils.py` 리네임 vs 수정

> Phase 2 PR#5·PR#6 동시 편집 (plan.md §6)

### 발생 상황

Phase 2에서 팀원3은 PR #10에서 `src/utils/text_utils.py`를 `src/utils/string_utils.py`로 리네임하고, `src/utils/__init__.py`와 `README.md`의 모듈명을 `string_utils` 기준으로 변경했다.

동시에 팀원1은 PR #14에서 기존 문자열 유틸 모듈에 `word_count(text: str) -> int`를 추가했다. 리네임 PR이 먼저 `main`에 머지된 뒤 팀원1 브랜치를 최신 `main` 기준으로 병합하면서, Git은 같은 원본 파일에 대해 한쪽은 리네임하고 다른 한쪽은 내용을 수정한 것으로 판단했다.

### 충돌 마커 캡처

```text
CONFLICT (modify/delete): src/utils/text_utils.py deleted in HEAD and modified in feature/6-text-improve.
CONFLICT (rename/modify): src/utils/text_utils.py renamed to src/utils/string_utils.py in HEAD, but modified in feature/6-text-improve.
```

```python
 <<<<<<< HEAD:src/utils/string_utils.py
def truncate(text: str, max_len: int) -> str:
    ...
 =======
def truncate(text: str, max_len: int) -> str:
    ...


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words."""
    if not text or not text.strip():
        return 0
    return len(text.split())
 >>>>>>> feature/6-text-improve:src/utils/text_utils.py
```

### 마커 의미

- `<<<<<<< HEAD:src/utils/string_utils.py`: 먼저 머지된 `main` 쪽 내용으로, 리네임 이후의 파일명과 기존 문자열 유틸 함수가 기준이 된다.
- `=======`: 리네임된 파일 내용과 팀원1 브랜치의 내용 수정분을 구분한다.
- `>>>>>>> feature/6-text-improve:src/utils/text_utils.py`: 팀원1 브랜치에서 기존 파일명 기준으로 추가한 `word_count` 변경분이다.

### 해결 선택과 근거

최종 모듈명은 먼저 머지된 리네임 PR의 결정에 맞춰 `string_utils.py`로 유지했다. 다만 팀원1의 `word_count`도 문자열 유틸 함수로 필요한 변경이므로, `string_utils.py` 안에 `slugify`, `truncate`, `word_count`가 모두 남도록 통합했다.

또한 `src/utils/__init__.py`는 `.string_utils import slugify, truncate, word_count`를 사용하도록 정리했고, `README.md` 함수 인덱스도 `string_utils.word_count`를 포함하도록 맞췄다.

### 결과

- 해결 커밋: `a41d7a2`
- PR 링크: https://github.com/CodysseyBMB/02.02-Git_Collaboration/pull/14
- 작성자: 팀원1 해결, 팀원2 기록
