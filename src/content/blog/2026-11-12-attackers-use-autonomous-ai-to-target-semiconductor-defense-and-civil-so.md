---
title: "Attackers Use Autonomous AI to Target Semiconductor, Defense and Civil Society Sectors"
description: "Autonomous AI attacks signal a critical escalation in threat capabilities."
publishDate: "2026-11-12"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-11-12-attackers-use-autonomous-ai-to-target-semiconductor-defense-and-civil-so.png"
img_alt: "Editorial hero image for Attackers Use Autonomous AI to Target Semiconductor, Defense and Civil Society Sectors"
---
A recent report from Palo Alto Networks' Unit 42 details a campaign where attackers used an open-source AI framework to automate intrusions. This isn't a theoretical exercise; the report documents 25 operations against 19 organizations in the semiconductor, defense, and civil society sectors between August and September 2026.

The attackers used a publicly available penetration testing framework called Cairn, hooking it up to Chinese AI models Zhipu GLM and DeepSeek. They gave the system a target domain and a high-level goal—like "obtain substantive high-value access"—and let the AI agent get to work. According to Unit 42, this resulted in confirmed breaches at 10 of the targeted organizations.

### How the Autonomous Attacks Worked

The Cairn framework operates using AI "agent workers" that coordinate through a shared "blackboard." An agent reads the current state, decides on an action, executes it, and writes the result back to the blackboard for the next cycle. The process loops through two phases: `Reason` (reviewing findings and planning the next step) and `Explore` (executing a single action).

The attackers ran a custom fork of Cairn from a server in Hong Kong. For each target, they provided a simple goal in Chinese. The AI agent then generated its own multi-stage attack plan, moving from reconnaissance to exploitation, privilege escalation, and lateral movement. The report notes these operations ran autonomously for anywhere from 20 minutes to over 50 hours.

Human operators could inject "hints" to guide the agent, and in one case, they supplied VPN credentials and group passwords, suggesting the AI-driven attacks were layered on top of prior intelligence gathering.

### Not Novel Exploits, Just Faster and More of Them

Here’s the most important part for defenders: the AI didn't invent novel zero-days. It succeeded by exploiting a familiar list of common security weaknesses:
*   Weak and default credentials
*   Authentication bypasses
*   Insecure direct object references
*   Exposed cloud APIs
*   Known public CVEs

In one case, the agent brute-forced a password on a partner application, created admin accounts, and exfiltrated user lists. In another, it used an unauthenticated account creation bug to harvest over a million member records from a teachers' union.

The novelty isn't the *what*, but the *how*. The report attributes the campaign to a China-nexus actor, CL-STA-1238. By using an autonomous framework, a small team could run nearly two dozen simultaneous intrusion attempts. The bottleneck is no longer the number of available human operators, but the number of targets with basic security hygiene gaps.

### Bypassing Guardrails with a Text File

The attackers also demonstrated how easily current model safety features can be bypassed. Cairn’s default prompts already instruct the model not to refuse tasks. The attackers reinforced this by adding a Chinese-language preamble to the system prompt for every API call, asserting the task was part of an authorized security test.

They also had the framework generate an `AUTHORIZATION.md` file for each operation, declaring the engagement was approved. According to Unit 42, neither Zhipu GLM nor DeepSeek refused this pretext.

This campaign offers a concrete example of AI-driven offense in the wild. The tools were a combination of open-source frameworks and commercial model APIs. The exploits were mundane. The success came from automating the discovery and exploitation of these known flaws at scale. The question for builders and defenders is no longer *if* an attacker will find your exposed API or weak password, but how quickly an automated agent will.

---

Source: [Attackers Use Autonomous AI to Target Semiconductor, Defense and Civil Society Sectors](https://unit42.paloaltonetworks.com/cairn-framework-ai-autonomous-attacks/)
