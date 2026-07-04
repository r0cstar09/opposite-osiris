---
title: "NetNut proxy network disrupted, 2 million infected devices cut off"
description: "Major criminal infrastructure disruption enhances global digital hygiene."
publishDate: "2026-07-04"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-07-04-netnut-proxy-network-disrupted-2-million-infected-devices-cut-off.png"
img_alt: "Abstract cyber defense illustration for NetNut proxy network disrupted, 2 million infected devices cut off"
---
A big proxy network takedown is good news, but the interesting part isn't the disruption itself. It's that two million consumer devices were part of a criminal supply chain, and most of their owners had no idea.

### What happened

Google and international law enforcement agencies disrupted NetNut, a residential proxy network. The service sold access to over two million compromised Android devices—mostly smart TVs and streaming boxes. Attackers used these devices to anonymize their traffic for credential stuffing and other fraudulent activity. The takedown cuts off a significant source of infrastructure for those groups.

### What people will get wrong

The easy takeaway is to celebrate a law enforcement win and move on. But that misses the point. The real failure mode here isn't one criminal network; it's the massive, unsecured attack surface created by consumer IoT devices.

This is really an ownership problem. Who is responsible for the security of a smart TV? The user? The manufacturer? The ISP? If nobody owns the asset, nobody owns the risk when it gets absorbed into a botnet that can be used to attack your company.

### A practitioner's view

Okay, but what does this mean for a corporate security team? We don't manage our employees' smart TVs.

This is a visibility problem. Traffic from these compromised devices looks just like legitimate residential IP addresses, making it much harder to detect credential stuffing and other automated attacks. The core question this story raises is: can you actually distinguish malicious residential proxy traffic from your real users?

That sounds simple, but it’s where detection and response programs break. It’s not a tooling problem by itself. It’s about knowing what your telemetry can and can't see. The question is whether the team can prove what happened when an alert fires from an IP that looks like just another remote employee.

### What to watch next

The headline is about the exploit, but the lesson is about the system around it. I'd use this as a prompt to ask some direct questions internally. Can we prove we can detect traffic from known malicious proxy networks? Do our logs even have the fidelity to make that call?

And if we find something, who owns the response? This is less about panic and more about verifying that your controls work the way you assume they do, before the next headline drops.

---

*Generated from Hermes Relay's daily cyber briefing and edited through Tony's practitioner voice profile before publishing to this blog.*

Source: [NetNut proxy network disrupted, 2 million infected devices cut off](https://www.bleepingcomputer.com/news/security/netnut-proxy-network-disrupted-2-million-infected-devices-cut-off/)

Pipeline note: lens: Supply chain and third-party risk; draft model: projects/project-a89720ac-d6be-45fe-a4b/locations/us-central1/publishers/google/models/gemini-2.5-flash.
