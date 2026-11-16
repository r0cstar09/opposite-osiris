---
title: "Google warns that fully-automated AI attacks are coming soon"
description: "Prepare for machine-speed AI attacks with enhanced detection and response capabilities."
publishDate: "2026-11-16"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-11-16-google-warns-that-fully-automated-ai-attacks-are-coming-soon.png"
img_alt: "Editorial hero image for Google warns that fully-automated AI attacks are coming soon"
---
Google's Threat Intelligence Group is marking a shift from attackers *using* AI to attackers *automating* with AI. In a recent report, they detail the move from human-in-the-loop social engineering or code generation to agentic workflows that automate vulnerability discovery and exploitation.

According to Google, this isn't a future prediction. They've already seen threat actors, including state-sponsored groups, adopt open-source offensive AI frameworks like CAIRN and ARTEX. The report projects that "little to no human interaction" attacks are just months away.

### A Look at an `exploit_agent`

The most concrete evidence comes from an exposed staging server that Google found. It hosted a multi-agent framework the attackers called `exploit_agent`. This system wasn't just a script; it was a full-fledged vulnerability research and weaponization pipeline that integrated with multiple LLMs.

Its job was to analyze software updates for signs of security flaws and then automatically attempt to exploit them. The server also contained stolen victim data, webshells, and brute-forcing scripts, showing this wasn't a theoretical exercise. For now, Google notes these automated attacks target "low-complexity flaws for which large language models (LLMs) could easily build exploits." Speed and scale are the advantage here, not finding a novel zero-day.

### The Coming Flood of Fake Exploits

One of the more interesting side effects Google observed is the impact on defender signal-to-noise ratio. The report highlights the recent PHP2Shell vulnerabilities, where hundreds of purported proof-of-concept (PoC) exploits—most of them AI-generated—appeared almost immediately after the announcement.

This creates a new kind of denial-of-service attack on security teams. Every PoC, no matter how flimsy, requires some level of verification. When attackers can generate a hundred plausible-looking but non-functional exploits in minutes, it makes finding the one that actually works that much harder. The automation isn't just accelerating exploitation; it's also accelerating the creation of false leads.

The immediate challenge isn't necessarily defending against a fully autonomous AI hacker. It's learning how to operate when the time between a patch announcement and a functional, automated exploit shrinks to hours, and every real exploit is hidden in a flood of AI-generated noise. How do you build a triage system that can tell the difference?

---
Source: [Google warns that fully-automated AI attacks are coming soon](https://www.bleepingcomputer.com/news/security/google-warns-that-fully-automated-ai-attacks-are-coming-soon/)
