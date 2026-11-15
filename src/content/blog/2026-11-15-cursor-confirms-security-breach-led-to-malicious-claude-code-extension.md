---
title: "Cursor confirms security breach led to malicious Claude Code extension"
description: "AI tool supply chain attacks pose direct developer and code integrity risks."
publishDate: "2026-11-15"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-11-15-cursor-confirms-security-breach-led-to-malicious-claude-code-extension.png"
img_alt: "Editorial hero image for Cursor confirms security breach led to malicious Claude Code extension"
---
An attack on the AI-powered code editor Cursor shows how your development environment's supply chain now extends to the AI infrastructure providers behind the tools you use. The breach didn't come from a flaw in Cursor's own code, but from credentials stolen from Fireworks AI, a third-party service Cursor used for model training and inference.

### A Breach Through the AI Back End

According to Cursor's incident report from November 2026, attackers first obtained an access key stored on Fireworks AI's platform. With that key, they accessed a read-only storage bucket containing historical AI coding-agent traces.

This is the critical step. The compromised data wasn't just generic logs; it was conversation traces from users who had *not* enabled Cursor's "Privacy Mode." Some of those traces contained unredacted API credentials, which the attackers then used to pivot and access more of Cursor's internal systems. This is a direct consequence of data being collected for model training purposes.

With this deeper access, the attackers stole a credential that allowed them to publish extensions to Cursor's marketplace. On October 29, they pushed malicious versions of Anthropic's popular Claude Code extension, exposing up to 5,000 developers to malware designed to install persistent SSH backdoors.

### Your AI Tool's Supply Chain is Now *Your* Supply Chain

The good news, if you can call it that, is that the attack was time-limited and partially botched. The malicious extensions were only available for about 11 hours, and security researchers noted coding errors that likely prevented the backdoor from working on many systems.

Still, the incident is a concrete example of a new failure mode. The initial point of compromise was a key managed by a third-party AI provider. The data that enabled the attackers to escalate their privileges was user-generated content (agent traces) retained for model training.

This connects directly to a trend of attacks targeting AI development infrastructure, which Wiz dubbed "Black October." The goal is often to steal credentials for unauthorized model inference or, as we see here, to use them as a launchpad for other attacks.

The lesson isn't the usual "vet your vendors." The specific question this incident raises is about the data you share with AI tools. The trade-off for users was clear: disable "Privacy Mode" to help improve the model, and your data—including any credentials you might have accidentally pasted—could end up in a training set that gets compromised.

When you evaluate the next AI-powered developer tool, the questions have to go deeper than features and price. Who is their AI infrastructure provider? What is their data retention policy for prompts and responses? And what, exactly, does enabling "Privacy Mode" do?

---
Source: [Cursor confirms security breach led to malicious Claude Code extension](https://www.bleepingcomputer.com/news/security/cursor-confirms-security-breach-led-to-malicious-claude-code-extension/)
