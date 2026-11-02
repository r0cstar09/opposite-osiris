---
title: "Hackers disrupt refrigeration systems at European supermarkets"
description: "Cyberattacks now directly threaten physical operations and revenue; evaluate our OT exposure."
publishDate: "2026-11-02"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-11-02-hackers-disrupt-refrigeration-systems-at-european-supermarkets.svg"
img_alt: "Editorial cyber defense illustration for Hackers disrupt refrigeration systems at European supermarkets"
---
An attack on supermarket refrigeration systems isn't a hypothetical tabletop exercise anymore. According to a November 2026 report from BleepingComputer, hackers remotely targeted freezers and coolers across more than 115 stores in at least six European countries, forcing systems into defrost mode or, in one case, cranking the heat to +50°C (122°F).

This isn't just another IT incident. It's a direct attack on operational technology (OT) that resulted in spoiled food, emergency interventions with refrigerated trucks, and immediate product loss. The targets included stores from major chains like Carrefour, ICA, and Ahold Delhaize.

### A Known Flaw, Exploited Again

The most telling detail is that this wasn't a novel attack. The director of Sabcobel, a refrigeration systems vendor involved in the incident, told reporters that the attackers used the same vulnerability exploited in similar attacks on French supermarkets just a month prior.

This raises an obvious and uncomfortable question: if the vulnerability was known, why were so many systems still exposed?

The answer points to the messy reality of securing OT in a distributed, franchise-based business. Statements from supermarket chains like ICA and Spar Colruyt noted that the affected locations were often run by independent entrepreneurs or operated outside the company's central network. These operators have their own refrigeration systems, which means corporate IT security doesn't necessarily have visibility or control.

### Remediation Is More Than a Software Update

According to the Sabcobel director, protecting the systems isn't as simple as pushing a patch. While the "simplest solution" is to manage the refrigerators via a secure internet connection, he stated that a software update alone is not enough and that physical modifications are also required.

This is a critical detail for any practitioner. When a fix requires a truck roll, it introduces significant friction. For an independent store owner, the cost and logistical hassle of scheduling a technician for a physical hardware change can lead to delays. The vendor said "most" of their clients adopted the secure solution after the first attack in France, which implies a meaningful number did not. Those were the stores that got hit.

This incident is a clear example of how OT risk materializes in the real world. It's not about a nation-state actor disabling the power grid; it's about a known flaw in a common commercial product being exploited for disruption. The defense isn't a sophisticated SIEM rule, but a physical hardware change that someone has to approve, schedule, and pay for.

For anyone managing security for a business with physical operations, the key question isn't just whether your OT is on the network. It's what happens when a vendor tells you a critical fix requires more than a download. How do you track that remediation across dozens or hundreds of locations you don't directly own?

---

Source: [Hackers disrupt refrigeration systems at European supermarkets](https://www.bleepingcomputer.com/news/security/hackers-disrupt-refrigeration-systems-at-european-supermarkets/)
