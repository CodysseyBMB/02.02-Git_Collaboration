# Phase 0 — 리포·규칙 세팅

> Parent plan: [`docs/plan.md`](../plan.md) §5 Phase 0
> Subject reference: [`docs/subject.md`](../subject.md) §4.1, §4.2, §4.3, §4.10

이 단계는 **GitHub Organization 레포와 협업 규칙의 뼈대**를 만든다. 유틸 함수 구현은 Phase 1부터 시작하며, 여기서는 디렉터리 구조·문서 골격·브랜치 보호 규칙만 확정한다. 미션의 핵심은 코드가 아니라 **PR 기반 협업 흐름을 재현 가능하게 세팅**하는 것이다.

---

## 1. Goal

- GitHub **Organization 레포**를 생성하고 팀원(3명)을 초대한다.
- `main` 브랜치 보호 규칙(직접 push 금지 · PR 머지만 · 승인 1개 이상)을 적용한다.
- 초기 스캐폴딩 PR을 통해 디렉터리 구조·문서 뼈대·빈 `__init__.py` 골격을 `main`에 머지한다.
- README에 **GitHub Flow 선택 이유 3줄**을 기록한다.
- 보호 규칙이 실제로 동작함을 **PR 경유 머지**로 검증한다.

---

## 2. Scope (In / Out)

**In scope**
- Org 레포 생성 및 Collaborator 초대 (subject §4.1 안 A).
- `main` 브랜치 보호 규칙 설정 (subject §4.2).
- 디렉터리 트리 생성 (`plan.md` §3).
- `docs/CONTRIBUTING.md` 뼈대(5개 항목 헤더만).
- `docs/conflict-resolution.md`, `docs/troubleshooting-log.md` 빈 템플릿.
- `src/utils/__init__.py` 빈 골격.
- `SUBMISSION.md` 뼈대(멤버별 링크 테이블).
- README: 프로젝트 소개 + GitHub Flow 선택 이유 3줄.

**Out of scope**
- 유틸 함수 구현 (Phase 1).
- 충돌 발생·해결 (Phase 2–3).
- 트러블슈팅 실습 (Phase 4).
- 멤버별 PR/리뷰 할당 (Phase 1부터).

---

## 3. Tasks

### 3.1 GitHub Org·레포 생성 (팀원1)

- Organization 생성 → `02-2.git_workflow` 레포 생성.
- 팀원2·팀원3을 Collaborator로 초대.
- `main` 브랜치 보호 규칙:
  - 직접 push 금지
  - PR 머지만 허용
  - 승인 1개 이상 필수

### 3.2 이슈·브랜치

| 항목 | 값 |
| ---- | -- |
| 이슈 | `#0 chore: initial repo scaffolding` |
| 브랜치 | `feature/0-scaffold` |
| PR | **PR#0 (팀원1)** — 이후 번호는 Phase 1 PR#1부터 |

### 3.3 디렉터리 트리

```
02-2.git_workflow/
├── README.md
├── SUBMISSION.md
├── docs/
│   ├── subject.md
│   ├── plan.md
│   ├── plans/
│   ├── CONTRIBUTING.md
│   ├── conflict-resolution.md
│   └── troubleshooting-log.md
├── src/
│   └── utils/
│       ├── __init__.py
│       ├── text_utils.py       (빈 파일)
│       ├── date_utils.py       (빈 파일)
│       ├── collection_utils.py (빈 파일)
│       └── number_utils.py     (빈 파일)
└── tests/                      (선택, 빈 디렉터리)
```

### 3.4 `README.md`

- 프로젝트 한 줄 소개.
- **GitHub Flow 선택 이유 3줄** (subject §4.3):
  1. `main`이 항상 배포 가능 상태를 유지한다.
  2. feature 브랜치 단위로 PR·리뷰가 자연스럽게 연결된다.
  3. 소규모 팀·짧은 주기 협업에 오버헤드가 적다.
- 함수 인덱스 섹션 헤더만 (내용은 Phase 1 이후 채움).

### 3.5 `docs/CONTRIBUTING.md` 뼈대

다음 5개 섹션 헤더를 미리 만든다 (본문은 Phase 1 전후 보강):

1. 브랜치 네이밍 (`feature/<issue>-<summary>`)
2. 커밋 컨벤션 (Conventional Commits)
3. PR 본문 규칙 (What · Why · How + `Closes #N`)
4. 코드 리뷰 규칙 (구체 코멘트 1개 이상, LGTM 금지)
5. 충돌 발생 시 기본 흐름 (누가 · 어떻게 · 어디 기록)

### 3.6 PR·리뷰·머지

- PR 본문: What / Why / How + `Closes #0`.
- 리뷰어: 팀원2 (승인) + 팀원3 (코멘트).
- **Squash and merge**로 `main`에 머지.
- `main`에 직접 push 시도 → 거부되는지 확인 (보호 규칙 검증).

---

## 4. Files Touched

| File | Action |
| ---- | ------ |
| `README.md` | create (소개 + GitHub Flow 3줄 + 인덱스 헤더) |
| `SUBMISSION.md` | create (멤버별 링크 테이블 뼈대) |
| `docs/CONTRIBUTING.md` | create (5개 섹션 헤더) |
| `docs/conflict-resolution.md` | create (빈 템플릿) |
| `docs/troubleshooting-log.md` | create (4 시나리오 헤더) |
| `src/utils/__init__.py` | create (빈 골격) |
| `src/utils/text_utils.py` | create (빈 파일) |
| `src/utils/date_utils.py` | create (빈 파일) |
| `src/utils/collection_utils.py` | create (빈 파일) |
| `src/utils/number_utils.py` | create (빈 파일) |

---

## 5. Acceptance Criteria

- [ ] Org 레포 URL이 팀원 3명 모두 접근 가능하다.
- [ ] `main`에 직접 push가 거부된다.
- [ ] PR 없이 `main` 머지가 불가능하다.
- [ ] 승인 0개 PR은 머지 버튼이 비활성화된다.
- [ ] 스캐폴딩 PR이 Squash merge로 `main`에 반영되었다.
- [ ] README에 GitHub Flow 선택 이유 3줄이 있다.
- [ ] `docs/CONTRIBUTING.md`에 5개 항목 헤더가 있다.
- [ ] `src/utils/` 디렉터리와 빈 모듈 4개 + `__init__.py`가 존재한다.

---

## 6. Commit / PR

```
chore: scaffold repo structure and collaboration docs
```

PR 본문 예시:

```
## What
Org 레포 스캐폴딩 — 디렉터리 구조, 문서 뼈대, utils 모듈 골격.

## Why
Phase 1 병렬 작업 전에 공통 레이아웃과 협업 규칙의 기반을 확정하기 위해.

## How
- `tree` 로 디렉터리 구조 확인
- README GitHub Flow 3줄 존재 확인
- main 보호 규칙: 직접 push 거부 확인

Closes #0
```

---

## 7. Risks / Notes

- Org 생성 권한은 팀원1(리포 리드)에게만 있다. Phase 0 시작 전 Org 초대를 완료할 것.
- `__init__.py`와 README 함수 인덱스는 Phase 1에서 **모든 멤버가 동시 편집**하는 충돌 지점이다 — Phase 0에서는 비워 둔다.
- 스캐폴딩 PR도 보호 규칙 검증용이므로 셀프 머지하지 않고 다른 멤버 1명 승인을 받는다.

---

## 8. Definition of Done

- Org 레포 + `main` 보호 규칙 적용 완료.
- 스캐폴딩 PR 머지 완료, `main`에 디렉터리 트리 존재.
- Phase 1에서 세 명이 동시에 feature 브랜치를 팔 수 있는 상태.
