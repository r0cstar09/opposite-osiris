---
title: "The Next AI Coding Leap Is Taste, Not Typing"
description: "Simon Willison’s sqlite-utils 4.0 release shows agents moving from autocomplete into release-quality engineering review."
publishDate: "2026-07-08"
tags: ["ai", "agents", "signal"]
---

## The shift

The interesting AI coding story this week is not another demo where a model spits out a toy app. It is Simon Willison shipping `sqlite-utils` 4.0 after using frontier coding agents as release reviewers.

The release itself is practical: database schema migrations are now part of `sqlite-utils`, alongside nested transactions through `db.atomic()` and support for compound foreign keys. Simon also published `sqlite-migrate` 0.2 as a compatibility shim that points the older package at the new built-in migration system. I verified both source pages were live before using them here.

The bigger signal is how the release got better. In Simon’s writeup, one model review produced a handful of scratch scripts and no major findings. Claude Fable 5, by contrast, wrote more test scripts, found release blockers, built a combined repro script, and helped drive fixes before the stable release.

That is the part builders should care about: the agent was not just generating code. It was attacking the release candidate like a stubborn maintainer with time, taste, and a checklist.

## Why it matters

A lot of teams still talk about AI coding as if the only metric is lines produced per hour. That is the wrong scoreboard. The expensive failures in real software are rarely caused by not typing fast enough. They come from missed edge cases, weak migration paths, accidental breaking changes, silent data loss, transaction bugs, bad defaults, and documentation that lies just enough to hurt users.

This `sqlite-utils` release is a cleaner example of where agentic engineering is headed. The useful loop was not “make me a feature.” It was closer to:

- compare the current branch against the last stable release
- exercise every new feature in throwaway scripts
- search for release blockers before the version promise hardens
- produce reproducible failures, not vibes
- help update docs and release notes after the behavior is verified

That is a materially different workflow from autocomplete. It turns the model into a parallel reviewer that can spend cheap attention on boring-but-dangerous paths humans tend to skip when they are tired.

## The operator angle

For operators, the lesson is not “trust the agent.” The lesson is “give the agent a harness that makes its work falsifiable.”

The pattern I like here is simple:

1. Give the model a real target: a release candidate, migration, API change, or production runbook.
2. Make it write executable scratch tests instead of just commenting on code.
3. Require repros for every serious claim.
4. Keep the human owner in the loop for taste, tradeoffs, and final judgment.
5. Preserve the artifacts long enough that another engineer can rerun the work.

That is how you get value without turning your codebase into an AI slop accumulator. The agent is not the maintainer. The agent is the tireless second pair of hands that can run down edge cases while the maintainer decides what actually belongs in the product.

Security teams should recognize this shape immediately. It looks like pre-release abuse-case testing. It looks like regression hunting. It looks like control validation. It looks like using cheap machine attention to find the weird state transition that breaks your assumptions.

## My read

The next jump in AI coding will be less about raw generation and more about taste under constraints.

Can the agent tell which bug matters before a stable release? Can it design an API that feels consistent with the rest of the library? Can it notice that a migration flag behaves dangerously only after a prior migration has already run? Can it produce a small repro instead of a dramatic paragraph?

Those are the capabilities that change engineering economics. Not because they remove humans, but because they let small teams run a release process that feels closer to having an extra senior engineer doing adversarial QA.

The danger is that companies will buy the coding-agent story and stop at code generation. That is the shallow win. The deeper win is building review harnesses, release checklists, synthetic workloads, rollback drills, and documentation verification into the agent loop.

In other words: stop asking the model to merely type. Ask it to prove the thing is ready.

## What I'm watching next

I am watching for agent workflows that become standard parts of serious software delivery:

- release-candidate review agents that compare behavior across versions
- migration test agents that generate dirty real-world database states
- security review agents that produce exploit-shaped repros without crossing into irresponsible publication
- documentation agents that verify examples against live code
- infrastructure agents that run rollback and failover drills before launch day

The teams that win will not be the ones with the flashiest prompt. They will be the ones that turn agents into repeatable engineering controls.

That is the real story in this release: not AI replacing a maintainer, but AI expanding what a careful maintainer can afford to check before shipping.

---

Sources:
- https://simonwillison.net/2026/Jul/7/sqlite-utils-4/#atom-everything
- https://simonwillison.net/2026/Jul/7/sqlite-migrate/#atom-everything
