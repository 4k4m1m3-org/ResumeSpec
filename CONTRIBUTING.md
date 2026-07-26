# Contributing to ResumeSpec

Thank you for your interest in contributing to ResumeSpec.

ResumeSpec is an open specification designed to define a structured, machine-readable format for resumes and professional profiles. Contributions are welcome across different areas, including specification design, documentation, examples, testing, and implementations.

This document explains how you can contribute effectively to the project.

---

# Ways to Contribute

There are several ways to contribute:

## Specification

Help improve the ResumeSpec standard by:

- Reviewing existing specifications.
- Proposing improvements.
- Identifying ambiguities.
- Suggesting new fields or structures.
- Creating or reviewing RFCs.

Specification changes should follow the RFC process described in the repository.

---

## Documentation

Documentation contributions are highly appreciated:

- Improving explanations.
- Fixing grammar or spelling issues.
- Adding examples.
- Translating documentation.
- Improving guides for new users.

---

## Code

You can contribute by:

- Implementing new features.
- Fixing bugs.
- Improving validation logic.
- Adding tests.
- Improving CLI tools.
- Optimizing existing code.

---

## Testing

Testing contributions help ensure the reliability of ResumeSpec:

- Adding unit tests.
- Reporting unexpected behavior.
- Creating test cases for edge cases.
- Validating schema compatibility.

---

# Before Contributing

Before starting work:

1. Read the project documentation.
2. Review existing issues and discussions.
3. Check current RFC proposals.
4. Make sure your contribution aligns with the project goals.

For significant changes, consider opening an issue first to discuss the proposal.

---

# Development Setup

Clone the repository:

git clone https://github.com/4k4m1m3/ResumeSpec.git

cd ResumeSpec

Install development dependencies:

pip install -r requirements.txt

Run the test suite:

pytest

Make sure all tests pass before submitting changes.

---

# Branch Guidelines

Create a dedicated branch for your contribution:

git checkout -b feature/my-change

Recommended branch naming:

- feature/ - New functionality.
- fix/ - Bug fixes.
- docs/ - Documentation changes.
- test/ - Test improvements.
- refactor/ - Code improvements.

Examples:

feature/json-schema-validation

docs/improve-installation-guide

fix/parser-edge-case

---

# Commit Guidelines

Use clear and descriptive commit messages.

Recommended format:

type: short description

Examples:

docs: improve contributing guide

feat: add resume validation command

fix: handle missing profile fields

test: add schema validation tests

Keep commits focused on a single purpose whenever possible.

---

# Pull Requests

Before submitting a pull request:

- Ensure tests pass.
- Update documentation if required.
- Keep changes focused.
- Explain the motivation behind the change.
- Include relevant examples when applicable.

A good pull request should include:

- A clear title.
- A concise description.
- The problem being solved.
- The proposed solution.
- Any possible impact or compatibility considerations.

---

# RFC Contributions

Changes that modify the ResumeSpec standard itself should go through the RFC process.

Examples of changes requiring an RFC:

- Adding new top-level sections.
- Changing existing data structures.
- Modifying compatibility rules.
- Introducing breaking changes.

RFCs should include:

- Motivation.
- Proposed change.
- Alternatives considered.
- Compatibility impact.

---

# Code Style

Please follow the existing project conventions.

General guidelines:

- Write clear and maintainable code.
- Prefer readability over clever solutions.
- Add tests for new functionality.
- Document public interfaces.
- Avoid unnecessary dependencies.

---

# Reporting Issues

When reporting an issue, include:

- A clear description of the problem.
- Steps to reproduce it.
- Expected behavior.
- Actual behavior.
- Environment information when relevant.

Good issue reports help maintainers understand and solve problems faster.

---

# Community Guidelines

All contributors are expected to:

- Be respectful.
- Provide constructive feedback.
- Accept different perspectives.
- Focus on improving the project.

Please read the project's Code of Conduct before participating.

---

# License

By contributing to ResumeSpec, you agree that your contributions will be licensed under the same license as the project.

See the LICENSE file for more information.

---

Thank you for helping improve ResumeSpec.