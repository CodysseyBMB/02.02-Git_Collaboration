# Git Workflow — 유틸 함수 모음

3인 팀이 **GitHub Flow**와 PR 기반 협업을 연습하기 위한 Python 유틸 모음 프로젝트입니다.  
과제 명세: [`docs/subject_korean.md`](docs/subject_korean.md) · 실행 계획: [`docs/plan.md`](docs/plan.md)

## GitHub Flow를 선택한 이유

1. `main`이 항상 배포 가능(머지 가능) 상태를 유지하기 쉽다.
2. `feature/` 브랜치 단위로 이슈·PR·코드 리뷰가 자연스럽게 연결된다.
3. 소규모 팀·짧은 주기 협업에 Git Flow 대비 오버헤드가 적다.

## 실행 방법

```bash
# Phase 1 이후 함수 구현이 완료되면
python -c "from src.utils import slugify; print(slugify('Hello World'))"
```

## 함수 인덱스

> Phase 1 이후 멤버별 PR 머지에 맞춰 채웁니다.

| 모듈 | 함수 | 작성자 | 설명 |
| ---- | ---- | ------ | ---- |
| `string_utils` | `slugify` | 팀원1 | 소문자·공백→하이픈 |
| `string_utils` | `truncate` | 팀원1 | 최대 길이 초과 시 `...` |
| `date_utils` | `days_between`, `to_iso` | 팀원2 | 날짜 간 일수 계산, ISO 날짜 문자열 변환 |
| `number_utils` | `format_currency`, `clamp` | 팀원3 | 통화 포맷·범위 제한 |

## 문서

| 문서 | 설명 |
| ---- | ---- |
| [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md) | 브랜치·커밋·PR·리뷰·충돌 협업 규칙 |
| [`docs/conflict-resolution.md`](docs/conflict-resolution.md) | 충돌 해결 기록 |
| [`docs/troubleshooting-log.md`](docs/troubleshooting-log.md) | Git 복구 4종 실습 기록 |
| [`SUBMISSION.md`](SUBMISSION.md) | 제출 인덱스 (멤버별 PR·증거 링크) |
