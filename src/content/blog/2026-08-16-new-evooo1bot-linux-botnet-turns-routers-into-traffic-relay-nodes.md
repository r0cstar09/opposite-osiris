---
title: "New Evooo1Bot Linux botnet turns routers into traffic relay nodes"
description: "Emerging botnet expands attack surface, enabling anonymized illicit activity via edge devices."
publishDate: "2026-08-16"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-08-16-new-evooo1bot-linux-botnet-turns-routers-into-traffic-relay-nodes.png"
img_alt: "Abstract cyber defense illustration for New Evooo1Bot Linux botnet turns routers into traffic relay nodes"
---
Another Mirai variant is in the news, this time turning Linux routers into SOCKS5 proxies. The headline is about the botnet, but the lesson is about the system around it. This isn't a malware story; it’s a story about ownership and visibility.

### What happened

A new botnet called Evooo1Bot, based on the Mirai source code, is targeting internet-facing Linux devices like routers. Once it compromises a device, it turns it into a SOCKS5 proxy. This allows attackers to hide their traffic, making it harder to trace where their real attacks—like credential stuffing or phishing—are coming from.

### The wrong conversation

The easy, and wrong, conversation to have is about Evooo1Bot itself. Focusing on the name of the malware or its specific features misses the point. It treats this as a novel threat that needs a novel defense.

It's not. This is a symptom of a much older and more boring problem. The real failure mode is assuming that every internet-facing asset in your environment is actually managed.

### This is an ownership problem

The interesting part of this story is not the botnet. It's that these devices are sitting there, unmanaged and unmonitored, ready to be compromised. That sounds simple, but it’s where security programs break.

What I'd want to know is, who owns the routers?

*   If a router's firmware needs a patch, who is responsible for testing and deploying it? Is it the network team? The local IT admin? A third-party vendor?
*   Are these devices even in an asset inventory? If a device isn't on the standard server image, it probably isn't getting scanned for vulnerabilities or monitored by the SOC.
*   If we detected a compromised router, who would get the ticket? If you don't have an immediate answer, you have an ownership problem.

If nobody owns the asset, nobody owns the risk. Your dashboard showing 100% patch compliance for Windows and RHEL servers is irrelevant if the initial foothold comes through a forgotten, internet-facing router management interface. That is not a tooling problem by itself; it's a gap in governance and basic inventory hygiene.

### What to ask next

This isn't about panicking over a new botnet. It's about using this as a prompt for verification. The next useful signal isn't what Evooo1Bot does next, but whether you can prove you're not exposed to this entire class of attack.

Before this story disappears from the newsfeed, ask a simple question: "Can we produce a list of all internet-facing management interfaces on our network hardware?" The answer, and how long it takes to get it, will tell you more about your security posture than another threat brief.

---

Source: [New Evooo1Bot Linux botnet turns routers into traffic relay nodes](https://www.bleepingcomputer.com/news/security/new-evooo1bot-linux-botnet-turns-routers-into-traffic-relay-nodes/)
