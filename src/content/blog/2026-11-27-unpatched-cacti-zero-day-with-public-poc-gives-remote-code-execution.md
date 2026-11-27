---
title: "Unpatched Cacti zero-day with public PoC gives remote code execution"
description: "Immediately isolate or remove unpatched Cacti instances to prevent active exploitation."
publishDate: "2026-11-27"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-11-27-unpatched-cacti-zero-day-with-public-poc-gives-remote-code-execution.png"
img_alt: "Editorial hero image for Unpatched Cacti zero-day with public PoC gives remote code execution"
---
A zero-day in the Cacti network monitoring tool is making the rounds, complete with a public proof-of-concept for unauthenticated remote code execution. While RCE is always serious, the interesting part here is the attack path. It’s a clean, four-request chain that turns a seemingly harmless guest account into a command shell.

### The Path from Guest to Shell

According to the researcher who published the exploit, the attack doesn't require a login, a valid API key, or any user interaction. It relies on the Cacti guest account being enabled—a common default state.

The attack itself is a stored SQL injection. As reported by BleepingComputer, an attacker can use the guest account's permissions to save malicious SQL statements in their graph display preferences. These preferences are stored in the Cacti database. When the backend poller process reads these preferences to generate a graph, it executes the attacker's SQL. This allows the attacker to modify the poller's own configuration and instruct it to run arbitrary OS commands on the server.

The result is RCE as the user running the Cacti poller process. While the researcher demonstrated root access, security firm watchTowr notes that privileges will depend on the specific deployment—it could just as easily be a low-privileged web server account. Still, compromising a central monitoring tool is a powerful pivot point, especially since Cacti often holds credentials for other network devices.

### A Familiar Disclosure Story

The exploit was published on GitHub without prior coordination with the Cacti project. The researcher, identified as "ek0ms savi0r," expressed frustration with the broader state of vulnerability disclosure, citing years of reports being dismissed by various companies.

This isn't just a technical failure in an application; it's a story about the breakdown of the disclosure process. The researcher's write-up points to a common sentiment: "We get cracked because we get gaslit for years by billion dollar companies that treat disclosure like a PR problem." When researchers feel that official channels are a dead end, some will opt for public disclosure. This puts defenders in a reactive position, but it also forces a conversation about how vendors handle security reports.

### The Immediate Mitigation

With no patch available at the time of the report, the obvious advice is to take Cacti servers offline. If that's not an option, the most direct mitigation is to disable the guest account. Since the entire attack chain hinges on guest access, turning it off should break the exploit.

Administrators can also look for signs of compromise. The report suggests reviewing poller configurations for unexpected commands and checking application logs for warnings about non-numeric values in graph settings, which could indicate an attempt to inject malicious code.

This incident is a good reminder to audit not just what's exposed to the internet, but what features are enabled by default inside our tools. How many other applications have a "guest" mode with just enough permission to become a foothold?

---

Source: [Unpatched Cacti zero-day with public PoC gives remote code execution](https://www.bleepingcomputer.com/news/security/unpatched-cacti-zero-day-with-public-poc-gives-remote-code-execution/)
