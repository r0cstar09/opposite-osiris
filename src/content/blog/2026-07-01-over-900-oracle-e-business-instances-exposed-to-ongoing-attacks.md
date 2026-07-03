---
title: "Over 900 Oracle E-Business instances exposed to ongoing attacks"
description: "Identify and secure critical Oracle EBS systems immediately, as attacks are active."
publishDate: "2026-07-01"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-07-01-over-900-oracle-e-business-instances-exposed-to-ongoing-attacks.png"
img_alt: "Abstract cyber defense illustration for Over 900 Oracle E-Business instances exposed to ongoing attacks"
---
The headline is about active attacks against Oracle EBS. The real story is about how these ancient, critical systems fall through the cracks.

### What Happened

A BleepingComputer report says over 900 Oracle E-Business Suite (EBS) instances are exposed online and being actively attacked. Attackers are using known flaws to get unauthenticated access to the ERP platform, which often houses a company's most sensitive financial and operational data.

Patches are available for some of these vulnerabilities, but the problem is that hundreds of these systems are sitting on the internet, unpatched or misconfigured.

### This Is an Ownership Problem

The immediate reaction is to treat this as a simple patching failure. "Just patch it" is the easy answer, but it misses the point entirely. The fact that over 900 critical ERP systems are exposed to the public internet is not just a patching problem; it's a symptom of a much deeper ownership problem.

These massive, complicated EBS platforms are often managed by a mix of teams: DBAs, application developers, finance department analysts, and IT infrastructure. When everyone has a piece of it, who is ultimately responsible for its security posture? Who is supposed to be checking for external exposure?

If nobody owns the asset, nobody owns the risk. That sounds simple, but it’s where security programs actually break. The real failure mode here is boring: a critical system that’s been running for 15 years has no clear owner, so basic hygiene like exposure monitoring and patch management never gets done. The dashboard is not the control.

### What I'd Want to Know

Forget the CVE for a second. The first question I’d ask is: can we produce a definitive list of every Oracle EBS instance we have, and who is the single point of contact accountable for it? Not the team, the *person*.

If we can't answer that, then running a vulnerability scan is just security theater. The scan will find the problem, but the ticket will get passed around between teams until the next breach headline comes along.

This is where the story gets useful. It’s a prompt to force an uncomfortable conversation. The security team’s job isn’t just to point out the vulnerability; it’s to find the person who has the authority and budget to fix it and make sure they accept the risk if they don't. That is not a tooling problem.

### What to Watch Next

The signal to watch isn't whether attackers reuse this exploit. They will. The real signal is internal. Use this story as a reason to audit your own critical, legacy applications.

Can you prove where your EBS instances are? Can you prove they aren't exposed? If you can't, this isn't a threat intelligence issue. It's a governance and visibility gap you need to fix before it shows up on someone else's report.

---

Source: [Over 900 Oracle E-Business instances exposed to ongoing attacks](https://www.bleepingcomputer.com/news/security/over-900-oracle-e-business-instances-exposed-to-ongoing-attacks/)
