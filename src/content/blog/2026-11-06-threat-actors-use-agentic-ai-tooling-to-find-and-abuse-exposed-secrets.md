---
title: "Threat actors use agentic AI tooling to find and abuse exposed secrets"
description: "Automated secret scanning and credential hygiene are now critical."
publishDate: "2026-11-06"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-11-06-threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets.png"
img_alt: "Editorial hero image for Threat actors use agentic AI tooling to find and abuse exposed secrets"
---
According to a Microsoft report from November 2026, threat actors are using an agentic AI framework to automate attacks, progressing from a public code scan to cloud data exfiltration in as little as five minutes. This isn't just about finding secrets faster; it's about chaining the entire attack together without a human at the keyboard.

### An Agent That Troubleshoots

The offensive framework, which Microsoft calls ARTEX, does more than just `grep` GitHub for exposed keys. The notable capability is its adaptive behavior. Microsoft observed the agent making API calls that initially failed, only to then correct itself and succeed.

In one example, the agent sent a request to the Azure Resource Manager (ARM) control plane using an incorrect API version meant for the data plane. After receiving an HTTP 400 error, it waited 28 seconds, then resubmitted the request with the correct ARM API version, receiving an HTTP 200. This isn't just a dumb script; it's a workflow with basic troubleshooting logic built in. This allows the agent to move from initial access to internal reconnaissance and exfiltration automatically.

### The Automated Attack Chain

The observed attacks followed a clear pattern. The agent scans public repositories for credentials, then uses a compromised service principal to authenticate to a target's Entra ID tenant. From there, it’s off to the races.

Microsoft saw the agent enumerate cloud resources, hunt for more credentials in Azure Key Vault and Storage Accounts, and access data in SharePoint and OneDrive. The entire process, from discovery to action, is automated. The speed of the attack drastically shortens the window for defenders to respond to a leaked-secret alert before actual damage is done.

### Deception as a Defense

While the usual advice about secret hygiene—rotating keys, using managed identities, and scanning your own code—is still fundamental, it’s not the whole story here. Because the threat is an automated agent, the defensive playbook can expand.

Microsoft’s report suggests using decoys and honeypots to disrupt the agent's workflow. The idea is to present the agent with attractive but fake targets, wasting its time and compute budget. A "fake win," where the agent believes it has successfully completed its objective on a decoy asset, could cause it to halt the attack prematurely. This approach targets the automation logic itself, rather than just blocking an IP address that the agent can easily change.

The report provides a few IOCs, including the IP address `199.19.77[.]84`, but emphasizes that these are easily changed. The real challenge isn't blocking this specific tool, but building defenses that can withstand automated, adaptive attacks. The question now is how brittle these agentic frameworks are. Can they distinguish a well-crafted honeypot from a real production system?

---

Source: [Threat actors use agentic AI tooling to find and abuse exposed secrets](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/)
