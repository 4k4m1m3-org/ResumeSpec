# Security Policy

## Overview

The security of ResumeSpec and its ecosystem is an important priority.

Although ResumeSpec is primarily an open specification project, security considerations are relevant across:

- Specification design.
- Reference implementations.
- Validation tools.
- Data processing.
- Community contributions.

This document explains how to report security issues and how they will be handled.

---

# Supported Versions

ResumeSpec is currently under active development.

Security fixes will generally be applied to:

- The latest stable release.
- The current development branch when applicable.

Older versions may not receive security updates.

Users are encouraged to keep their ResumeSpec implementations and dependencies updated.

---

# Reporting a Security Vulnerability

If you discover a potential security vulnerability, please report it privately.

Do not publicly disclose security issues through:

- GitHub Issues.
- Pull Requests.
- Public discussions.

before the issue has been reviewed and addressed.

---

# How to Report

When reporting a security issue, please include:

- A clear description of the vulnerability.
- Steps to reproduce the issue.
- Potential impact.
- Affected components or versions.
- Any relevant logs, examples, or proof of concept information.

Providing detailed information helps the maintainers investigate and resolve the issue faster.

---

# Security Report Handling

After receiving a security report, maintainers will:

1. Acknowledge receipt of the report.
2. Review and validate the reported issue.
3. Determine the impact and affected components.
4. Develop a mitigation or fix when necessary.
5. Communicate the resolution process with the reporter when appropriate.

Response times may vary depending on the complexity and severity of the issue.

---

# Responsible Disclosure

ResumeSpec follows a responsible disclosure approach.

Security researchers and contributors are encouraged to:

- Give maintainers reasonable time to investigate.
- Avoid exposing sensitive information publicly.
- Avoid accessing, modifying, or deleting data belonging to others.
- Avoid actions that could negatively impact project users.

Good-faith security research is appreciated and helps improve the project.

---

# Security Considerations for Resume Data

ResumeSpec defines a structured format for professional information, which may contain sensitive personal data.

Implementations using ResumeSpec should consider:

- Protecting personal information.
- Applying appropriate access controls.
- Avoiding unnecessary data exposure.
- Validating external input.
- Protecting stored resume documents.
- Following applicable privacy regulations.

ResumeSpec does not guarantee the security of data stored or processed by third-party implementations.

---

# Implementation Security Guidelines

Developers implementing ResumeSpec should consider:

- Validating input data before processing.
- Avoiding insecure parsing methods.
- Keeping dependencies updated.
- Handling malformed documents safely.
- Preventing injection vulnerabilities.
- Protecting credentials and secrets.
- Applying secure software development practices.

---

# Scope of Security Issues

Examples of security issues that should be reported include:

- Remote code execution vulnerabilities.
- Authentication or authorization issues.
- Data exposure vulnerabilities.
- Unsafe parsing behavior.
- Validation bypasses with security impact.
- Dependency vulnerabilities affecting ResumeSpec components.

---

# Out of Scope

The following are generally not considered security vulnerabilities unless they create a significant security impact:

- Documentation errors.
- Feature requests.
- Normal specification disagreements.
- Minor usability issues.
- Non-sensitive validation improvements.

---

# Security Updates

Security-related updates may be communicated through:

- Release notes.
- Changelog entries.
- Security advisories when applicable.

Users are encouraged to monitor project updates to stay informed about security improvements.

---

# Acknowledgments

ResumeSpec appreciates the efforts of security researchers, contributors, and community members who responsibly report issues and help improve the security of the project.

Thank you for helping keep ResumeSpec secure.