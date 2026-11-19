---
title: "How OpenAI’s Performance Factory keeps ChatGPT fast"
description: "AI agents autonomously optimize critical systems, requiring clear human oversight."
publishDate: "2026-11-19"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-11-19-how-openai-s-performance-factory-keeps-chatgpt-fast.png"
img_alt: "Editorial hero image for How OpenAI’s Performance Factory keeps ChatGPT fast"
---
OpenAI is using its own models for more than just powering chatbots. A recent post details their "Performance Factory," an internal system where AI agents act as autonomous performance engineers for the infrastructure running ChatGPT.

This isn't just about using an AI assistant to help a developer find a bug. OpenAI describes a closed-loop system that automatically detects performance regressions, investigates the root cause, proposes a code fix, and, after a human engineer's review, verifies that the deployed fix actually worked. It's a concrete example of an agentic workflow doing real, complex engineering work in production.

### From Manual Debugging to an Agent Factory

The post outlines a fascinating evolution that other engineering teams might recognize. The work started with manual investigations, which were slow and required deep system knowledge. Then, Codex became a "partner," allowing engineers to ask questions and get help debugging, but the human still had to steer the process.

The next step was capturing the investigation process itself into a reusable "skill" called `perf-forensics`. This skill taught the model which tools to use and how to diagnose a slowdown. Soon, engineers found themselves acting as simple proxies, copying an alert into a prompt and pasting the results back into Slack.

The final steps were to automate that proxy work. First, they moved investigations into a cloud service triggered by alerts. The final stage was building the "Performance Factory," a complete system that manages the entire lifecycle of a regression, handing off tasks between agents and humans. According to OpenAI, this system has handled over 1,700 investigations in just over three months.

### Agents Auditing Other Agents

One of the most interesting details is how they handle the unreliability of AI-generated analysis. Early on, they found that an agent might stop at the first plausible explanation it found, which was sometimes wrong.

To counter this, they implemented an adversarial review process. After one agent diagnoses a root cause, a second, separate agent is tasked with trying to disprove the diagnosis. This reviewer re-checks assumptions and tests counterfactuals. For example, if a code rollout is blamed for a slowdown, the reviewer checks if requests that *weren't* part of that rollout remained healthy.

This agent-on-agent audit is a clever, specific control. Rather than just relying on a human to catch every error, they've built a check-and-balance system into the automated workflow itself. They claim this adversarial step, combined with breaking work into smaller, focused tasks, improved the accuracy of their root-cause analysis significantly.

### The Hard Part is Still the Fix

OpenAI is candid that diagnosing a problem is easier than fixing it. The Performance Factory can generate a pull request with a proposed fix, but this is where the human handoff is critical. Engineers review the code, and the system is designed to make this review as efficient as possible with auto-generated summaries, charts, and flame graphs.

They note that agent-proposed fixes can be overly complex or introduce new issues. Architectural decisions, like adding a cache, still require an engineer who can weigh the trade-offs. The human review gate remains a hard requirement.

The "Performance Factory" provides a detailed look at what it takes to move from an AI assistant to a truly autonomous agent system. It’s less about a magical AI that solves problems and more about thoughtful system design: a task tracker, a dispatch loop, event subscriptions, and—most importantly—explicit checks and balances like adversarial review and mandatory human sign-off. The real lesson here isn't that an AI can find a performance bug, but what kind of scaffold you need to build to let it do that work safely and effectively in a production environment.

---

Source: [How OpenAI’s Performance Factory keeps ChatGPT fast](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast)
