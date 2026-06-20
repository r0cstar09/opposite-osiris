---
title: "Spanish Active Timed Recall"
publishDate: "2026-06-20"
img: "/assets/spanish-active-recall/spanish-active-recall-hero.svg"
img_alt: "Stylized Spanish Active Timed Recall dashboard showing sentence sprints, review queues, and verb training"
description: |
  A custom Spanish learning web app built around active recall: sentence production under timer
  pressure, lesson-based misses, verb conjugation drills, and review loops that keep weak prompts
  visible until they are actually sealed.
tags:
  - Astro
  - FastAPI
  - Spanish Learning
  - Active Recall
  - FSRS
  - LLM Evaluation
---

## Overview

Spanish Active Timed Recall is a custom Spanish practice system built for production, not passive recognition. The app turns Spanish study into a set of timed recall loops: hear or read a prompt, produce the answer, get graded, and send misses back into review until the pattern is actually stable.

The goal is simple: make it harder to lie to yourself about fluency. If a sentence pattern, verb form, or listening prompt breaks under time pressure, it stays visible.

---

## What the app does

The site is organized around a few practical training modes:

- **Timed sentence recall.** Prompts require active Spanish production instead of multiple-choice recognition.
- **Lesson-based practice.** Sentence patterns are grouped into structured lessons so progress maps to concrete grammar and usage targets.
- **Review queues.** Missed sentence prompts and verb prompts flow into review instead of disappearing after a single session.
- **Verb training.** Full-grid conjugation work supports targeted practice across tense, person, and verb families.
- **LLM-assisted grading.** Answers are evaluated for meaning, grammar, and acceptable variation rather than exact string matching only.
- **Progress feedback.** The UI makes completion, misses, and review state obvious so the next action is clear.

---

## Why I built it

Most language apps are good at keeping users busy. They are not always good at exposing whether you can produce language when the answer is not already on the screen.

This project is designed around a different constraint: **output first**.

Instead of optimizing for streaks or recognition, the app focuses on the uncomfortable part of learning Spanish:

- recalling the structure without hints,
- producing the full sentence,
- choosing the right tense or pronoun under pressure,
- and revisiting missed prompts until the failure mode is gone.

---

## System design

The app is split between a fast static frontend and a local API/backend stack:

```text
Astro frontend
  └─ Spanish practice UI, lesson browser, review pages, verb trainer

FastAPI backend
  └─ grading, study state, misses, lesson progress, audio/shadowing support

Local data + review state
  └─ prompt attempts, resolved misses, lesson completion, verb prompt progress
```

The frontend is intentionally direct: English UI, Spanish practice content, clear progress state, and minimal friction between seeing a miss and practicing it again.

The backend owns the study state and grading behavior so the UI can remain focused on practice rather than business logic.

---

## Engineering details worth showing off

This is not just a static portfolio demo. It is a working personal learning system with real product constraints:

- **Schema-driven practice content** so sentence patterns and verb prompts can expand without rewriting UI flows.
- **Robust grading paths** that handle imperfect LLM output and fall back safely when model responses are malformed.
- **Monotonic completion logic** so already-passed prompts are not accidentally reopened by stale duplicate submissions.
- **Miss promotion workflows** so failed sentence lessons can be moved into active timed recall.
- **Tailnet-friendly deployment** so heavier backend work can run privately while the Astro interface stays fast and reachable.

---

## Outcome

The result is a Spanish app that behaves more like a training system than a content library. It tracks what breaks, keeps that material in front of the learner, and pushes practice toward the skill that matters most: producing Spanish without waiting for the app to hand you the answer.
