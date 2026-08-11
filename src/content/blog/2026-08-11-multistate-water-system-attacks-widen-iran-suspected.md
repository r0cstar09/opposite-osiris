---
title: "Multistate Water System Attacks Widen, Iran Suspected"
description: "Widespread water utility attacks highlight broad critical infrastructure vulnerability to state actors."
publishDate: "2026-08-11"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-08-11-multistate-water-system-attacks-widen-iran-suspected.png"
img_alt: "Abstract cyber defense illustration for Multistate Water System Attacks Widen, Iran Suspected"
---
The story about widespread attacks on water utilities is a perfect example of how we miss the point. The headline is about Iran, but the lesson is about basic asset management.

### What Happened

According to reports, attackers are targeting water systems in at least a dozen U.S. states. They aren't using zero-days; they're going after internet-exposed Programmable Logic Controllers (PLCs) that are easy to find and compromise. U.S. authorities suspect Iran-backed groups are behind it, likely for disruption and reconnaissance.

### What People Will Get Wrong

The common mistake here is to focus on the nation-state attacker. It’s easy to get distracted by the attribution to Iran and frame this as a sophisticated threat. That’s not the useful part of the story.

This isn't really an advanced persistent threat problem. It's a "Why is critical infrastructure sitting on the public internet?" problem. It's a failure of the most basic security controls: asset inventory and exposure management. If a device is controlling water for a community, it shouldn't be discoverable with a simple internet scan.

### The Practitioner Lens

When I see a story like this, my first thought isn't about the attacker's TTPs. It's about ownership. Who is responsible for that PLC? Is it even in an asset inventory? Or is it just a box that was installed a decade ago and has been running ever since, outside of any security program's visibility?

This is where security programs break. We build dashboards and run vulnerability scans on the networks we know about. But the real failure mode is usually boring and forgotten. A PLC connected to the internet isn't a tooling failure by itself; it's a governance failure. Someone, at some point, either decided to connect it or didn't know they shouldn't.

The question I'd be asking my team is simple: Can we prove we don't have this problem? How would we even check? If nobody owns the asset, nobody owns the risk. That's the real story here.

### What to Watch Next

This isn't about panic; it's about verification. The immediate takeaway isn't to start hunting for Iranian malware. It's to use this as a forcing function to answer some basic questions.

Can you produce a list of all internet-facing OT assets in your environment? Do you know who is responsible for them? If the answer is "no" or "maybe," that's your next priority. The story will fade from the news cycle, but the underlying exposure will remain until someone takes ownership of it.

---

Source: [Multistate Water System Attacks Widen, Iran Suspected](https://www.darkreading.com/ics-ot-security/multistate-water-system-attacks-widen-iran-suspected)
