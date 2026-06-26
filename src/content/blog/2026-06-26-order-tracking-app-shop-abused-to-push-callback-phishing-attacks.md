---
title: "Order-tracking app Shop abused to push callback phishing attacks"
description: "Verify all inbound support requests; assume legitimate apps can be weaponized."
publishDate: "2026-06-26"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-06-26-order-tracking-app-shop-abused-to-push-callback-phishing-attacks.png"
img_alt: "Abstract cyber defense illustration for Order-tracking app Shop abused to push callback phishing attacks"
---
This isn't just another phishing story. It's about what happens when attackers weaponize the trust you've outsourced to a third-party application.

The headline is about the exploit, but the lesson is about the system around it.

### What happened

Attackers are injecting fake purchase receipts into Shopify's "Shop" order-tracking app. These fake orders look legitimate but contain fraudulent support numbers. When a user calls the number, they're connected to a scammer who tries to social engineer them into installing remote access software or giving up sensitive information.

The whole thing works because the notification comes from a trusted app that people use every day.

### What people will get wrong

The easy, and wrong, takeaway is that this is just another user awareness problem. The impulse is to say, "we need to train users to be more skeptical." That's not a strategy; it's a wish.

This is really a third-party risk and visibility problem. An approved, legitimate application has become an unmonitored attack channel. If the Shop app is on a corporate phone, you’ve implicitly trusted it. Now that trust is being used to bypass your other controls.

### The practitioner's question

The interesting part is not the phishing lure. The interesting part is what happens next, and whether you can even see it.

That sounds simple, but it's where programs break. Let's ask some better questions:

*   If an employee calls the fake number from a work device and installs a remote access tool, does your EDR generate an alert? Does anyone see it?
*   Do you have an inventory of which third-party consumer apps are connected to corporate identities or installed on managed devices?
*   Who owns that risk? If the answer is "the user," you don't have a program.

Telling people to "verify all inbound support requests" is fine, but it's not a control. The real failure mode is assuming your existing security stack gives you visibility into the activity happening *inside* every legitimate app on every device. It probably doesn't.

### What to watch next

The signal to watch is whether this tactic—injecting malicious content into trusted, high-volume consumer apps—becomes a repeatable playbook. It probably will.

I'd use this as a prompt to pressure-test some assumptions. Can you prove what third-party apps are running in your environment? Can you detect the installation of a new remote access tool, regardless of how the user was convinced to install it?

This is less about panic and more about verification. If nobody owns the app, nobody owns the risk. Find out who owns it before a real incident forces the conversation.

---

*Generated from Hermes Relay's daily cyber briefing and edited through Tony's practitioner voice profile before publishing to this blog.*

Source: [Order-tracking app Shop abused to push callback phishing attacks](https://www.bleepingcomputer.com/news/security/order-tracking-app-shop-abused-to-push-callback-phishing-attacks/)

Pipeline note: lens: Supply chain and third-party risk; draft model: projects/project-a89720ac-d6be-45fe-a4b/locations/us-central1/publishers/google/models/gemini-2.5-flash.
