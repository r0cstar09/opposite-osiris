---
title: "Hermes Relay — Automated Cybersecurity Briefing Pipeline"
publishDate: 2026-05-23
img: /assets/hermes-relay/hermes-relay-hero.png
img_alt: "Cyber-style hero art for automated daily cybersecurity intelligence briefings"
description: |
  A Python pipeline that ingests cybersecurity RSS feeds, deduplicates stories, scores the top
  items with Vertex AI Gemini, and delivers an executive-ready HTML briefing — scheduled daily
  via GitHub Actions with optional email delivery.
tags:
  - Python
  - Vertex AI
  - GitHub Actions
  - Threat Intelligence
  - Automation
  - RSS
---

## Introduction

**Hermes Relay** curates high-impact cybersecurity news and turns it into a **daily executive-ready briefing**. It pulls from trusted industry RSS feeds, filters out stories you have already seen, uses **Google Vertex AI Gemini** to score and summarize the top items, then writes structured **JSON + HTML** outputs — with optional email delivery through iCloud SMTP.

Repository: [github.com/r0cstar09/hermes-relay](https://github.com/r0cstar09/hermes-relay)

---

## Problem

Security teams and leaders are flooded with headlines. Manually scanning nine-plus feeds, picking what matters, writing board-level context, and formatting a briefing for email or LinkedIn does not scale — and it is easy to skip on busy days. Hermes Relay automates the **collect → dedupe → rank → summarize → deliver** loop so the briefing shows up consistently.

---

## What it does

Each run follows a two-stage pipeline orchestrated by `orchestrator.py`:

1. **`hermes-relay.py`** — Fetches RSS entries from sources including Krebs on Security, BleepingComputer, Mandiant, Microsoft Security, Google TAG, Unit 42, CISA alerts/advisories, and Dark Reading. Hashes title + link to **deduplicate** against prior `hermes_signal_*.json` files, then saves today's new articles to `hermes_signal_YYYY-MM-DD.json`.

2. **`llm_score_and_summarize.py`** — Loads today's new articles, applies a rotating **"lens of the day"** (e.g. first-24-hours response, supply-chain risk, explain to non-security leadership), and calls **Vertex Gemini** to score stories and produce:
   - Key takeaways and board-level impact notes
   - LinkedIn-ready copy blocks
   - Ranked top stories saved to `json_output/YYYY-MM-DD/hermes_llm_top3_*.json`
   - A styled HTML briefing at `hermes_briefing_*.html`
   - Optional SMTP email if credentials are configured

**GitHub Actions** runs the same pipeline on a daily cron (and manual dispatch), authenticates to GCP via a service account secret, and uploads JSON/HTML artifacts for 30 days.

---

## How the project is structured

```text
hermes-relay/
├── hermes-relay.py              # RSS ingest + dedupe → hermes_signal_*.json
├── llm_score_and_summarize.py     # Vertex Gemini scoring + HTML/email
├── orchestrator.py                # validates env, runs both scripts
├── hermes_signal_YYYY-MM-DD.json
├── json_output/YYYY-MM-DD/
│   ├── hermes_llm_top3_*.json
│   └── hermes_briefing_*.html
├── .github/workflows/hermes-relay.yml
└── requirements.txt
```

![Repository layout](/assets/hermes-relay/hermes-relay-01-structure.png)

- **Ingest layer** — Feed list, parsing, and hash-based dedupe so only new stories enter the LLM step.
- **Intelligence layer** — Prompt engineering with daily lenses and per-article angle selection; Gemini returns scored summaries tuned for executives and practitioners.
- **Delivery layer** — HTML briefing template with article cards, scores, board notes, and copy-paste LinkedIn blocks; email is optional.
- **Automation layer** — Workflow validates GCP secrets, runs `orchestrator.py`, uploads artifacts.

![GitHub Actions workflow](/assets/hermes-relay/hermes-relay-02-workflow.png)

---

## What the briefing looks like

The HTML output is designed like a morning intelligence email: briefing title, date, ranked articles with **scores out of 10**, bullet takeaways, yellow **board-level impact** sections, and blue **LinkedIn-ready** copy blocks.

![Sample daily cybersecurity briefing HTML output](/assets/hermes-relay/hermes-relay-briefing-preview.png)

Each story links back to the original source. The lens rotates by calendar day so summaries emphasize different executive angles over time — compliance one day, concrete detections the next, threat-landscape framing another.

---

## Stack

| Layer | Technology |
|-------|------------|
| Ingest | Python, `feedparser`, SHA-256 dedupe |
| LLM | Google Vertex AI Gemini (`gemini-2.5-flash` default) |
| Orchestration | `orchestrator.py`, GitHub Actions cron + `workflow_dispatch` |
| Output | JSON artifacts + styled HTML briefing |
| Email (optional) | iCloud SMTP |

---

## Outcomes

- **Consistent daily briefings** without manual feed triage
- **Deduped ingest** so repeat headlines do not re-enter the pipeline
- **Executive-ready formatting** — board notes and social copy included
- **Scheduled automation** with artifact retention in CI
- **Secrets isolated** — GCP and SMTP credentials stay in GitHub Secrets / local `.env`, not in the repo

---

## Repository

Full source and workflow: [github.com/r0cstar09/hermes-relay](https://github.com/r0cstar09/hermes-relay)
