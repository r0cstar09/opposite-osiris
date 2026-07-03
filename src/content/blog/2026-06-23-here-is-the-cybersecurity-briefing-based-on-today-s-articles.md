---
title: "Here is the cybersecurity briefing based on today's articles:"
description: "Global FortiGate credential theft impacts 430k firewalls, over 100M user credentials."
publishDate: "2026-06-23"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-06-23-here-is-the-cybersecurity-briefing-based-on-today-s-articles.png"
img_alt: "Abstract cyber defense illustration for Here is the cybersecurity briefing based on today's articles:"
---
The headline numbers are big, but the useful question is what this story exposes about how security programs actually break. This isn't about Fortinet specifically; it's about what happens when a device you trust becomes the point of failure.

### What happened

According to a SOCRadar report, an active campaign is targeting FortiGate firewalls. Attackers are reportedly using custom Golang-based sniffers on compromised firewalls to steal credentials. The report claims over 430,000 firewalls have been targeted, with more than 110 million user credentials identified as compromised or at risk.

### What people will get wrong

The mistake is focusing on the 110 million credentials. That number is a symptom, not the disease. The real failure is a compromised network perimeter device. If an attacker can deploy a custom sniffer to your firewall, you have a much bigger problem than stolen passwords. The firewall itself has been owned. Chasing the credentials feels like progress, but it ignores the root cause: the integrity of a core security control has failed.

### This is an ownership problem

When a firewall is compromised, the first question shouldn't be about the credentials. It should be: who owns this box? Is it the network team, focused on uptime and traffic? Or the security team, who should be worried about device integrity?

That sounds simple, but it's where programs break. If nobody is responsible for baselining the firewall's software and configuration, how would you ever detect a malicious tool running on it? Your logs might look fine. Traffic might be flowing. The dashboard is not the control.

The interesting part is not the exploit; it's the assumption that our security infrastructure is secure. This story shows that assumption can fail at scale. What I'd want to know is:

- Can we prove our firewalls *haven't* been modified?
- Do we have telemetry from the device itself, not just the traffic passing through it?
- If we found a custom sniffer, who would be responsible for the investigation and cleanup?

If you don't have answers to those questions, you don't have a credential problem—you have a governance and visibility problem waiting for a headline.

### What to watch next

The signal to watch isn't how many more credentials leak. The signal is whether teams use this as a reason to validate their own perimeter controls. This is a perfect, non-controversial reason to ask your network team: "Can we prove what's running on our firewalls? Let's test our ability to detect unauthorized changes."

If the conversation stays at the level of password resets, the lesson has been missed. If it forces a real conversation about device ownership and integrity monitoring, then it's a useful wake-up call.

---
