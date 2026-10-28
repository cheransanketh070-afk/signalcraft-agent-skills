# Security Policy

## Scope

This repository contains agent instructions, Markdown references, templates, and small maintenance scripts. It does not ship a network service or require API credentials to use the skills.

## Reporting a vulnerability

Please do not publish secrets, exploit details, or private data in a public issue. Use GitHub's private vulnerability reporting feature if enabled for this repository. If it is unavailable, contact the maintainer through the verified contact information on the GitHub profile and request a private channel.

Include the affected file/version, impact, reproduction steps with synthetic data, and a suggested mitigation if known.

## Safety posture

- Never put API keys, passwords, access tokens, private customer data, or internal URLs into skill files or issue templates.
- Review scripts and skill instructions before running/enabling them.
- Installer scripts do not overwrite an existing same-named skill unless `--overwrite` is provided.
- Skills are not a sandbox; host tools and permissions determine what an agent can do.
