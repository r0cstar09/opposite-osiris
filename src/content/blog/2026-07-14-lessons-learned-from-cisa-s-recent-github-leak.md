---
title: "Lessons Learned from CISA’s Recent GitHub Leak"
description: "Public code leaks demand immediate automated credential scanning and remediation."
publishDate: "2026-07-14"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-07-14-lessons-learned-from-cisa-s-recent-github-leak.png"
img_alt: "Abstract cyber defense illustration for Lessons Learned from CISA’s Recent GitHub Leak"
---
The CISA credential leak isn't shocking because it happened; it's useful because it shows how security programs actually break. The headline is about a federal agency's mistake, but the lesson is about visibility and ownership.

### What happened

A CISA contractor pushed code containing sensitive credentials, including AWS GovCloud keys, to a public GitHub repository. The data was exposed for nearly six months before an external party, KrebsOnSecurity, discovered and reported it.

### What people will get wrong

The easy takeaway is to blame the contractor or to treat this as a simple reminder to scan for secrets. That misses the point. The interesting part isn't the leak itself, but the six-month detection gap.

This isn't a story about a sophisticated attack. It's a story about a boring, systemic failure. The real failure mode is usually a gap in ownership, a blind spot in asset management, or an alert that nobody is assigned to receive.

### Practitioner lens

That six-month gap is where the story gets more useful. It tells me that a control either failed or wasn't there in the first place. This is less about buying a new scanner and more about asking hard questions about the ones you already have.

What I'd want to know is:

-   Was this repository even in scope for CISA's security tooling? If you don't know a contractor is using a personal repo for your project, you can't scan it. This is an asset and third-party management problem.
-   If there was a scanner, did it miss this specific format? Or did it fire an alert that went into an unmonitored queue?
-   Who owned the response? A tool finding a key is just a notification. Who was responsible for revoking the credential, confirming it was no longer active, and scrubbing it from the repository's history?

That sounds simple, but it's where programs break. A dashboard showing "100% scanned" is not the same as a validated control. If nobody owns the asset, nobody owns the risk. This incident is a perfect example.

### What to watch next

The question is whether your team can prove what happened here couldn't happen to you.

Use this as an excuse to verify your own program. Don't just ask if you have secret scanning. Ask for proof that it’s covering all repositories, including those used by contractors. Ask who gets the alert and what the documented procedure is for revoking a key at 2 AM on a Saturday.

The real signal isn't in another postmortem. It's in the answers you get to those questions.

---

Source: [Lessons Learned from CISA’s Recent GitHub Leak](https://krebsonsecurity.com/2026/07/lessons-learned-from-cisas-recent-github-leak/)
