---
title: "\"City-Forum\" data-theft attacks target Salesforce, ServiceNow portals"
description: "Critical SaaS platforms need immediate third-party risk review of configuration."
publishDate: "2026-08-13"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-08-13-city-forum-data-theft-attacks-target-salesforce-servicenow-portals.png"
img_alt: "Abstract cyber defense illustration for \"City-Forum\" data-theft attacks target Salesforce, ServiceNow portals"
---
This isn't really a Salesforce or ServiceNow vulnerability story. It's an ownership story. The headline is about attackers scraping data, but the real lesson is about how easily we lose track of the systems we depend on.

### What happened

Attackers are using custom tools to scrape sensitive data from public-facing Salesforce Experience Cloud and ServiceNow portals. The campaign, called "City-Forum," has been active since at least March 2024. It’s not exploiting a software flaw; it’s just pulling data that organizations have inadvertently exposed to anonymous users through their portal configurations.

### What people will get wrong

The easy mistake here is to file this under "third-party risk" and assume a vendor questionnaire would have caught it. That completely misses the point.

This is not a tooling problem by itself. The failure isn't that Salesforce or ServiceNow are insecure. The failure is assuming that a powerful, configurable platform is secure by default. The real failure mode is usually more boring: a business unit spins up a portal, sets some fields to public for a forgotten reason, and then nobody ever looks at it again. If nobody owns the asset, nobody owns the risk.

### The practitioner lens

This is where the story gets useful. The "City-Forum" campaign is just a symptom of a widespread governance gap. We buy powerful SaaS platforms to move faster, but we often forget to assign clear responsibility for how they're configured and managed over time.

That sounds simple, but it's where security programs break. The interesting part is not the attacker's custom tooling. The interesting part is asking your own organization a few direct questions:

*   Who has the authority to create a public-facing portal in our critical SaaS apps?
*   Who is responsible for reviewing the data exposed through those portals?
*   Can we even produce a list of all of them, right now?
*   Do we have logs that show what anonymous users are accessing?

The dashboard is not the control. Your SaaS security posture management (SSPM) tool might show you a green checkmark, but if a business team can expose customer PII with a few clicks in a portal builder, the control isn't working. This is really an ownership problem.

### What to watch next

I wouldn't get distracted by the name "City-Forum." I'd use this as a direct prompt to pressure-test my own program. The question is whether the team can prove what happened—or what *could* happen—in its own environment.

Forget the threat intel feed for a minute. What I'd want to know is whether we can validate our own SaaS configurations today. Can we confirm what's exposed, check the logs, and prove we have a clear owner who can fix a misconfiguration before the next BleepingComputer article drops? That’s the signal that matters.

---

Source: ["City-Forum" data-theft attacks target Salesforce, ServiceNow portals](https://www.bleepingcomputer.com/news/security/city-forum-data-theft-attacks-target-salesforce-servicenow-portals/)
