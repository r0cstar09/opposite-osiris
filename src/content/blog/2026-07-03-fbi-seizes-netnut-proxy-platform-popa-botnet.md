---
title: "FBI Seizes NetNut Proxy Platform, Popa Botnet"
description: "Immediately assess if our systems contributed to this botnet or used its services."
publishDate: "2026-07-03"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-07-03-fbi-seizes-netnut-proxy-platform-popa-botnet.png"
img_alt: "Abstract cyber defense illustration for FBI Seizes NetNut Proxy Platform, Popa Botnet"
---
The real question isn't just *if* your systems are part of this botnet, but how quickly you can prove they aren't. That’s the test this FBI takedown puts to every security team.

### What happened

The FBI, with help from industry partners, seized hundreds of domains tied to NetNut, a large residential proxy service. This action came after NetNut was linked to the Popa botnet, a network of at least two million compromised devices.

Essentially, a legitimate-looking proxy service was allegedly being used as the command-and-control infrastructure for a massive botnet. The devices in the botnet are regular computers and IoT gear, infected without their owners' knowledge. The full story is over at Brian Krebs's site.

### What people will get wrong

The easy mistake is to treat this as just another threat intelligence story. File the domains, check for a match, and move on. But the headline is about the takedown; the lesson is about the system around it.

This is really an ownership and visibility problem. The story isn't that a proxy service was abused—that happens all the time. The interesting part is that it forces a question most teams don't want to answer: can you prove a negative? Can you prove none of your assets are sending traffic through this network? If an alarm didn't go off, how would you even know to look?

### This is a pop quiz for your program

In the first 24 hours, the job isn't just to block IOCs. It’s to validate your controls.

The first question is about business risk: did anyone in the company buy services from NetNut? Maybe for market research or ad verification? If nobody owns third-party service procurement, you have no idea what your real attack surface is. You need to be able to answer that question fast.

The second question is about asset compromise: are any of your endpoints part of the Popa botnet?

That sounds simple, but it’s where programs break. How would you actually check?
- Do you have logs of all outbound connections from your endpoints? Are they searchable?
- Can you quickly query your entire fleet for signs of the malware?
- What if the compromised device is some unmanaged IoT thing sitting on the guest network?

If the answer is "we'd have to check with the network team" or "our EDR should have caught it," that's not good enough. The dashboard is not the control. This is a moment to prove you can trace activity from your network out into the world. If you can't, that's the real failure mode, and it's a lot more boring and a lot more common than a botnet headline.

### What to watch next

The useful signal here isn't what the attackers do next. It's what security teams do. Will this story be used as a no-notice fire drill to test egress visibility and asset inventory? Or will it just be a headline that fades from the feed by next week?

I'd use this as a prompt. Ask your team how they would prove you're not involved. If the answer is weak, you've found your next real project. That's more valuable than just summarizing the story.

---

*Generated from Hermes Relay's daily cyber briefing and edited through Tony's practitioner voice profile before publishing to this blog.*

Source: [FBI Seizes NetNut Proxy Platform, Popa Botnet](https://krebsonsecurity.com/2026/07/fbi-seizes-netnut-proxy-platform-popa-botnet/)

Pipeline note: lens: First 24 hours; draft model: projects/project-a89720ac-d6be-45fe-a4b/locations/us-central1/publishers/google/models/gemini-2.5-flash.
