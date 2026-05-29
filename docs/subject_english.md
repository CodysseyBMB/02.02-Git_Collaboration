# Git Workflow Mission

---

## 1. Mission Overview

Git is not just a version control tool—it is **core infrastructure for team collaboration**. No matter how well you code, if you cannot use Git properly, you become a bottleneck on team projects.

In this mission, you simulate real collaboration in a **team of 3–5 people**. You experience conflicts by editing the same files at the same time, exchange code reviews through **PRs**, and apply a **branching strategy**. The goal is not to memorize commands, but to internalize *why this workflow exists* together with your teammates.

The experience from this mission applies directly in industry. In particular, **PR-based collaboration** and a **code review culture** are among the most important soft skills in professional work.

---

## 2. Final Deliverables

Complete **one team GitHub repository** that includes the following deliverables.

### 2.1 Repository & Submission Index

| Item | Description |
|------|-------------|
| **GitHub repository URL** | Team repository address |
| **`SUBMISSION.md`** | A **submission index** that gathers PR links, document links, and evidence links per team member in one place |

### 2.2 Collaboration Documents (3 required)

| Document | Role |
|----------|------|
| `docs/CONTRIBUTING.md` | Collaboration rules: branches, commits, PRs, reviews, conflict handling, etc. |
| `docs/conflict-resolution.md` | Record of conflict resolution process |
| `docs/troubleshooting-log.md` | Git troubleshooting records (4 scenarios) |

### 2.3 Git History Evidence (choose 1)

- **Text** or **screenshot** of `git log --oneline --graph --all` output

### 2.4 “Simple Outcome” (choose 1 from below)

| Option | Content |
|--------|---------|
| **Utility function collection** | Per-member utility functions (any language, e.g. Python) |
| **Team introduction** | `README` + `team/` folder |
| **Learning summary notes** | Per-member markdown notes |

---

## 3. Learning Objectives

After completing this assignment, learners should be able to explain the following on their own.

1. How **branches** work internally (pointers to commits), and **why work is split across branches**.
2. What **GitHub Flow** is, and why teams need this kind of strategy.
3. The purpose of **PRs (Pull Requests)** and the value of **code review**.
4. Why **conflicts** occur, and what conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) mean.
5. The differences among **`reset`**, **`revert`**, and **`stash`**, and when to use each.
6. When problems arise during team collaboration (conflicts, mistaken commits, etc.), **leave a record** and explain the resolution process in a reproducible way.

---

## 4. Functional Requirements

You must satisfy **all** of the following requirements.

### 4.1 Team Setup & Repository Preparation

| Item | Requirement |
|------|-------------|
| **Team size** | **3–5 people** |
| **Repository** | **Option A** or **B** below |

| Option | Description |
|--------|-------------|
| **A (recommended)** | Create a GitHub **Organization** repository |
| **B (alternative)** | Create a personal repository and invite **Collaborators** |

**Default folder & file structure**

| Path | Purpose |
|------|---------|
| `README.md` | Project intro, how to run, etc. |
| `docs/` | Documentation |
| `src/` | Code or example files |
| `team/` | Per-member intro docs (if chosen) |

### 4.2 Branch Protection Rule (`main`)

Configure the following on the **`main` branch**.

| Rule | Requirement |
|------|-------------|
| **Direct push** | Disallowed |
| **Merge** | Allowed **only via PR** |
| **Approval** | At least **1 approve** required |

### 4.3 Branching Strategy (GitHub Flow)

| Branch | Role |
|--------|------|
| **`main`** | Always in a deployable state (“does not break” by team standards) |
| **`feature/*`** | Work-unit branches |

| Item | Requirement |
|------|-------------|
| **Naming** | Define rules and document them in `docs/CONTRIBUTING.md` |
| **Rationale** | Record **within 3 lines** why you chose GitHub Flow in `README.md` or `docs/CONTRIBUTING.md` |

### 4.4 Issue-Based Work & PR Linking (required)

| Item | Requirement |
|------|-------------|
| **Issues** | Create each task as an **Issue** and link it to a PR |
| **PR body** | Include `Closes #issue-number` or `Fixes #...` for traceability |
| **`SUBMISSION.md`** | Quickly verify each member’s “Issues/PRs I created” |

### 4.5 Commit Message Convention

| Item | Requirement |
|------|-------------|
| **Documentation** | State team rules in `docs/CONTRIBUTING.md` |
| **Recommended format (example)** | `feat: subject`, `fix: subject`, `docs: subject`, `refactor: subject`, etc. |

**Counted as a “meaningless message” (if any of the following applies)**

| Type | Examples |
|------|----------|
| Words that do not imply what changed | `update`, `fix`, `temp`, `wip`, `final`, etc. |
| Does not show what/why changed | `bug fix`, `edit file`, etc. (no specific target or effect) |

### 4.6 PR-Based Collaboration (per-member contribution)

| Item | Requirement |
|------|-------------|
| **Merge path** | All `feature` branches merge into `main` **via PR** |

**Minimum per member (everyone must meet)**

| Criterion | Minimum count |
|-----------|---------------|
| PR created and merged | **2** |
| Code reviews written (excluding own PRs) | **2** |
| Addressing review feedback | **At least once** on own PR (evidenced by commit, edit, or reply) |

**Minimum PR body content (format flexible)**

| Item | Content |
|------|---------|
| **What** | What changed |
| **Why** | Why it changed |
| **How** | How to test/verify |

### 4.7 Minimum Code Review Quality

| Item | Requirement |
|------|-------------|
| **Comments** | At least **one substantive comment** (not only “LGTM/looks good”)—e.g. line/file-specific question, alternative, risk, improvement suggestion |
| **Interaction** | At least **one round** of reply or fix between reviewer and author, recorded in the thread |

### 4.8 Conflict Resolution Practice (including non-trivial conflicts)

| Scope | Requirement |
|-------|-------------|
| **Whole team** | **2+** conflict resolution records (commits, PRs, docs) |
| **Non-trivial conflict** | **At least 1** (one or more of the following) |

| Type | Description |
|------|-------------|
| **Same file, adjacent hunk** | Both sides modify the same hunk (adjacent lines) in the same file differently |
| **Rename vs content edit** | One side moves/renames (or deletes) a file; the other edits content (causes issues on merge/rebase) |

Record the conflict resolution process in **`docs/conflict-resolution.md`** (following the template is recommended).

### 4.9 Git Troubleshooting Practice (team: all 4 + member participation)

**The whole team performs all four scenarios below and documents them.**

| Scenario | Description |
|----------|-------------|
| `git commit --amend` | Edit the most recent commit message |
| `git reset --soft HEAD~1` | Undo local commit, keep changes |
| `git revert` | Undo a commit already pushed to remote |
| `git stash` / `git stash pop` | Stash work, switch branches, etc. |

| Item | Requirement |
|------|-------------|
| **Per member** | Each member participates in writing at least **one** scenario resolution record (name/role visible in the doc) |
| **Record location** | **`docs/troubleshooting-log.md`** |

### 4.10 Collaboration Guide (`docs/CONTRIBUTING.md`)

Written by the team with divided responsibilities. **Must include at minimum:**

| Item |
|------|
| Branch naming rules |
| Commit message convention |
| PR writing rules (what to put in the body) |
| Code review rules (including minimum review quality) |
| Default flow when conflicts occur (who / how / where to record) |

### 4.11 Simple Outcome (choose 1) + per-member minimum

Choose **one** of the following (complex feature implementation is not the goal).

| Choice | Content |
|--------|---------|
| **(A) Utility function collection** | At least **one function per member** + brief usage example (`README` or docstring) |
| **(B) Team introduction** | Per-member intro files under `team/` + links/list in `README` |
| **(C) Learning notes** | At least **one note per member** + table of contents in `README` |

| Item | Requirement |
|------|-------------|
| **Per member** | At least **one contributing commit** each toward the chosen outcome |

---

## 5. Bonus Tasks (optional)

| Item | Content |
|------|---------|
| **History cleanup** | Use `git rebase -i` to squash/reword commits on a personal `feature` branch. Document before/after history briefly |
| **CODEOWNERS & review automation** | Use `.github/CODEOWNERS` to assign responsible reviewers per file/folder |
