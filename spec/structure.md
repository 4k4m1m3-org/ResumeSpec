# ResumeSpec Structure

ResumeSpec defines a professional profile as a structured document composed of independent sections.

Each section represents one aspect of a person's professional identity.

The standard intentionally separates structure from representation.

A resume, portfolio, LinkedIn profile, company directory, recruiting platform, or AI assistant may choose to display only a subset of the available sections while preserving the same underlying profile.

---

# Core Principles

The ResumeSpec structure follows several principles.

## Modular

Every section is independent.

Applications may ignore sections they do not support without breaking compatibility.

## Extensible

New sections can be added in future versions without modifying existing ones.

## Machine-readable

Every section has a predictable structure that software can validate.

## Human-centered

Although designed for machines, every section represents information that humans naturally understand.

---

# High-level Structure

A ResumeSpec profile consists of multiple top-level sections.

```
Profile
├── Identity
├── Summary
├── Experience
├── Education
├── Certifications
├── Skills
├── Projects
├── Awards
├── Publications
├── Languages
├── References
├── Contact
└── Metadata
```

Not every profile needs every section.

A student profile may not contain work experience.

A researcher may contain publications.

A freelancer may contain many projects.

The standard supports all of these without requiring a different format.

---

# Required vs Optional Sections

ResumeSpec distinguishes between required and optional sections.

## Required

These sections are necessary to identify the profile.

Examples include:

- Identity
- Metadata

## Recommended

Most professional profiles should include them.

Examples include:

- Summary
- Experience
- Skills

## Optional

These sections exist only when relevant.

Examples include:

- Publications
- Awards
- References
- Projects
- Patents
- Volunteer Work

Future versions of ResumeSpec may introduce additional optional sections.

---

# Ordering

The logical order of sections does not define their presentation order.

For example:

A recruiter may want to see:

Experience
→ Skills
→ Certifications

A university may prefer:

Education
→ Publications
→ Awards

An AI assistant may use all available sections simultaneously.

ResumeSpec stores structured information.

Applications decide how to present it.

---

# Relationships Between Sections

Sections are independent but may reference one another.

For example:

- A certification may validate a skill.
- A project may demonstrate experience.
- A publication may belong to a research position.
- An award may reference a project.

These relationships enrich the profile without creating duplication.

---

# Metadata

Every ResumeSpec document contains metadata describing the profile itself.

Examples include:

- specification version
- document identifier
- creation date
- last updated
- language
- profile owner

Metadata allows software to process ResumeSpec documents consistently.

---

# Future Extensions

The ResumeSpec structure is designed for long-term evolution.

Future versions may introduce new sections without breaking existing implementations.

Applications that do not recognize a section should safely ignore it while preserving the rest of the profile.

This guarantees forward compatibility across versions.

---

# Next Step

This document explains *how* ResumeSpec is organized.

The next document, `sections.md`, defines every section and the information it may contain.
