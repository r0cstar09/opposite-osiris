---
title: "Malicious Claude Code extension on Cursor planted SSH backdoors"
description: "5,000 developers exposed to SSH backdoors via a compromised AI dev tool."
publishDate: "2026-10-30"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-10-30-malicious-claude-code-extension-on-cursor-planted-ssh-backdoors.svg"
img_alt: "Editorial cyber defense illustration for Malicious Claude Code extension on Cursor planted SSH backdoors"
---
A malicious extension for an AI code editor recently aimed to install SSH backdoors on developer machines, but the attack was largely tripped up by its own coding errors. The incident is less a story about a sophisticated threat and more a look at the clumsy realities of supply chain attacks.

On October 29, a malicious version of Anthropic's Claude Code extension appeared on the marketplace for Cursor, an AI-focused editor built on VS Code. According to a report from *BleepingComputer*, the package was available for about 11 hours and potentially exposed up to 5,000 developers.

### A Backdoor That Couldn't Open the Door

The malware’s goal was to establish a persistent SSH backdoor. It bundled a malicious JavaScript loader that executed as soon as the extension was installed, collecting system information and attempting to phone home to an attacker-controlled server.

However, researchers at Phorion and OpenSourceMalware who analyzed the code found some embarrassing bugs.

On macOS, the malware tried to check if SSH was enabled by running `systemsetup -getremotelogin`. But it ran the command without the necessary elevated privileges, causing it to error out. The script was coded to proceed only if the command's output contained "Off," so the error caused it to skip the step of actually enabling SSH.

The failure on Windows was even more basic. The malware tried to install and start the OpenSSH server using PowerShell commands, but it attempted to execute them via `/bin/sh`—a Unix shell that isn't part of a standard Windows install. The setup failed immediately.

In both cases, if the SSH server wasn't already running, the reverse tunnel the malware tried to create couldn't provide access.

### Recon Still Worked

Even with the failed backdoor, the malware wasn't entirely useless. It successfully collected and exfiltrated reconnaissance data, including the user's hostname, public IP, Git email address, and the names of environment variables that might point to credentials. The script didn't steal the credentials directly, suggesting the attackers planned to return for manual access later.

Cursor removed the malicious package, temporarily shut down its marketplace for an audit, and worked to get the attacker's server taken offline.

### The Real Supply Chain Question

The most interesting part of this story isn't the buggy malware, but how it got there. An attacker was able to publish a malicious package under Anthropic's name in Cursor's official marketplace.

The report leaves the central question unanswered: was Cursor's publishing infrastructure compromised, or did Anthropic's credentials get stolen? Without knowing the entry point, it's hard to evaluate the security of this specific ecosystem. For any team using specialized, AI-centric developer tools, the real question is about the integrity of the marketplace itself. How does the platform verify publisher identity before a package goes live?

---

Source: [Malicious Claude Code extension on Cursor planted SSH backdoors](https://www.bleepingcomputer.com/news/security/malicious-claude-code-extension-on-cursor-planted-ssh-backdoors/)
