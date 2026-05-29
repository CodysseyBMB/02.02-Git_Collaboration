# Phase 4 — Git 트러블슈팅 4종 실습

> Parent plan: [`docs/plan.md`](../plan.md) §5 Phase 4, §7
> Subject reference: [`docs/subject.md`](../subject.md) §3-5, §4.9

전원이 **4개 복구 시나리오**를 실습하고 `docs/troubleshooting-log.md`에 기록한다. subject §4.9: 4종 모두 실습 + 멤버별 최소 1건 작성. 각 기록은 **상황 → 명령 → before/after → 배운 점 → 작성자** 순이다.

---

## 1. Goal

- `git commit --amend`, `git reset --soft HEAD~1`, `git revert <hash>`, `git stash` / `stash pop` 4종 실습.
- 각 시나리오별 before/after `git log --oneline` 캡처.
- `docs/troubleshooting-log.md` 4건 작성 (팀원3 총괄, 전원 분담).
- `reset` vs `revert` vs `stash` **언제 쓰는지** 팀이 설명할 수 있는 상태.

---

## 2. Scope (In / Out)

**In scope**
- 4 시나리오를 **별도 feature 브랜치** 또는 로컬 sandbox에서 실습 (main 직접 실험 금지).
- before/after 히스토리 텍스트 캡처.
- `troubleshooting-log.md` 4건.

**Out of scope**
- main 브랜치에 revert/amend 커밋 push (실습은 sandbox 브랜치).
- `SUBMISSION.md` 최종 정리 (Phase 5).
- 새 기능·충돌 작업.

---

## 3. Tasks

### 3.1 시나리오 분담

| # | 시나리오 | 명령 | 용도 | 기록 작성자 |
| - | -------- | ---- | ---- | ----------- |
| 1 | 커밋 메시지 수정 | `git commit --amend` | 직전 커밋 메시지 정정 | **팀원1** |
| 2 | 로컬 커밋 되돌리기 | `git reset --soft HEAD~1` | 커밋 취소·변경분 유지 | **팀원2** |
| 3 | 원격 커밋 되돌리기 | `git revert <hash>` | 이미 push된 커밋 안전 취소 | **팀원3** |
| 4 | 작업 임시 보관 | `git stash` / `git stash pop` | 브랜치 전환 전 작업 대피 | **팀원1** |

> 팀원1은 시나리오 1·4, 팀원2는 2, 팀원3은 3을 **작성**한다. **실습은 전원**이 각 시나리오를 직접 실행해 본다.

### 3.2 시나리오 1 — `git commit --amend` (팀원1 작성)

**상황**: feature 브랜치에서 `feat: add slugify` 커밋 후 메시지 오타 발견 (`slugfy`).

```bash
git checkout -b sandbox/amend-demo
# ... 작업 후 커밋
git commit -m "feat: add slugfy"          # before
git log --oneline -3                       # 캡처 ①

git commit --amend -m "feat: add slugify"
git log --oneline -3                       # 캡처 ② — hash 변경 확인
```

**배운 점**: amend는 **히스토리를 rewrite**한다. 이미 push한 커밋에 amend하면 force push가 필요하며 협업 시 위험.

### 3.3 시나리오 2 — `git reset --soft HEAD~1` (팀원2 작성)

**상황**: 커밋은 했지만 아직 push 전, 커밋을 쪼개고 싶음.

```bash
git checkout -b sandbox/reset-demo
git commit -m "feat: add slugify and truncate"   # before
git log --oneline -3                              # 캡처 ①

git reset --soft HEAD~1
git status                                        # staged 상태 확인
git commit -m "feat: add slugify"
git commit -m "feat: add truncate"
git log --oneline -3                              # 캡처 ②
```

**배운 점**: `--soft`는 변경분을 **staging area에 유지**. `--mixed`(기본)는 unstaged, `--hard`는 변경분 삭제(위험).

### 3.4 시나리오 3 — `git revert <hash>` (팀원3 작성)

**상황**: `main`에 이미 머지·push된 커밋에 버그가 있어 **안전하게 되돌리기**.

```bash
git checkout -b sandbox/revert-demo origin/main
git log --oneline -5                              # 캡처 ①
BUGGY_HASH=$(git log --oneline -1 --format=%H)   # 되돌릴 커밋

git revert $BUGGY_HASH --no-edit
git log --oneline -5                              # 캡처 ② — revert 커밋 추가
```

**배운 점**: revert는 **새 커밋**으로 이전 변경을 취소. push된 히스토리를 rewrite하지 않아 **협업에 안전**.

### 3.5 시나리오 4 — `git stash` / `stash pop` (팀원1 작성)

**상황**: feature 작업 중 긴급 hotfix 브랜치로 전환해야 함.

```bash
git checkout -b sandbox/stash-demo
# ... 파일 수정 (uncommitted)
git status                                        # 캡처 ① — dirty working tree

git stash push -m "WIP: slugify edge case"
git status                                        # clean
git checkout -b hotfix/quick-fix
# ... hotfix 작업 ...
git checkout sandbox/stash-demo
git stash pop
git status                                        # 캡처 ② — WIP 복원
```

**배운 점**: stash는 **커밋되지 않은 변경**을 임시 보관. pop 후 충돌 가능 — `stash list`로 관리.

### 3.6 `docs/troubleshooting-log.md` 템플릿

```markdown
## 시나리오 N — <제목>

### 상황
(어떤 문제/상황에서 이 명령이 필요했는지)

### 실행 명령
\`\`\`bash
(실제 실행한 명령)
\`\`\`

### Before
\`\`\`
(git log --oneline 캡처)
\`\`\`

### After
\`\`\`
(git log --oneline 캡처)
\`\`\`

### 배운 점
(reset vs revert vs stash 중 언제 이 명령을 쓰는지)

### 작성자
팀원N
```

### 3.7 PR (선택)

- `docs/troubleshooting-log.md` 작성 PR: `docs: add git troubleshooting log (4 scenarios)`.
- 리뷰어 1명 승인 후 Squash merge.

---

## 4. Files Touched

| File | Action |
| ---- | ------ |
| `docs/troubleshooting-log.md` | 4 시나리오 기록 작성 |

---

## 5. Acceptance Criteria

- [ ] 4 시나리오 모두 **전원 실습** 완료.
- [ ] `troubleshooting-log.md`에 4건, 각각 before/after + 배운 점 + 작성자.
- [ ] 멤버별 최소 1건 **작성** (팀원1: 2건, 팀원2: 1건, 팀원3: 1건).
- [ ] sandbox 브랜치 실습 — `main` 히스토리 오염 없음.
- [ ] 팀이 `reset` / `revert` / `stash` 차이를 구두로 설명 가능.

---

## 6. Commit / PR

```
docs: add git troubleshooting log for amend, reset, revert, stash
```

---

## 7. Risks / Notes

- **`git reset --hard`는 실습 금지** — 데이터 손실 위험. `--soft`만 사용.
- amend/revert 실습은 **sandbox 브랜치**에서만. main에 revert 커밋을 남기면 Phase 5 git log가 지저분해진다.
- revert 실습용 "버그 커밋"은 테스트용 더미 변경으로 만든다 (실제 utils 코드를 깨뜨리지 않을 것).
- stash pop 충돌 시 `git stash drop` 전에 충돌 해결 — 이것도 기록에 포함하면 가산점.

---

## 8. Definition of Done

- `troubleshooting-log.md` 4건 완성.
- subject §4.9 요구 충족.
- Phase 5 마무리(submission·git log 캡처) 시작 가능.
