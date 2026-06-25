---
title: "Attackers Hit Cisco SD-WAN Flaw 2 Months Before Disclosure"
description: "Active exploitation means immediate investigation and remediation of core network infrastructure is paramount."
publishDate: "2026-06-25"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-06-25-attackers-hit-cisco-sd-wan-flaw-2-months-before-disclosure.png"
img_alt: "Abstract cyber defense illustration for Attackers Hit Cisco SD-WAN Flaw 2 Months Before Disclosure"
---
The headline is about an exploit, but the lesson is about the two-month blind spot. Patching today is the easy part. Proving you weren't owned for the last 60 days is where a security program actually breaks.

### What happened

A critical Cisco SD-WAN vulnerability, CVE-2026-20245, was actively exploited for two months before it was publicly disclosed. According to Mandiant's research, attackers used the flaw to establish unauthorized peering with affected devices. From there, they created rogue root accounts, giving them complete control over the network hardware.

### What people will get wrong

The common mistake is to treat this like any other patch-and-scan cycle. A team will run a scan, apply the patch, the light will turn green, and the ticket will get closed.

That misses the entire point. This isn't a patching problem; it's a forensics problem that started two months ago. The question isn't "are we vulnerable *now*?" It's "were we compromised *then*?"

### The real work is hunting, not just patching

If you're running this gear, your first 24 hours after hearing this news shouldn't be a race to patch. It should be a hunt. Assume you were hit and work backward to prove you weren't.

What I'd want to know is, can we even answer the question? Do we have logs going back two months that show unauthorized peering or new accounts on our network devices? Does anyone even own those logs, or know what "bad" looks like?

This is really an ownership and visibility problem. If you can't tell who had root on your SD-WAN appliance last month, you have no way to prove you're safe now. Patching the hole doesn't tell you if someone is already inside the house.

### What to watch next

The signal to watch isn't the patch rate for this CVE. It's whether this kind of pre-disclosure exploitation against core infrastructure becomes a repeatable playbook.

Use this as a fire drill for your own program. Ask the question: can we validate who has admin on our critical network devices? Can we prove it for last week? Last month? If the answer is no, that's the real vulnerability to fix.

---

*Generated from Hermes Relay's daily cyber briefing and edited through Tony's practitioner voice profile before publishing to this blog.*

Source: [Attackers Hit Cisco SD-WAN Flaw 2 Months Before Disclosure](https://www.darkreading.com/cyberattacks-data-breaches/attackers-hit-cisco-sd-wan-flaw-2-months-before-disclosure)

Pipeline note: lens: First 24 hours; draft model: projects/project-a89720ac-d6be-45fe-a4b/locations/us-central1/publishers/google/models/gemini-2.5-flash.
