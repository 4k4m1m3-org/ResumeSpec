# ResumeSpec

> One professional identity. Unlimited representations.

ResumeSpec is an open specification for representing professional identities in a structured, portable, and machine-readable format.

Instead of treating a résumé as the source of truth, ResumeSpec defines a canonical professional profile that can be transformed into multiple representations while preserving the same underlying information.

A résumé is only one possible output.

---

## Why ResumeSpec?

Today, professional information is fragmented.

The same person manually maintains:

- Résumés
- LinkedIn profiles
- Portfolio websites
- Job board profiles
- Internal HR systems
- Freelance platforms

Each platform requires rewriting, reformatting, and synchronizing the same information.

This duplication creates inconsistency, outdated information, and unnecessary work.

ResumeSpec proposes a different model.

Instead of editing multiple documents, maintain a single structured professional identity that can generate any representation.

---

## Core Principles

ResumeSpec is built around a few fundamental ideas:

- A person has one professional identity.
- Documents are representations, not the source.
- Information should be structured, not formatted.
- The specification must be human-readable.
- The specification must be machine-readable.
- The specification must be vendor-neutral.
- The specification should be extensible over time.

---

## What ResumeSpec is

ResumeSpec is:

- an open specification
- a portable professional profile
- a structured data model
- a common language for professional information
- a foundation for tools and generators

---

## What ResumeSpec is not

ResumeSpec is not:

- a résumé template
- a visual design system
- a PDF generator
- a LinkedIn replacement
- a recruiting platform

---

## Possible representations

A ResumeSpec profile could generate:

- Professional résumé (PDF)
- ATS-friendly résumé
- Personal portfolio website
- LinkedIn-compatible profile
- JSON API
- Markdown profile
- HTML profile
- Internal HR profile
- Developer portfolio
- AI-ready context
- Future formats not yet invented

All of them originate from the same source.

---

## Repository Structure

```
/
├── README.md
├── VISION.md
├── ROADMAP.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
│
├── spec/
│   ├── overview.md
│   ├── structure.md
│   ├── sections.md
│   ├── versioning.md
│   └── schema/
│
└── rfcs/
```

---

## Documentation

The specification is organized as follows.

| Document | Description |
|----------|-------------|
| `spec/overview.md` | What ResumeSpec is |
| `spec/structure.md` | Overall specification structure |
| `spec/sections.md` | Definition of profile sections |
| `spec/versioning.md` | Versioning strategy |
| `rfcs/` | Proposed changes to the specification |

---

## Current Status

ResumeSpec is currently under active design.

The specification is evolving through public discussion and RFCs before reaching its first stable release.

Early feedback is encouraged.

---

## Contributing

Contributions are welcome.

Whether you are a developer, recruiter, designer, HR professional, or simply interested in improving how professional information is represented, your feedback is valuable.

Please read:

- CONTRIBUTING.md
- CODE_OF_CONDUCT.md

before opening issues or pull requests.

---

## License

ResumeSpec is released under the MIT License.

---

## Vision

People do not have multiple careers.

They have one professional identity expressed through many different formats.

ResumeSpec standardizes that identity.
