---
title: "Default Azure Automation Setting Enables Cross-Tenant Identity Takeover"
description: "Default cloud settings can compromise cross-tenant identity; prioritize immediate audit and remediation."
publishDate: "2026-07-25"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-07-25-default-azure-automation-setting-enables-cross-tenant-identity-takeover.png"
img_alt: "Abstract cyber defense illustration for Default Azure Automation Setting Enables Cross-Tenant Identity Takeover"
---
The headline is about a default Azure setting, but the real story is about ownership. This kind of flaw is less about a clever exploit and more a test of whether you know what’s running in your environment and who is responsible for it.

### What Happened

A default public configuration in Azure Automation, combined with other flaws, could have allowed an attacker to take over another tenant's identity. In a shared cloud environment, that’s about as bad as it gets—it breaks the isolation we all assume we have. An attacker could get at another customer's data, credentials, and workloads. Microsoft has pushed fixes, but the problem of risky defaults in complex services isn't going away.

### What People Will Get Wrong

The mistake is to treat this as a Microsoft problem that Microsoft fixed. The story is over, move on. Or worse, to assume your cloud security posture tool would have flagged this and saved the day.

That thinking completely misses the operational reality. The interesting part isn't the specific vulnerability chain; it's that these Azure Automation accounts are exactly the kind of thing that gets created for a project and then orphaned. If nobody owns the asset, nobody owns the risk. And nobody is checking the configuration.

### A More Useful Lens

Let's be practical. The CISO asks, "Are we exposed to this?" The security team's first question isn't about the exploit mechanics. It's "Where are all of our Azure Automation accounts?" followed immediately by "Who the hell owns them?"

This is where response plans fall apart. It sounds simple, but it's not. You can't just run a single query and get a clean list with owner names. You're digging through runbooks and service principals set up years ago, maybe by someone who doesn't even work here anymore. This is an inventory and ownership problem first, and a vulnerability second.

An alert on a dashboard is not a control. Knowing about a misconfiguration is useless if you can't find the person with the context and the permissions to fix it. That’s not a tooling problem; it’s a governance problem.

### What to Watch Next

Don't just watch for this becoming repeatable attacker tradecraft. Watch your own team.

Can you answer the question: "Show me all Azure Automation accounts and their owners right now"? If the answer is a week-long investigation, that's the real vulnerability to fix. Use this disclosure as a forcing function to validate your cloud inventory and make sure every asset has a clear owner. Because the next "dangerous default" in some other service is already out there waiting.

---

Source: [Default Azure Automation Setting Enables Cross-Tenant Identity Takeover](https://www.darkreading.com/cloud-security/default-azure-automation-setting-cross-tenant-identity-takeover)
