# ResumeSpec Overview

> **One professional identity.**  
> **Unlimited representations.**

---

# Introduction

ResumeSpec is an open specification for representing professional identities in a structured, portable, and machine-readable format.

Rather than defining how a résumé should look, ResumeSpec defines how professional information should be represented.

It provides a common language for describing a person's professional experience, qualifications, knowledge, skills, and achievements independently of any platform, application, or document format.

ResumeSpec is not a résumé format.

It is a specification for professional identity.

---

# Why ResumeSpec Exists

Professional information is fragmented.

A single professional often maintains the same information across multiple systems:

- PDF résumés
- LinkedIn profiles
- Personal websites
- GitHub profiles
- Applicant Tracking Systems (ATS)
- Recruiting platforms
- Company directories
- Human Resources (HR) systems
- AI assistants

Each platform stores similar information using different models, structures, and assumptions.

As a result, professionals must manually maintain multiple versions of the same profile throughout their careers.

Over time, these representations inevitably diverge.

The result is duplicated effort, inconsistent information, outdated profiles, and unnecessary maintenance.

ResumeSpec exists to solve this problem by defining a single, structured representation of professional identity that can be reused everywhere.

---

# The Core Idea

People do not have multiple careers.

They have one professional identity expressed through many different representations.

ResumeSpec standardizes that identity.

Instead of maintaining multiple versions of the same information, professionals maintain a single canonical profile from which every representation can be generated.

The professional identity becomes the source of truth.

Everything else becomes a representation.

---

# Professional Identity

ResumeSpec models a professional identity.

A professional identity is the structured representation of a person's professional journey, capabilities, and achievements throughout their career.

Depending on the individual's background, it may include:

- Identity
- Professional summary
- Work experience
- Education
- Certifications
- Projects
- Skills
- Languages
- Publications
- Presentations
- Awards
- Volunteer work
- References
- Achievements
- Professional interests
- Metadata
- Custom extensions

ResumeSpec defines the meaning and structure of this information.

It intentionally does not define how the information should be presented.

---

# Separation of Data and Presentation

ResumeSpec separates professional data from presentation.

The specification defines **what** the information is.

Implementations decide **how** that information is presented.

The same ResumeSpec document may generate:

- A one-page résumé
- A multi-page curriculum vitae (CV)
- A LinkedIn profile
- A personal portfolio
- An ATS-compatible profile
- A company directory entry
- A JSON API response
- Context for AI assistants
- Internal HR records
- Formats that do not yet exist

Every representation originates from the same professional identity.

---

# Design Principles

ResumeSpec is built around the following principles.

## Single Source of Truth

Professional information should exist only once.

Every representation should be generated from the same canonical profile.

---

## Human Readable

Professional profiles should remain understandable and editable by humans.

No proprietary software should be required to maintain them.

---

## Machine Readable

The specification should be deterministic, structured, and unambiguous.

Software should be able to parse ResumeSpec documents consistently with minimal interpretation.

---

## Presentation Independent

ResumeSpec defines information.

It does not define layouts, typography, colors, branding, templates, or visual design.

Presentation belongs entirely to implementations.

---

## Portable

Professional identities should move freely between applications, organizations, and platforms without losing meaning or information.

---

## Extensible

The specification should evolve without breaking existing documents.

Communities and organizations should be able to extend ResumeSpec while preserving interoperability with the core specification.

---

## Vendor Neutral

ResumeSpec is independent of any company, recruiting platform, cloud provider, or AI vendor.

Anyone may implement the specification.

---

## Open

ResumeSpec is developed openly.

Anyone may study it, implement it, improve it, or contribute to its evolution.

---

# Scope

ResumeSpec defines the structure and semantics of professional information.

Examples include:

- Identity
- Professional summary
- Experience
- Education
- Certifications
- Projects
- Skills
- Languages
- Publications
- Awards
- References
- Metadata
- Extensions

ResumeSpec intentionally does **not** define:

- Résumé templates
- PDF layouts
- Website themes
- Typography
- Visual design
- ATS scoring algorithms
- Recruiting workflows
- Hiring processes
- User interfaces

Those concerns belong to implementations built on top of the specification.

---

# Intended Ecosystem

ResumeSpec is designed to become the foundation of an open ecosystem.

Possible implementations include:

- Résumé generators
- Portfolio generators
- Static site generators
- LinkedIn exporters
- Profile editors
- Schema validators
- APIs
- ATS integrations
- HR software
- AI assistants
- Recruitment platforms
- Developer tools

The specification intentionally avoids prescribing how these tools should be implemented.

Innovation belongs to implementations.

Interoperability belongs to the specification.

---

# Versioning

ResumeSpec follows Semantic Versioning (SemVer).

Backward compatibility is considered a primary design goal.

Breaking changes should be introduced only when they provide substantial long-term benefits and cannot be achieved through additive evolution.

---

# Governance

ResumeSpec is an open community specification.

Its evolution is managed through public discussion and Requests for Comments (RFCs).

Major changes should be proposed, documented, reviewed, and discussed before adoption.

The specification belongs to its community, not to any individual or organization.

---

# Long-Term Vision

ResumeSpec envisions a future where professionals own their professional identity independently of any platform.

Instead of rewriting the same information for every employer, recruiting platform, AI assistant, or online profile, professionals maintain a single structured identity that can be transformed into any required representation.

Platforms will evolve.

Document formats will change.

Artificial intelligence will reshape how professional information is consumed.

Professional identity, however, should remain durable, portable, interoperable, and under the control of the individual.

ResumeSpec exists to make that possible.

---

# Mission Statement

ResumeSpec does not describe a résumé.

It describes a professional.

A résumé is only one representation of that professional.

The professional identity is the source.

Every document, profile, website, application, or future platform is simply another representation of the same underlying identity.

---

**ResumeSpec defines the professional identity.**

**Everything else is a representation.**
