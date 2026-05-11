# Okta Advanced Posture Checks — Sample osquery Checks

This folder contains sample osquery checks that can be used with [Okta Advanced Posture Checks](https://support.okta.com/help/s/blog/a67KZ000000oLyAYAU/introducing-advanced-posture-checks-for-device-compliance-enforcement?language=en_US).

## What Are Advanced Posture Checks?

Advanced Posture Checks extend Okta's device assurance capabilities by letting you write your own SQL-based osquery checks instead of relying solely on built-in device attributes. When a user tries to access a protected resource, Okta Verify runs the configured osquery checks on the device and returns the results to Okta, which evaluates them against the device assurance policy before granting access.

This enables enforcement of highly specific security requirements, such as the absence of known-malicious software, unauthorized tools, or compromised packages; as a condition of access. Checks run via [osquery](https://osquery.io/), a lightweight endpoint agent that exposes OS data through a SQL interface.

## Folder Structure

Checks are organized by the platform(s) they target:

| Folder     | Description                                      |
| ---------- | ------------------------------------------------ |
| `Cross/`   | Checks that apply to any Operative System        |
| `macOS/`   | Checks targeting macOS-specific osquery tables   |
| `Windows/` | Checks targeting Windows-specific osquery tables |

## File Format

Each check follows this YAML structure:

```yaml
title: <Human-readable name>
id: <Unique identifier>
description: <What the check detects and why it matters>
references:
  - <Links to threat intel or vendor documentation>
author:
  - <Author email>
platform:
  - macOS | Windows | Linux
query: |
  <osquery SQL query>
```

The `query` field contains standard SQL compatible with osquery's virtual table schema. Queries should return a non-empty result set when a threat is detected (positive match) and an empty result set when the device is clean.
