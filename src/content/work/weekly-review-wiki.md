---
title: "Weekly Review Wiki"
publishDate: "2026-06-18"
img: "/assets/weekly-review-wiki/weekly-review-wiki-hero.svg"
img_alt: "Stylized weekly review wiki pipeline with input, schema, and publish stages"
description: |
  A schema-gated Astro publishing system that turns weekly reviews into a durable personal wiki:
  structured frontmatter, consistent page design, and an archive that preserves decisions,
  reflections, and operating-system improvements over time.
tags:
  - Astro
  - Zod
  - Content Collections
  - Personal Knowledge Management
  - Automation
  - Static Publishing
---

## Overview

Weekly Review Wiki is a personal knowledge system for turning weekly reflections into a durable, browsable archive. Instead of leaving review notes scattered across chats, documents, or memory, the system publishes structured weekly pages with consistent metadata and layout.

The project treats personal reflection as content infrastructure: typed frontmatter, predictable sections, schema validation, and a frontend designed for reading back decisions later.

---

## Why it exists

Weekly reviews are only useful if the insights survive the week they were written in. The system is built to preserve:

- what went well,
- what created friction,
- what needs follow-up,
- what systems changed,
- and what decisions should not be rediscovered from scratch later.

The result is a personal operating-system changelog, not just a diary.

---

## Technical shape

```text
Review source material
  └─ weekly notes, summaries, themes, decisions

Schema layer
  └─ Astro content collections + Zod frontmatter validation

Publishing layer
  └─ static pages, archive routes, consistent visual design

Review loop
  └─ previous decisions inform next-week planning
```

The schema is the important part. It prevents the wiki from drifting into inconsistent one-off pages and makes each review easier to scan, compare, and reuse.

---

## Engineering details worth showing off

- **Schema-gated publishing** keeps review entries consistent and build-safe.
- **Astro content collections** provide typed content and fast static rendering.
- **Human-designed output** avoids the generic Markdown dump problem.
- **Archive-first structure** makes older reviews useful instead of buried.
- **Automation-friendly inputs** allow future summaries, reminders, or dashboards to be generated from the same structured source.

---

## Outcome

Weekly Review Wiki turns weekly reflection into durable infrastructure. It gives each review a stable home, enforces enough structure to stay useful, and creates a long-term archive of decisions, progress, and system improvements.
