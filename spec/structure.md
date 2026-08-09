# ResumeSpec Structure

ResumeSpec defines a professional profile as a structured document composed of metadata and independent sections.

The standard intentionally separates professional information from its representation.

A resume, portfolio, LinkedIn profile, company directory, recruiting platform, or AI assistant may choose to display only a subset of the available sections while preserving the same underlying professional profile.

---

# Core Principles

The ResumeSpec structure follows several principles.

## Modular

Professional information is organized into independent sections.

Applications may support all sections or only a subset depending on their purpose.

## Extensible

New sections and capabilities may be introduced in future versions while preserving compatibility with existing profiles whenever possible.

## Machine-readable

The structure is predictable and defined through formal schemas so that software can validate and process ResumeSpec documents consistently.

## Human-centered

Although designed for machine processing, every section represents information that humans naturally understand.

## Presentation-independent

The logical structure of a ResumeSpec document does not define how the information should be displayed.

Applications and services are responsible for presentation.

---

# Document Structure

A ResumeSpec document consists of two required top-level properties:

```text
ResumeSpec
├── metadata
└── sections
```

The `metadata` property describes the ResumeSpec document and its version information.

The `sections` property contains the professional information represented by the profile.

This separation allows the document to describe both its own technical context and the professional identity it represents.

---

# Metadata

The `metadata` property contains information describing the ResumeSpec document.

The current Core Model requires:

* `resumespecVersion`
* `schemaVersion`
* `language`

Additional metadata may include:

* Profile version
* Creation date
* Last updated date
* Visibility
* Tags

Metadata describes the document and its processing context. It does not represent a professional section.

---

# Sections

The `sections` property contains the professional information represented by the profile.

Sections are represented as named properties rather than an ordered array.

The current Core Model defines the following sections:

* Identity
* Summary
* Experience
* Education
* Certifications
* Courses
* Skills
* Technologies
* Projects
* Publications
* Awards
* Volunteer
* Languages
* References
* Social
* Links
* Achievements
* Interests
* Attachments

Not every profile needs every section.

A student profile may contain education and skills without professional experience.

A researcher may contain publications and academic achievements.

A freelancer may contain many projects and professional links.

The same ResumeSpec structure supports these different profiles without requiring a different document format.

The detailed structure and supported information for each section are defined in `sections.md`.

---

# Required vs Optional Sections

ResumeSpec requires the top-level `metadata` and `sections` properties.

The individual sections contained within `sections` are optional unless a future version of the specification explicitly defines otherwise.

Applications may therefore create profiles containing only the sections relevant to the professional identity being represented.

For example, a minimal profile may contain:

* Identity
* Summary
* Skills

while a more comprehensive profile may contain many additional sections.

The absence of a section does not indicate that the corresponding information is invalid or unavailable. It only means that the profile does not represent that information.

---

# Section Independence

Sections are independently structured.

Applications may process, display, export, or ignore individual sections according to their capabilities and use case.

For example:

* A resume generator may use Identity, Summary, Experience, Education, and Skills.
* A portfolio may emphasize Projects, Publications, Links, and Technologies.
* A recruiting system may prioritize Experience, Skills, Certifications, and Education.
* An AI assistant may process all available sections.

Applications should preserve information they do not understand whenever the surrounding format and implementation allow it.

---

# Ordering

The logical order of sections does not define their presentation order.

For example, a recruiter may want to present:

```text
Experience
→ Skills
→ Certifications
```

A university may prefer:

```text
Education
→ Publications
→ Awards
```

An AI assistant may use all available sections simultaneously.

ResumeSpec stores structured information.

Applications decide how that information is presented.

---

# Relationships Between Sections

Sections are conceptually independent but may contain information that relates to information represented elsewhere in the profile.

For example:

* A certification may provide evidence of a skill.
* A project may demonstrate the application of a technology or skill.
* A publication may be associated with professional or academic experience.
* An award may recognize the results of a project.

These relationships allow implementations to build richer representations without requiring professional information to be duplicated unnecessarily.

The Core Model defines reusable components that can be used by multiple sections.

---

# Reusable Components

ResumeSpec uses reusable components to represent common concepts shared across sections.

Examples include:

* Person
* Organization
* Position
* DateRange
* Contact
* Location
* Link
* Skill
* Technology
* Language
* Credential
* Identifier
* Evidence

Components provide consistent structures for information that may appear in multiple sections.

For example, an `Organization` may be used by Experience, Education, Certifications, Projects, Awards, and Volunteer activities.

The detailed component definitions are implemented in the JSON Schema and documented as part of the Core Model.

---

# Extensibility

The ResumeSpec structure is designed to evolve over time.

Future versions may introduce:

* New sections.
* New optional fields.
* New reusable components.
* Additional metadata.
* Extension mechanisms.

Applications should be designed to handle unknown optional information safely whenever possible.

Extensions must preserve the meaning of the Core Model and should not redefine existing fields or concepts.

Extension mechanisms and compatibility requirements are defined by the ResumeSpec specification and its governance process.

---

# Experimental Structures

ResumeSpec may contain experimental structural concepts proposed through Requests for Comments (RFCs).

RFC-0002 proposes Section Containers such as:

* `ExperienceSection`
* `SkillSection`
* `TechnologySection`
* `LanguageSection`
* `LinkSection`

These structures are experimental and are not part of the stable Core Model unless formally adopted.

Experimental structures must therefore not be treated as required elements of a standard ResumeSpec profile.

---

# Compatibility and Evolution

ResumeSpec is designed to support long-term evolution.

When future versions introduce new optional sections or fields, implementations that do not recognize them should safely ignore them whenever possible while preserving the rest of the profile.

This approach allows the ecosystem to evolve without requiring every implementation to support every capability immediately.

Compatibility guarantees and version evolution rules are defined in `versioning.md`.

---

# Separation of Structure and Representation

ResumeSpec defines the structure and semantics of professional information.

It does not define:

* Resume layouts
* Typography
* Colors
* Branding
* Website themes
* PDF formatting
* User interfaces

A single ResumeSpec document may therefore generate multiple representations while preserving the same underlying professional identity.

For example:

```text
                    ResumeSpec
                        │
          ┌─────────────┼─────────────┐
          │             │             │
        Resume       Portfolio     LinkedIn
          │             │             │
          └─────────────┼─────────────┘
                        │
                 Same professional
                      identity
```

The representation may change.

The underlying professional information remains the same.

---

# Next Step

This document explains *how* a ResumeSpec document is organized.

The next document, `sections.md`, defines the official sections and the information they may contain.
