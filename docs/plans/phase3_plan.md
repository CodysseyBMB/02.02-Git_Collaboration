# Phase 3 — 충돌 해결 & 기록

> Parent plan: [`docs/plan.md`](../plan.md) §5 Phase 3, §6
> Subject reference: [`docs/subject.md`](../subject.md) §3-4, §4.8

Phase 1·2에서 **의도적으로 남겨 둔 두 건의 충돌**을 로컬에서 재현·해결하고, `docs/conflict-resolution.md`에 과정을 남긴다. subject §4.8: **충돌 해결 기록 2건 이상, 비자명 충돌 1건 이상** — 본 설계는 두 건 모두 비자명 충돌이다.

---

## 1. Goal

- 충돌 A (`__init__.py` 인접 hunk) 로컬 rebase/merge로 재현·해결·PR 머지.
- 충돌 B (리네임 vs 내용 편집) 재현·해결·PR 머지.
- `docs/conflict-resolution.md`에 각 충돌별 **상황 / 마커 캡처 / 해결 선택·근거 / 결과 PR 링크** 기록.
- `main`이 모든 유틸 함수를 export하는 **깨끗한 상태**로 수렴.

---

## 2. Scope (In / Out)

**In scope**
- `git merge` 또는 `git rebase`로 충돌 재현.
- 충돌 마커(`<<<<<<<`, `=======`, `>>>>>>>`) 해석 및 수동 해결.
- 해결 커밋 push + PR 머지.
- `conflict-resolution.md` 2건 작성 (팀원2 총괄, 전원 보강).

**Out of scope**
- 트러블슈팅 4종 (`reset`, `revert`, `stash` — Phase 4).
- `SUBMISSION.md` 최종 정리 (Phase 5).
- 새 기능 추가.

---

## 3. Tasks

### 3.1 충돌 A — `__init__.py` 인접 hunk

| 항목 | 내용 |
| ---- | ---- |
| **상황** | PR#2(팀원2)·PR#3(팀원3)이 모두 `src/utils/__init__.py` export 블록에 import 라인 추가 |
| **재현** | PR#2 머지 후 PR#3 브랜치를 `main`에 `git rebase main` |
| **마커** | 같은 hunk에서 `<<<<<<<` / `=======` / `>>>>>>>` — 양쪽 import 라인 충돌 |
| **해결** | 두 import 라인 **모두 보존**, `__all__`에 6개 함수 전부 포함 |
| **담당** | 팀원3 해결 → 팀원2 `conflict-resolution.md` 정리 |

**재현 명령 예시**

```bash
git checkout feature/3-number-utils
git fetch origin
git rebase origin/main
# 충돌 발생 → __init__.py 편집
git add src/utils/__init__.py
git rebase --continue
git push --force-with-lease
```

**해결 후 `__init__.py` 목표 형태**

```python
from .text_utils import slugify, truncate
from .date_utils import days_between, to_iso
from .number_utils import format_currency, clamp

__all__ = [
    "slugify", "truncate",
    "days_between", "to_iso",
    "format_currency", "clamp",
]
```

### 3.2 충돌 B — 리네임 vs 내용 편집

| 항목 | 내용 |
| ---- | ---- |
| **상황** | PR#5(팀원3)는 `string_utils.py` → `text_utils.py` 리네임, PR#6(팀원1)은 같은 파일 내용 수정 |
| **재현** | PR#5 머지 후 PR#6 브랜치 `git rebase main` |
| **마커** | "deleted by us / modified by them" 또는 rename 감지 충돌 |
| **해결** | 최종 파일명 `text_utils.py`에 PR#6의 `word_count` 등 변경분 **통합** |
| **담당** | 팀원1·팀원3 합의, 팀원2 문서화 |

**재현 명령 예시**

```bash
git checkout feature/6-text-improve
git rebase origin/main
# rename/content 충돌 → text_utils.py에 양쪽 변경 반영
git add src/utils/text_utils.py
git rebase --continue
git push --force-with-lease
```

### 3.3 `docs/conflict-resolution.md` 템플릿

각 충돌마다 아래 섹션을 채운다:

```markdown
## 충돌 A — __init__.py 인접 hunk

### 발생 상황
(어떤 PR이 먼저 머지되었고, 어떤 브랜치 rebase 시 충돌이 났는지)

### 충돌 마커 캡처
\`\`\`
(<<<<<<< / ======= / >>>>>>> 포함 코드 스니펫 또는 스크린샷)
\`\`\`

### 마커 의미
- `<<<<<<< HEAD`: (현재 브랜치 쪽 내용)
- `=======`: 구분선
- `>>>>>>> commit`: (incoming 쪽 내용)

### 해결 선택과 근거
(왜 양쪽 import를 모두 보존했는지)

### 결과
- 해결 커밋: `<hash>`
- PR 링크: <url>
- 작성자: 팀원N
```

### 3.4 PR 머지 완료

- PR#3 (충돌 A 해결 후) → Squash merge.
- PR#6 (충돌 B 해결 후) → Squash merge.
- `main`에서 `python -c "from src.utils import *"` import smoke test.

---

## 4. Files Touched

| File | Action |
| ---- | ------ |
| `src/utils/__init__.py` | 충돌 A 해결 |
| `src/utils/text_utils.py` | 충돌 B 해결 |
| `README.md` | 충돌 해결 후 인덱스 동기화 |
| `docs/conflict-resolution.md` | 2건 기록 작성 |

---

## 5. Acceptance Criteria

- [ ] 충돌 A rebase 재현 → 해결 → PR#3 머지 완료.
- [ ] 충돌 B rebase 재현 → 해결 → PR#6 머지 완료.
- [ ] `conflict-resolution.md`에 2건, 각각 마커 캡처 + 해결 근거 + PR 링크.
- [ ] 비자명 충돌 **1건 이상** (본 설계: 2건 모두 비자명) 충족.
- [ ] `main`에서 모든 export 함수 import 가능.
- [ ] `git log --oneline --graph --all`에 merge/rebase 히스토리가 보임.

---

## 6. Commit / PR

```
fix: resolve __init__ export conflict between date and number utils   # PR#3
fix: integrate text_utils rename with word_count addition             # PR#6
docs: record conflict A and B resolution in conflict-resolution.md
```

---

## 7. Risks / Notes

- rebase 후 `--force-with-lease` push 시 다른 팀원과 coordinate — 같은 브랜치를 동시에 push하지 않을 것.
- 충돌 마커를 **그대로 커밋하면 안 됨** — 반드시 마커 제거 후 검증.
- "deleted by us" 충돌은 `git status`에서 `deleted`/`modified`로 표시될 수 있어, `git add` 대상 파일을 주의 깊게 확인.
- subject §3-4: 마커가 **무엇을 의미하는지** 문서에 반드시 설명.

---

## 8. Definition of Done

- PR#3·PR#6 모두 `main`에 머지.
- `conflict-resolution.md` 2건 완성.
- `main`이 Phase 4(트러블슈팅) 시작 가능한 안정 상태.
