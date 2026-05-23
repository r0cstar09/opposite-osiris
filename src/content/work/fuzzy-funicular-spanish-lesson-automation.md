---
title: "fuzzy-funicular — Spanish Lesson Delivery Automation"
publishDate: 2026-05-23
img: /assets/fuzzy-funicular/fuzzy-funicular-hero.png
img_alt: "GitHub Actions workflow scheduling daily Spanish lesson email delivery"
description: |
  A Python and GitHub Actions pipeline that validates structured lesson JSON, selects lessons by
  date and cadence, renders Markdown/HTML email drills, and delivers daily Spanish writing practice
  through scheduled SMTP automation.
tags:
  - Python
  - GitHub Actions
  - Workflow Automation
  - Content Modeling
  - Education Systems
---

## Introduction

**fuzzy-funicular** is a lesson-delivery automation system I built to turn structured Spanish drill content into reliable, scheduled email practice. The problem was operational, not pedagogical: manual sends were easy to skip, hard to pace consistently, and risky to ship without validation. The solution is a small Python pipeline plus GitHub Actions that enforces schema checks, date-based lesson selection, and repeatable Markdown/HTML rendering before anything reaches a mailbox.

Repository: [github.com/r0cstar09/fuzzy-funicular](https://github.com/r0cstar09/fuzzy-funicular)

---

## Problem

Daily language practice only works when delivery is consistent. When lessons are prepared and sent by hand:

- cadence drifts after busy weeks or travel
- formatting quality varies lesson to lesson
- a broken lesson file can slip into production unnoticed
- pacing changes (every other day, restart mid-sequence) require manual recalculation

I needed a system that treats lessons like versioned data, validates them before send, and automates scheduling without exposing credentials in the repository.

---

## Solution

The project implements an end-to-end delivery loop:

1. **Normalize lessons** into `lesson.json` files with a fixed drill schema (cognitive framing, controlled drills, contrast sets, guided writing, answer keys).
2. **Validate all lessons** on every workflow run before attempting delivery.
3. **Select the correct lesson** from start date, starting lesson number, and configurable cadence (including non-daily schedules).
4. **Render learner-ready Markdown and HTML** from JSON, then send via iCloud SMTP using GitHub Actions secrets.

![Repository structure for lessons, scripts, and workflow automation](/assets/fuzzy-funicular/fuzzy-funicular-01-structure.png)

---

## Architecture and Workflow

```text
lesson PDFs (reference) → normalized lesson.json + lesson.md
        ↓
send_daily_lesson.py (--validate-all on CI)
        ↓
date/cadence selector → Markdown renderer → HTML email body
        ↓
GitHub Actions cron / manual dispatch → SMTP send
```

**Content layer:** each `lessons/lesson-N/` folder holds source PDFs plus normalized JSON used by automation. PDFs remain reference material; JSON drives rendering.

**Delivery layer:** `scripts/send_daily_lesson.py` discovers lessons, validates schema, selects by calendar rules, and renders email content.

**Automation layer:** `.github/workflows/send-daily-lesson.yml` runs on a daily cron schedule (and manual dispatch), installs dependencies, validates every lesson, then sends the selected lesson or a manually specified lesson number.

![GitHub Actions workflow with validation gate and scheduled send](/assets/fuzzy-funicular/fuzzy-funicular-02-workflow.png)

The workflow reads cadence configuration from environment variables (`LESSON_START_DATE`, `LESSON_START_LESSON_NUMBER`, `LESSON_CADENCE_DAYS`) so progression can pause or resume without rewriting selection logic. Secrets (`ICLOUD_EMAIL`, `ICLOUD_APP_PASSWORD`, `RECIPIENT_EMAIL`) stay in GitHub Actions — never committed to the repo.

![Lesson selection logic driven by start date and cadence](/assets/fuzzy-funicular/fuzzy-funicular-03-script-selection.png)

---

## Structured Lesson Model

Lessons are machine-checkable JSON, not ad hoc email copy. Each file includes metadata (`pattern_id`, `difficulty`, `target_pattern`) and eight drill sections:

- cognitive shift
- controlled recombination
- pattern mutation
- contrastive discrimination
- guided personal writing
- reverse conceptual expression
- common errors
- answer key

![Representative lesson JSON schema for drill-based Spanish practice](/assets/fuzzy-funicular/fuzzy-funicular-04-lesson-json.png)

This schema keeps content reusable: the same structure powers validation, rendering, and future tooling (indexing, search, or alternate channels) without rewriting lesson bodies.

---

## Validation and Dry-Run Safety

Before any send, the pipeline validates every `lesson.json` and fails fast on missing sections or malformed types. That prevents a single broken lesson from breaking production delivery.

![Validation output confirming lessons pass schema checks](/assets/fuzzy-funicular/fuzzy-funicular-05-validate-output.png)

A `--dry-run` mode renders the selected lesson to stdout so I can review Markdown output without sending email — useful when tuning copy or testing a specific lesson number.

![Dry-run preview of rendered lesson content](/assets/fuzzy-funicular/fuzzy-funicular-06-dryrun-preview.png)

---

## Stack

| Layer | Technology |
|-------|------------|
| Runtime | Python 3.11 |
| Orchestration | GitHub Actions (cron + `workflow_dispatch`) |
| Content format | JSON + Markdown |
| Rendering | Python Markdown → HTML email template |
| Delivery | SMTP (iCloud) via repository secrets |
| Scheduling | Cron + configurable cadence environment variables |

---

## Outcomes

- **Automated daily (or custom-cadence) delivery** with a validation gate on every run.
- **63 lesson folders** currently ship with paired `lesson.json` and `lesson.md` artifacts (lessons 1–64, with lesson 11 still pending JSON normalization).
- **Configurable pacing** via start date, start lesson number, cadence days, and optional no-wrap behavior when the sequence completes.
- **Separation of concerns** between reference PDFs and normalized JSON that powers automation — making content updates predictable and testable.

---

## Repository

Full source, workflow definition, and lesson corpus: [github.com/r0cstar09/fuzzy-funicular](https://github.com/r0cstar09/fuzzy-funicular)
