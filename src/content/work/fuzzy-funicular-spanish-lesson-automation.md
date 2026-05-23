---
title: "fuzzy-funicular — Spanish Lesson Delivery Automation"
publishDate: 2026-05-23
img: /assets/fuzzy-funicular/fuzzy-funicular-hero.png
img_alt: "Cyber-style hero art blending Spanish language motifs with automated lesson delivery"
description: |
  Automated daily Spanish writing drills delivered by email — structured exercises that build
  sentence patterns, tense choice, and productive output through cognitive framing, controlled
  practice, contrast sets, and answer keys.
tags:
  - Python
  - GitHub Actions
  - Spanish Learning
  - Writing Drills
  - Workflow Automation
---

## Introduction

**fuzzy-funicular** sends structured Spanish **writing practice** to your inbox on a steady schedule. Each lesson targets one grammar pattern (ser + cognates, pronominal verbs, preterite vs imperfect, and more) and follows the same eight-part drill sequence every time — so you always know what to study, and you are producing Spanish in full sentences instead of only reading rules.

Repository: [github.com/r0cstar09/fuzzy-funicular](https://github.com/r0cstar09/fuzzy-funicular)

---

## Why this helps you learn Spanish

Most apps optimize for recognition. These lessons optimize for **production** — writing real sentences under light time pressure:

- **Daily output.** English prompts, Spanish answers. Active recall, not passive review.
- **One pattern per lesson.** Repeat a single structure until it feels automatic.
- **English traps first.** Each lesson names what English speakers get wrong, then the Spanish logic to use instead.
- **Automatic spacing.** Lessons arrive on a schedule you control (daily, every other day, etc.).
- **Answers at the end.** Drills run without the key visible so you can self-check honestly.

If you have studied Spanish before but still freeze when writing, the flow is: **pattern → examples → short writes → contrast → personal sentences → common errors → answer key**.

---

## What each exercise section trains

| Section | What you practice | What gets better |
|--------|-------------------|------------------|
| **Cognitive shift** | English trap vs Spanish logic, formula, examples | Choosing structures by meaning, not word-for-word translation |
| **Controlled recombination** | English prompts → Spanish with the target pattern | Speed producing the pattern in new contexts |
| **Pattern mutation** | Transform given Spanish sentences | Flexibility — you own the pattern, not one frozen template |
| **Contrastive discrimination** | Pick the best option between near-miss pairs | Fine distinctions (preterite vs imperfect, reflexive vs not, etc.) |
| **Guided personal writing** | Short prompts about your life | Transfer to things you actually say |
| **Reverse conceptual expression** | Explain the concept from Spanish cues | Deeper understanding of *why* a form fits |
| **Common errors** | Typical mistakes and corrections | Catch habits before they stick |
| **Answer key** | Full solutions | Honest self-correction without a tutor for every line |

---

## How the project is structured

The repo keeps **content**, **delivery code**, and **scheduling** separate so lessons and automation can change independently.

```text
fuzzy-funicular/
├── lessons/lesson-N/
│   ├── *.pdf              # source PDFs (reference)
│   ├── lesson.json        # schema-driven lesson (email source of truth)
│   └── lesson.md          # human-readable mirror
├── scripts/send_daily_lesson.py
├── .github/workflows/send-daily-lesson.yml
├── requirements.txt
└── README.md
```

- **`lessons/`** — 63 folders with `lesson.json` today (lessons 1–64; lesson 11 still being normalized). PDFs stay for editing; JSON drives rendering.
- **`scripts/send_daily_lesson.py`** — Discovers lessons, validates schema, selects by date/cadence, renders Markdown → HTML, sends via SMTP. Supports `--validate-all` and `--dry-run`.
- **`.github/workflows/`** — Cron + manual dispatch. Validates every lesson before send. Cadence via env vars; credentials in GitHub Secrets only.

![Repository layout](/assets/fuzzy-funicular/fuzzy-funicular-01-structure.png)

---

## What the emails look like

Each message uses a styled HTML template: gray outer shell, white card, **blue gradient header** (“Spanish Writing Trainer”, lesson title, pattern ID), then numbered sections with blue left borders. Cropped previews below (800×450) show the header and opening framing — not the full scroll-length email.

**Lesson 1 — cognates and *ser* frames (A1–A2)**

![Lesson 1 email preview with gradient header and pattern framing](/assets/fuzzy-funicular/fuzzy-funicular-email-lesson-01.png)

**Lesson 25 — pronominal verbs (A2–B1)**

![Lesson 25 email preview with gradient header and pronominal verb framing](/assets/fuzzy-funicular/fuzzy-funicular-email-lesson-25.png)

**Lesson 40 — preterite vs imperfect (A2–B1)**

![Lesson 40 email preview with gradient header and past-tense framing](/assets/fuzzy-funicular/fuzzy-funicular-email-lesson-40.png)

---

## How delivery works

On each run, GitHub Actions installs dependencies, runs `--validate-all`, then sends the lesson chosen by date and cadence (or a manual lesson number). Rendering turns JSON into Markdown, then into the HTML template above.

![GitHub Actions workflow](/assets/fuzzy-funicular/fuzzy-funicular-02-workflow.png)

The pipeline exists so practice does not depend on willpower: the lesson arrives, you write for twenty to forty minutes, then you check the key.

---

## Outcomes

- Consistent writing habit through scheduled email delivery
- 63 structured lessons from foundational frames through intermediate grammar
- Repeatable drill design with a clear start, middle, and self-check
- Configurable pacing (start date, starting lesson, every-N-days cadence)

---

## Stack

Python 3.11 · JSON lesson schema · Markdown → HTML · GitHub Actions · iCloud SMTP

Full source: [github.com/r0cstar09/fuzzy-funicular](https://github.com/r0cstar09/fuzzy-funicular)
