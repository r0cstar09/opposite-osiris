---
title: "GitHub Octoverse 2026"
description: "Agentic engineering drives exponential code output, fundamentally shifting development scale."
publishDate: "2026-10-29"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-10-29-github-octoverse-2026.svg"
img_alt: "Editorial cyber defense illustration for GitHub Octoverse 2026"
---
GitHub's 2026 Octoverse report is out, and the numbers show a fundamental shift in development scale, driven by what they're calling "agentic engineering." According to GitHub, merged pull requests have tripled in less than a year to 220 million per month. Monthly commits are up more than 3x to 7.38 billion.

These aren't just bigger numbers; they represent a phase change in how code is produced. This isn't about developers typing faster. It's about a massive increase in automated code generation, and it forces a new conversation about our tools and review processes.

### A New Baseline for Code Volume

The growth metrics from the report, shared via Simon Willison's blog on October 28, 2026, are stark. The tripling of PRs and commits, along with a doubling of new repositories to 30.3 million per month, suggests that AI agents are now a primary author of code, not just an assistant.

This isn't an incremental increase. An engineering team that was built to handle 10 pull requests a day now has to process 30. A security team whose scanners were already running constantly now has three times the code to analyze. The operational reality is that human-centric review processes cannot scale at the same rate.

### Using LLMs to Measure LLM Impact

An interesting detail in the report's methodology is GitHub's own use of AI. They used a fine-tuned LLM to classify repositories by industry based on names, descriptions, and READMEs. They also used LLM classification to clean up user location data, adjusting for VPN usage.

This is a good example of the "turtles all the way down" nature of this technology. We're now using AI to measure the impact of AI, which is a necessary step when the scale of data exceeds human analytical capacity. It also hints at the kind of tooling we'll need to build ourselves: systems that can intelligently classify, triage, and analyze codebases too large to read.

### What Does "Code Review" Mean Now?

The core question these numbers raise for any defender or builder is what "review" even means at this scale. When a pull request is 95% agent-generated, is a human line-by-line review the right approach? Is it even possible?

Our security tooling was built for a world of human-authored code and its corresponding error patterns. The challenge isn't just scanning more code for the same old injection flaws. The real work is figuring out what new, systemic failure modes emerge from agent-authored code. Are we looking for subtle logic flaws, incorrect assumptions baked into the training data, or just a higher volume of mundane bugs?

The practical experiment for any team is to measure the ratio of agent-generated code to human-authored code in your own projects. What is that ratio today, and what was it six months ago? More importantly, what's your ratio of human review time to total lines of code committed? If one is growing exponentially and the other is static, something has to give.

---
Source: [GitHub Octoverse 2026](https://simonwillison.net/2026/Oct/28/github-octoverse-2026/)
