# Git Workflow 미션 진행 계획 (plan.md) — 3인 협업 시나리오

본 문서는 `docs/subject.md` 의 기능 요구사항(§4.1~§4.11)과 제출물(§2)을 **3명이 진행하는 구체 시나리오**로 옮긴 실행 계획이다. 미션의 목적은 코드 구현이 아니라 **PR 기반 협업·코드 리뷰·충돌 해결·복구 명령 경험을 재현 가능한 기록으로 남기는 것**(subject §1, §3)이므로, 본 계획의 핵심은 "어떤 산출물을 어떤 순서로 만들고, 어디서 충돌을 의도적으로 발생시키며, 누가 무엇을 기록하는가"의 타임라인이다.

---

## 1. 팀 구성 & 역할 (3인)


| 멤버     | 역할                   | 담당 유틸 모듈                               | 비고                                      |
| ------ | -------------------- | -------------------------------------- | --------------------------------------- |
| **팀원1** | 리포 리드 / GitHub 설정 담당 | `text_utils.py`                        | Org·브랜치 보호 규칙 세팅, `CONTRIBUTING.md` 총괄  |
| **팀원2** | 리뷰 코디네이터             | `date_utils.py`, `collection_utils.py` | 리뷰 라운드 진행, `conflict-resolution.md` 총괄  |
| **팀원3** | 문서/품질 담당             | `number_utils.py`                      | README 인덱스, `troubleshooting-log.md` 총괄 |


> 역할은 "총괄"일 뿐 문서는 **모두가 분담 작성**한다(subject §4.10). 각 문서 안에 작성자 이름/역할을 명시한다.

---

## 2. 사전 고정 결정 (Locked Decisions)

subject 가 "안 A / 안 B" 중 선택을 요구하거나, 미리 굳혀야 협업이 꼬이지 않는 항목.


| 항목                             | 결정                                                                                  | 근거                                                 |
| ------------------------------ | ----------------------------------------------------------------------------------- | -------------------------------------------------- |
| 리포 형태 (subject §4.1)           | **안 A · GitHub Organization 레포**                                                    | 권장안, 권한·브랜치 보호 관리가 명확                              |
| 브랜치 전략 (subject §4.3)          | **GitHub Flow** (`main` + `feature/`*)                                              | 소규모·짧은 주기 협업에 적합, 배포 가능 상태 유지가 단순                  |
| Simple Outcome (subject §4.11) | **(A) 유틸 함수 모음 (Python)**                                                           | 멤버별 함수 1개 이상 + 같은 파일 동시 편집으로 **충돌을 자연스럽게 유발**하기 좋음 |
| 브랜치 네이밍                        | `feature/<issue번호>-<요약>` (예: `feature/12-add-slugify`)                              | 이슈-브랜치-PR 추적성 (subject §4.4)                       |
| 커밋 컨벤션 (subject §4.5)          | **Conventional Commits** (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`) | 레포 `.cursorrules §6` 와 일치                          |
| main 보호 (subject §4.2)         | 직접 push 금지 · PR 머지만 허용 · **승인 1개 이상 필수**                                            | subject 요구 그대로                                     |
| 머지 방식                          | **Squash and merge** (개인 feature 한정)                                                | 히스토리 깔끔, 보너스 `rebase -i` 와 별개                      |


---

## 3. 레포 구조 (subject §4.1)

```
02-2.git_workflow/   (= 팀 GitHub 레포 루트로 매핑)
├── README.md                     # 프로젝트 소개·실행법·GitHub Flow 선택 이유(3줄)·유틸 함수 인덱스
├── SUBMISSION.md                 # 멤버별 PR/이슈/증거 링크 제출 인덱스 (subject §2.1)
├── docs/
│   ├── subject.md
│   ├── plan.md                   # (본 문서)
│   ├── plans/                    # Phase 0–5 실행 계획 (phase0_plan.md … phase5_plan.md)
│   ├── CONTRIBUTING.md           # 협업 규칙 (subject §4.10)
│   ├── conflict-resolution.md    # 충돌 해결 기록 (subject §4.8)
│   └── troubleshooting-log.md    # Git 복구 4종 기록 (subject §4.9)
├── src/
│   └── utils/
│       ├── __init__.py           # 각 모듈 함수 재노출 (충돌 발생 지점)
│       ├── text_utils.py         # 팀원1
│       ├── date_utils.py         # 팀원2
│       ├── collection_utils.py   # 팀원2
│       └── number_utils.py       # 팀원3
└── tests/                        # (선택) 함수별 간단 검증
```

> `src/utils/__init__.py` 와 `README.md` 의 "함수 인덱스" 두 곳은 **모든 멤버가 동시에 같은 줄 근처를 수정**하게 되어 §6 의 충돌 시나리오를 자연스럽게 만든다.

---

## 4. 협업 산출물 문서 (subject §2.2)


| 문서                            | 최소 포함 내용                                                                                  | 1차 작성 책임   |
| ----------------------------- | ----------------------------------------------------------------------------------------- | ---------- |
| `docs/CONTRIBUTING.md`        | 브랜치 네이밍 / 커밋 컨벤션 / PR 본문 규칙(What·Why·How) / 코드 리뷰 규칙(최소 품질) / 충돌 발생 시 기본 흐름(누가·어떻게·어디 기록) | 팀원1 (전원 보강) |
| `docs/conflict-resolution.md` | 충돌별: 발생 상황 / 충돌 마커 캡처 / 해결 선택과 근거 / 결과 커밋·PR 링크                                           | 팀원2         |
| `docs/troubleshooting-log.md` | 4개 시나리오별: 상황 / 명령 / before·after / 배운 점 / 작성자                                             | 팀원3         |


`git log --oneline --graph --all` 결과(텍스트 또는 스크린샷)는 미션 막바지에 캡처해 `SUBMISSION.md` 에 첨부한다(subject §2.3).

---

## 5. 단계별 진행 시나리오 (Phases)

각 단계는 이슈 → `feature/`* 브랜치 → PR → 리뷰 → 머지의 한 사이클이다. **모든 머지는 PR 경유**(subject §4.6).

> 상세 실행 계획: [`docs/plans/phase0_plan.md`](plans/phase0_plan.md) … [`phase5_plan.md`](plans/phase5_plan.md)

### Phase 0 — 리포·규칙 세팅 (팀원1)

- Org 레포 생성, `main` 브랜치 보호 규칙 설정(직접 push 금지, PR+승인 1 필수). (subject §4.2)
- 초기 스캐폴딩 PR: `chore:` 디렉터리 구조 + `src/utils/__init__.py`(빈 골격) + 문서 뼈대.
- README 에 **GitHub Flow 선택 이유 3줄**(subject §4.3) 기록.
- 이 PR도 보호 규칙 검증을 겸해 PR로 머지(셀프 머지 대신 다른 멤버 1명 승인).

### Phase 1 — 멤버별 유틸 1차 작성 (병렬)

세 명이 **동시에** 각자 이슈를 만들고 브랜치를 판다. 여기서 `__init__.py`/README 동시 편집으로 충돌이 발생하도록 일부러 머지 타이밍을 겹친다.


| 이슈  | 브랜치                      | PR (작성자)      | 내용                                                       |
| --- | ------------------------ | ------------- | -------------------------------------------------------- |
| #1  | `feature/1-text-utils`   | **PR#1 (팀원1)** | `text_utils.slugify`, `truncate` + `__init__` 재노출        |
| #2  | `feature/2-date-utils`   | **PR#2 (팀원2)** | `date_utils.days_between`, `to_iso` + `__init__` 재노출     |
| #3  | `feature/3-number-utils` | **PR#3 (팀원3)** | `number_utils.format_currency`, `clamp` + `__init__` 재노출 |


→ PR#1 먼저 머지. PR#2·PR#3 은 `__init__.py` 같은 영역을 수정했으므로 **나중에 머지되는 쪽에서 충돌 발생** (= 충돌 시나리오 A, §6).

### Phase 2 — 2차 작업 + 리네임 충돌 유발


| 이슈  | 브랜치                          | PR (작성자)      | 내용                                                               |
| --- | ---------------------------- | ------------- | ---------------------------------------------------------------- |
| #4  | `feature/4-collection-utils` | **PR#4 (팀원2)** | `collection_utils.chunk`, `unique`                               |
| #5  | `feature/5-rename-text`      | **PR#5 (팀원3)** | `string_utils.py` → `text_utils.py` 로 **모듈 리네임** + README 인덱스 정리 |
| #6  | `feature/6-text-improve`     | **PR#6 (팀원1)** | 같은 `text_utils.py` **내용 수정**(함수 추가)                              |


→ PR#5(리네임)와 PR#6(내용 편집)이 같은 파일을 다르게 다뤄 **rename vs content edit 충돌** 발생 (= 충돌 시나리오 B, §6, subject §4.8 비자명 충돌).

### Phase 3 — 충돌 해결 & 기록

- §6 의 두 충돌을 각각 로컬에서 `git merge`/`rebase` 로 재현·해결하고 `docs/conflict-resolution.md` 에 기록.
- 해결 커밋·PR 링크를 문서에 남긴다.

### Phase 4 — 트러블슈팅 4종 실습 (§7)

- 4개 복구 시나리오를 전원이 실습하고 `docs/troubleshooting-log.md` 에 작성자 표기와 함께 기록.

### Phase 5 — 마무리

- `git log --oneline --graph --all` 캡처.
- `SUBMISSION.md` 에 멤버별 PR/이슈/리뷰/충돌·트러블슈팅 기여 링크 정리.
- README 의 함수 인덱스 최종 동기화.

---

## 6. 충돌 시나리오 상세 (subject §4.8)

전체 팀 기준 **충돌 해결 기록 2건 이상**, 그중 **비자명 충돌 1건 이상**을 만족시키기 위해 아래 2건을 설계한다(둘 다 비자명).

### 충돌 A — 같은 파일 인접 hunk (`__init__.py`)

- 상황: PR#2(팀원2)·PR#3(팀원3)이 모두 `src/utils/__init__.py` 의 동일한 export 블록(인접 줄)에 import 라인을 추가.
- 재현: PR#2 머지 후 PR#3 브랜치를 `main` 에 rebase → 같은 hunk 충돌.
- 해결: 두 import 라인을 **모두 보존**하도록 마커(`<<<<<<<`/`=======`/`>>>>>>>`) 정리.
- 담당/기록: 팀원3가 해결 → 팀원2가 `conflict-resolution.md` 정리.

### 충돌 B — 리네임 vs 내용 편집 (`string_utils.py`)

- 상황: PR#5(팀원3)는 `string_utils.py` → `text_utils.py` 리네임, PR#6(팀원1)은 같은 파일 내용 수정.
- 재현: 리네임 PR 먼저 머지 후 내용 편집 브랜치 rebase → "deleted by us / modified by them" 류 충돌.
- 해결: 새 파일명(`text_utils.py`)에 내용 변경분을 반영하는 방향으로 합의·통합.
- 담당/기록: 팀원1·팀원3 합의, 팀원2가 문서화.

> 충돌 마커가 무엇을 의미하는지(subject §3-4)와 해결 선택의 근거를 문서에 반드시 남긴다.

---

## 7. Git 트러블슈팅 4종 (subject §4.9)

전원이 4개 시나리오를 모두 실습하되, 각 시나리오 **기록 작성자**는 아래처럼 분담(멤버별 최소 1개 작성, subject §4.9).


| 시나리오       | 명령                        | 용도                | 기록 작성자 |
| ---------- | ------------------------- | ----------------- | ------ |
| 커밋 메시지 수정  | `git commit --amend`      | 직전 커밋 메시지 정정      | **팀원1** |
| 로컬 커밋 되돌리기 | `git reset --soft HEAD~1` | 커밋 취소·변경분 유지      | **팀원2** |
| 원격 커밋 되돌리기 | `git revert <hash>`       | 이미 push된 커밋 안전 취소 | **팀원3** |
| 작업 임시 보관   | `git stash` / `stash pop` | 브랜치 전환 전 작업 대피    | **팀원1** |


각 기록은 상황 → 실행 명령 → before/after 히스토리 → 배운 점 순으로 작성한다.

---

## 8. PR·리뷰 분배 매트릭스 (subject §4.6, §4.7)

멤버별 최소: **머지된 PR 2개 / 작성한 리뷰 2개(본인 PR 제외) / 본인 PR 리뷰 반영 1회 이상**.


| PR                    | 작성자 | 리뷰어(승인) | 추가 리뷰어 |
| --------------------- | --- | ------- | ------ |
| PR#1 text-utils       | 팀원1  | 팀원2      | 팀원3     |
| PR#2 date-utils       | 팀원2  | 팀원3      | 팀원1     |
| PR#3 number-utils     | 팀원3  | 팀원1      | 팀원2     |
| PR#4 collection-utils | 팀원2  | 팀원1      | —      |
| PR#5 rename-text      | 팀원3  | 팀원2      | —      |
| PR#6 text-improve     | 팀원1  | 팀원3      | —      |


**멤버별 합계 확인**


| 멤버  | 머지 PR          | 작성 리뷰           | 비고  |
| --- | -------------- | --------------- | --- |
| 팀원1  | PR#1, PR#6 (2) | PR#3, PR#4 (2+) | OK  |
| 팀원2  | PR#2, PR#4 (2) | PR#1, PR#5 (2+) | OK  |
| 팀원3  | PR#3, PR#5 (2) | PR#2, PR#6 (2+) | OK  |


**리뷰 품질(subject §4.7)**: 각 리뷰는 "LGTM" 금지, **라인/파일 단위의 구체 코멘트(질문·대안·리스크·개선 제안) 1개 이상** + 작성자와 **최소 1라운드 응답/수정**을 스레드에 남긴다. 예: PR#1 에서 팀원2가 `slugify` 의 유니코드 처리 누락을 지적 → 팀원1이 커밋으로 반영 → 본인 PR 리뷰 반영 1회 충족.

**PR 본문 필수(subject §4.6)**: What(무엇을) / Why(왜) / How(검증 방법) + 연결 이슈에 `Closes #N`.

---

## 9. 완료 정의 (Definition of Done) / 제출 체크리스트

- Org 레포 생성 + `main` 보호 규칙(직접 push 금지·PR 머지·승인 1 필수) 적용 (§Phase 0)
- `docs/CONTRIBUTING.md` 5개 항목(브랜치/커밋/PR/리뷰/충돌 흐름) 모두 포함
- 모든 작업이 이슈 → `feature/`* → PR 경유로 머지, PR 본문에 `Closes #N`
- 멤버별 머지 PR 2 / 작성 리뷰 2 / 본인 PR 리뷰 반영 1회 충족 (§8 매트릭스)
- 충돌 해결 기록 2건 이상, 비자명 충돌 1건 이상 → `docs/conflict-resolution.md` (§6)
- 트러블슈팅 4종 모두 기록, 멤버별 최소 1건 작성 → `docs/troubleshooting-log.md` (§7)
- Simple Outcome (A) 유틸 함수 모음: 멤버별 함수 1개 이상 + 사용 예시, 멤버별 기여 커밋 1개 이상
- `git log --oneline --graph --all` 증거 캡처
- `SUBMISSION.md` 에 멤버별 PR/이슈/리뷰/충돌·트러블슈팅 링크 정리

---

## 10. (선택) 보너스 (subject §5)

- 개인 `feature` 브랜치에서 `git rebase -i` 로 커밋 squash/reword 후 before/after 히스토리 기록.
- `.github/CODEOWNERS` 로 `src/utils/*` 파일별 책임 리뷰어 자동 지정.

> 보너스는 본 미션의 §9 체크리스트를 모두 충족한 뒤 별도 브랜치로 진행한다.

