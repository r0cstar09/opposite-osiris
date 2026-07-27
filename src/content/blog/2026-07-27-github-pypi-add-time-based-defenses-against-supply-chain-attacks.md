---
title: "GitHub, PyPI add time-based defenses against supply chain attacks"
description: "New platform defenses significantly reduce open-source supply chain attack exposure."
publishDate: "2026-07-27"
tags: ["cyber", "threat-intelligence", "defense"]
img: "/assets/blog/hermes-relay/2026-07-27-github-pypi-add-time-based-defenses-against-supply-chain-attacks.png"
img_alt: "Abstract cyber defense illustration for GitHub, PyPI add time-based defenses against supply chain attacks"
---
The new time-based defenses from GitHub and PyPI are getting attention, but not for the right reasons. This isn't a story about platforms solving supply chain security. It's a story about whether our own internal processes are mature enough to even benefit from the help.

### What's Happening

GitHub and PyPI are adding friction for attackers by introducing time-based holds on newly published or updated packages. The idea is to create a delay—a window of time where a new package is held for analysis and reputation checks before it's widely available. This gives automated tooling a chance to spot malicious code before it gets pulled into thousands of projects.

### Where People Will Get It Wrong

The obvious take is that this is a great new layer of defense, and it is. But the mistake is thinking this is a passive control that just works for you in the background. It's not.

The platforms are giving you a window of time. That's it. They aren't stopping your developers or your build pipelines from pulling a malicious package that manages to get through. Believing the problem is now "handled" by the platform is where security programs will fail.

### This Is Really a Visibility Problem

That delay is only valuable if you can use it. The real question this news should trigger is: "Do we even have a policy for the age of packages we consume?"

That sounds simple, but it's where the work actually is.
- Do you know which of your projects are pulling dependencies flagged as "new"?
- Can your build systems enforce a rule like, "Reject any package less than 72 hours old"?
- If a critical project *needs* a brand-new release to fix a bug, who owns the risk assessment and exception process?

If you can’t answer those questions, then the platform's new time delay doesn't do much for you. The feature gives you an opportunity to build a better internal control, but it's not the control itself. Your CI/CD pipeline is the real enforcement point. If nobody owns the dependency management rules, nobody owns the risk.

### What to Watch Next

The signal to watch isn't what attackers do next. It's what your own development and security teams do.

Use this as a prompt. Ask your teams: "How would we operationalize this? Can we prove we aren't pulling a package that was published five minutes ago?" If the answer is a shrug, that's the real vulnerability the story exposes. The headline is about the platform, but the lesson is about your own house.

---

Source: [GitHub, PyPI add time-based defenses against supply chain attacks](https://www.bleepingcomputer.com/news/security/github-pypi-add-time-absed-defenses-against-supply-chain-attacks/)
