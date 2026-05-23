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

**fuzzy-funicular** sends structured Spanish **writing practice** to your inbox on a steady schedule. Each lesson targets one grammar pattern (ser + cognates, pronominal verbs, preterite vs imperfect, and dozens more) and walks you through the same drill sequence every time — so you are not guessing what to study, and you are not only reading rules without producing Spanish.

Repository: [github.com/r0cstar09/fuzzy-funicular](https://github.com/r0cstar09/fuzzy-funicular)

---

## Why this helps you learn Spanish

Most apps optimize for recognition — tap the right word, finish the streak, move on. That does not reliably build **production**: writing your own sentences under time pressure. These lessons are built around output:

- **You write every day.** Prompts are in English; you respond in Spanish. That forces active recall, not passive review.
- **One pattern per lesson.** You repeat a single structure until it feels automatic (e.g. *Cuando era niño…* vs *Ayer llegué…*), instead of mixing ten topics and retaining none.
- **English traps are named first.** Each lesson opens with what English speakers get wrong and the Spanish logic that replaces it — so you fix mindset before drilling forms.
- **Spacing is automatic.** Lessons arrive on a schedule you configure (daily, every other day, etc.), which supports retention better than binge-studying once a week.
- **Answers stay separate.** Drills run without the key in view; the answer key is at the bottom so you can self-check honestly.

If you have studied Spanish before but still freeze when writing, this format targets that gap: **pattern → examples → many short writes → contrast → personal sentences → errors → key**.

---

## What each exercise section trains

Every lesson uses the same eight-part sequence. Together they move you from understanding *why* a pattern works to using it in your own context.

| Section | What you practice | What gets better |
|--------|-------------------|------------------|
| **1) Cognitive shift** | English trap vs Spanish logic, formula, natural examples | You stop translating literally and start choosing structures by meaning |
| **2) Controlled recombination** | English prompts → Spanish sentences with the target pattern | Speed and accuracy producing the pattern in new contexts |
| **3) Pattern mutation** | Transform given Spanish sentences (subject, time, polarity, etc.) | Flexibility — you own the pattern, not one frozen template |
| **4) Contrastive discrimination** | Pick the best Spanish option between near-miss pairs | Fine distinctions (preterite vs imperfect, reflexive vs non-reflexive, etc.) |
| **5) Guided personal writing** | Short prompts about your real life | Transfer to things you actually say — work, family, routines |
| **6) Reverse conceptual expression** | Spanish cues → English (or explain the concept) | Deeper understanding; you can explain *why* a form fits |
| **7) Common errors** | Typical mistakes, why they happen, corrections | You recognize your own habits before they fossilize |
| **8) Answer key** | Full solutions for written sections | Honest self-correction without needing a tutor for every line |

Early lessons (e.g. cognates with **ser**) build confidence and sentence frames. Mid lessons (e.g. **pronominal verbs**) separate reflexive, reciprocal, passive *se*, and meaning-change pairs. Later lessons (e.g. **preterite vs imperfect**) train narrative Spanish — background vs completed events — the split that blocks many intermediate writers.

---

## How the project is structured

The repo separates **reference material**, **machine-readable lessons**, **delivery logic**, and **scheduling** so content and automation can evolve independently.

```text
fuzzy-funicular/
├── lessons/lesson-N/          # one folder per lesson number
│   ├── *.pdf                  # source PDFs (reference only)
│   ├── lesson.json            # schema-driven lesson used by the sender
│   └── lesson.md              # human-readable mirror of the JSON
├── scripts/
│   └── send_daily_lesson.py   # discover, validate, select, render, send
├── .github/workflows/
│   └── send-daily-lesson.yml  # cron + manual dispatch, validate-all gate
├── requirements.txt
└── README.md
```

**`lessons/`** — Each numbered folder holds PDFs from the original curriculum plus a normalized `lesson.json`. The JSON is the source of truth for email rendering; PDFs stay for context when editing or auditing content. There are 63 lessons with JSON today (lessons 1–64, with lesson 11 still being normalized).

**`scripts/send_daily_lesson.py`** — Discovers all `lesson.json` files, validates the shared schema, picks the lesson for today (or a manual `--lesson-number`), renders Markdown then HTML, and sends via SMTP. Flags like `--validate-all` and `--dry-run` support CI and local preview without sending mail.

**`.github/workflows/`** — Runs on a daily cron and on manual trigger. Every run validates **all** lessons before send, reads cadence settings (`LESSON_START_DATE`, `LESSON_START_LESSON_NUMBER`, `LESSON_CADENCE_DAYS`), and uses repository secrets for SMTP credentials — nothing sensitive lives in the repo.

![Repository layout: lessons, scripts, and GitHub Actions workflow](/assets/fuzzy-funicular/fuzzy-funicular-01-structure.png)

---

## What the emails look like

Each message uses the same HTML template: a blue gradient header (“Spanish Writing Trainer”), lesson title, and pattern ID, then eight drill sections with blue accent bars. Previews below are cropped from the top of the real rendered email so you see the colors and layout—not plain text only.

**Lesson 1 — cognates and ser frames (A1–A2)**

<img src="/assets/fuzzy-funicular/fuzzy-funicular-email-lesson-01-top.png" alt="Lesson 1 email with gradient header and cognitive shift section" width="496" />
<img src="/assets/fuzzy-funicular/fuzzy-funicular-email-lesson-01-drills.png" alt="Lesson 1 email header plus writing drills with styled sections" width="496" />

**Lesson 25 — pronominal verbs (A2–B1)**

<img src="/assets/fuzzy-funicular/fuzzy-funicular-email-lesson-25-top.png" alt="Lesson 25 email with gradient header and pronominal verb framing" width="496" />

**Lesson 40 — preterite vs imperfect (A2–B1)**

<img src="/assets/fuzzy-funicular/fuzzy-funicular-email-lesson-40-top.png" alt="Lesson 40 email with gradient header and past-tense framing" width="496" />
<img src="/assets/fuzzy-funicular/fuzzy-funicular-email-lesson-40-drills.png" alt="Lesson 40 email header plus preterite and imperfect drills" width="496" />

---

## How delivery works

On each scheduled run, the workflow checks out the repo, installs Python dependencies, runs `--validate-all`, then sends the lesson selected by date and cadence (or a specific lesson when triggered manually). Rendering turns the JSON into Markdown, then into styled HTML suitable for email clients.

![GitHub Actions workflow with validation before send](/assets/fuzzy-funicular/fuzzy-funicular-02-workflow.png)

That pipeline exists so **practice does not depend on willpower** — the lesson shows up; you write for twenty to forty minutes; you check the key.

---

## Outcomes

- **Consistent writing habit** through scheduled email delivery
- **63 structured lessons** spanning foundational frames through intermediate grammar
- **Repeatable drill design** so each session has a clear start, middle, and self-check
- **Configurable pacing** (start date, starting lesson, every-N-days cadence) without rebuilding content

---

## Stack

Python 3.11, JSON lesson schema, Markdown → HTML rendering, GitHub Actions, iCloud SMTP.

Full source: [github.com/r0cstar09/fuzzy-funicular](https://github.com/r0cstar09/fuzzy-funicular)
