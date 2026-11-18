---
title: "Microsoft’s Agent Framework PyPI package compromised to steal credentials"
description: "Compromised AI dev tools risked our cloud credentials, highlighting critical supply chain vulnerabilities."
publishDate: "2026-11-18"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-11-18-microsoft-s-agent-framework-pypi-package-compromised-to-steal-credential.png"
img_alt: "Editorial hero image for Microsoft’s Agent Framework PyPI package compromised to steal credentials"
---
### A PyPI hijack that ran without an `import`

A recent compromise of Microsoft's `agent-framework` on PyPI is a good reminder that a malicious package doesn't need to be imported to run. Attackers published two malicious versions of the popular AI agent toolkit, but the interesting part is *how* the payload executed. They used a classic Python trick: a `.pth` file.

These path configuration files are a feature of Python's `site-packages` directory. They're meant to add extra directories to `sys.path`, but they can also execute arbitrary code on interpreter startup. In this case, the attackers dropped a `.pth` file that loaded and ran a credential-stealing script. This means any developer who installed the bad package (`1.26.1` or `1.26.2`) had the malware running in their environment every time they launched Python, even if their own code never touched the agent framework.

### Targeting the modern dev workflow

The payload wasn't a generic keylogger. According to analysis from several security firms, the malware was a credential harvester built for modern, cloud-native development. It was designed to scrape secrets from environment variables and configuration files, specifically targeting:

*   Azure and AWS credentials
*   GitHub, Docker, and Hugging Face tokens
*   OpenAI API keys

Even more specifically, the malware attempted to grab Azure managed identity access tokens and OIDC tokens from Azure DevOps and GitHub Actions. This shows a clear intent to move from a compromised developer machine or CI/CD runner into the cloud control plane. All stolen data was exfiltrated to a single `webhook.site` endpoint.

### A persistent intrusion

The incident timeline, reported by BleepingComputer on November 18, 2026, shows a determined attacker. After PyPI administrators quarantined the first malicious release, the attacker pushed a second one just two and a half minutes later. This suggests the compromise of Microsoft's PyPI publishing credentials wasn't immediately contained. The second package was also caught and quarantined within minutes, but the attacker's quick response implies they still had access.

The immediate advice is to check for the malicious versions and rotate any credentials that might have been exposed. But the bigger question is about the attack vector. It's still unclear how the attacker gained publishing rights to an official Microsoft package. Until that's public, it's hard for anyone else to know what control actually failed.

---

Source: [Microsoft’s Agent Framework PyPI package compromised to steal credentials](https://www.bleepingcomputer.com/news/security/microsofts-agent-framework-pypi-package-compromised-to-steal-credentials/)
