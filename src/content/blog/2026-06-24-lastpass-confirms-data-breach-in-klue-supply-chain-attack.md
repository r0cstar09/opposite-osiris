---
title: "LastPass confirms data breach in Klue supply chain attack"
description: "A single third-party compromise amplified risk across multiple organizations."
publishDate: "2026-06-24"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-06-24-lastpass-confirms-data-breach-in-klue-supply-chain-attack.png"
img_alt: "Abstract cyber defense illustration for LastPass confirms data breach in Klue supply chain attack"
---
The headline is about LastPass, but the real story is about OAuth tokens and the blast radius of your vendors. This isn't just another supply-chain story; it's a reminder that access granted to a partner is still access you have to defend.

### What happened

The short version: Attackers used stolen OAuth tokens from a third-party vendor, Klue, to get into LastPass's Salesforce environment. This is a direct consequence of the Klue supply chain attack reported earlier this month. It's a classic case of a compromise at one company creating a breach at another.

### What people will get wrong

The easy takeaway is "supply chain attacks are bad." That's not useful.

The real mistake is treating this as a vendor problem you can solve with a questionnaire. This is an identity and access management problem. The attackers didn't breach a firewall; they used a key (an OAuth token) that was stolen from a partner to walk in the front door of a critical application. The headline is about the exploit, but the lesson is about the system around it.

### This is an ownership problem

That OAuth token from Klue gave it access to the LastPass Salesforce environment. That sounds simple, but it's where security programs break.

What I'd want to know is:
*   Who on the security team owned that integration?
*   Who was tracking what that token could actually *do*?
*   What logging was in place to detect anomalous activity from a third-party token?

This isn't about blaming the person who set up the integration. It's about whether the security team has the visibility to even ask these questions *before* an incident. The dashboard is not the control. If you can't trace the permissions of every third-party token connected to your critical apps, you don't have a vendor risk program, you have a vendor risk spreadsheet.

### What to watch next

The question now is whether this kind of OAuth abuse becomes standard attacker tradecraft. I'd watch for similar disclosures.

More practically, I'd use this as a prompt to ask my own team: Can we inventory all third-party OAuth tokens with access to our core SaaS apps? Can we see what they're doing? If the answer is "no" or "maybe," that's the next thing to fix.

---

Source: [LastPass confirms data breach in Klue supply chain attack](https://www.bleepingcomputer.com/news/security/lastpass-confirms-data-breach-in-klue-supply-chain-attack/)
