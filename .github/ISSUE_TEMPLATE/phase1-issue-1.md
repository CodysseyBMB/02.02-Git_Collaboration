---
title: "feat: implement text_utils (slugify, truncate)"
labels: enhancement
---

## 목표

`text_utils` 모듈에 `slugify`, `truncate` 함수를 구현하고 패키지 재노출 및 README 인덱스를 갱신한다.

## 구현 범위

- `src/utils/text_utils.py` — `slugify`, `truncate`
- `src/utils/__init__.py` — import 및 `__all__` 재노출
- `README.md` — 함수 인덱스 2행 추가

## Phase 1 조율

- 브랜치: `feature/1-text-utils`
- **PR#1은 PR#2·PR#3보다 먼저 Squash merge** (충돌 시나리오 A 전제)
- 상세: [`docs/phase1-coordination.md`](../docs/phase1-coordination.md)
