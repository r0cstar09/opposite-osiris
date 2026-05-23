---
title: "fuzzy-funicular — Spanish Lesson Delivery Automation"
publishDate: 2026-05-23
img: /assets/fuzzy-funicular/fuzzy-funicular-email-lesson-40-top.png
img_alt: "Rendered Spanish daily lesson email with pattern framing and writing drills"
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

The engineering side is simple: lessons live as JSON, a Python script renders them into email-friendly HTML, and GitHub Actions delivers them on a cron you control. The learning side is what matters: **daily output in full sentences**, with mistakes explained and answers at the end.

Repository: [github.com/r0cstar09/fuzzy-funicular](https://github.com/r0cstar09/fuzzy-funicular)

---

## Why this helps you learn Spanish

Most apps optimize for recognition — tap the right word, finish the streak, move on. That does not reliably build **production**: writing and speaking your own sentences under time pressure. These lessons are built around output:

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

## What the emails look like

Each message opens with the lesson title, pattern ID, and target grammar focus, then the cognitive framing and examples. Drill sections follow in the same order every time so you always know where you are in the workout.

**Lesson 1 — cognates and ser frames (A1–A2):** high-frequency *-al* cognates in natural Spanish sentences.

![Lesson 1 email — header, pattern focus, and cognitive shift](/assets/fuzzy-funicular/fuzzy-funicular-email-lesson-01-top.png)

![Lesson 1 email — controlled writing drills](/assets/fuzzy-funicular/fuzzy-funicular-email-lesson-01-drills.png)

**Lesson 25 — pronominal verbs (A2–B1):** choosing the right *se* function in context (reflexive, reciprocal, passive, chunks like *quejarse de*).

![Lesson 25 email — pronominal verb pattern and framing](/assets/fuzzy-funicular/fuzzy-funicular-email-lesson-25-top.png)

**Lesson 40 — preterite vs imperfect (A2–B1):** telling past stories with the correct tense for background vs completed events.

![Lesson 40 email — past narration pattern and examples](/assets/fuzzy-funicular/fuzzy-funicular-email-lesson-40-top.png)

![Lesson 40 email — preterite/imperfect writing drills](/assets/fuzzy-funicular/fuzzy-funicular-email-lesson-40-drills.png)

---

## How delivery works (brief)

Lessons are stored as `lesson.json` files (63 lessons today, numbered 1–64 with lesson 11 still being normalized). A GitHub Actions workflow validates every file, selects the lesson for the current date and cadence settings, renders Markdown to HTML, and sends via SMTP. You can also dry-run a lesson locally or trigger a specific lesson number manually.

![Scheduled workflow with validation before send](/assets/fuzzy-funicular/fuzzy-funicular-02-workflow.png)

That automation exists so **practice does not depend on willpower** — the lesson shows up; you write for twenty to forty minutes; you check the key.

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
