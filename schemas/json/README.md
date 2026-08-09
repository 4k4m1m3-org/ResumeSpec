# ResumeSpec JSON Schema

## Overview

The ResumeSpec JSON Schema is the technical implementation layer of the ResumeSpec standard.

The specification documents define the concepts, structure, sections, components, and evolution principles of ResumeSpec. The JSON Schema transforms those concepts into a machine-readable contract that enables validation, interoperability, and consistent implementation across different platforms.

The schema defines:

- The required structure of a ResumeSpec document.
- Supported data types.
- Valid sections and components.
- Validation rules.
- Extensibility mechanisms.
- Version compatibility requirements.

The goal is to allow compatible applications, services, and platforms to create, validate, exchange, and consume ResumeSpec documents independently of the programming language, framework, or technology stack used.

---

## Purpose

The JSON Schema provides the technical foundation for ResumeSpec implementations.

It enables:

- Resume builders.
- Applicant Tracking Systems (ATS).
- Recruitment platforms.
- Career management tools.
- AI-powered career assistants.
- Personal portfolio platforms.
- Professional identity systems.

Any system implementing ResumeSpec should be able to use the schema as the source of truth for document validation.

---

## Design Principles

### Human-readable and machine-readable

ResumeSpec documents must be understandable by humans while remaining structured enough for automated processing.

The schema represents professional information in a form that can be consumed by:

- People.
- Software applications.
- Search systems.
- Artificial intelligence systems.

---

### Stable core, extensible ecosystem

ResumeSpec defines a stable core model while allowing future extensions.

The core schema should prioritize:

- Backward compatibility.
- Clear semantics.
- Long-term stability.
- Predictable evolution.

Extensions may introduce:

- New sections.
- New component types.
- Additional metadata.
- Industry-specific information.
- Localization capabilities.

---

### Semantic structure over visual formatting

The JSON Schema represents professional information, not document appearance.

ResumeSpec focuses on:

- Meaning.
- Relationships.
- Skills.
- Experience.
- Achievements.
- Evidence.
- Professional identity.

Presentation and rendering should be handled by external systems.

A single ResumeSpec document should be able to generate multiple representations, including:

- PDF resumes.
- Web profiles.
- Professional portfolios.
- Recruiter dashboards.
- AI-readable profiles.

---

# Schema Structure

A ResumeSpec document consists of two required top-level properties:

    ResumeSpec
    ├── metadata
    └── sections

## Metadata

`metadata` describes the ResumeSpec document itself.

The current schema requires:

- `resumespecVersion`
- `schemaVersion`
- `language`

Additional metadata may include:

- Profile version.
- Creation date.
- Last updated date.
- Visibility.
- Tags.

Example:

    {
      "metadata": {
        "resumespecVersion": "1.0",
        "schemaVersion": "1.0",
        "language": "en"
      }
    }

## Sections

`sections` contains the professional information represented by the profile.

Sections are represented as named properties rather than an ordered array.

The current schema defines sections including:

- Identity.
- Summary.
- Experience.
- Education.
- Certifications.
- Courses.
- Skills.
- Technologies.
- Projects.
- Publications.
- Awards.
- Volunteer activities.
- Languages.
- References.
- Social profiles.
- Links.
- Achievements.
- Interests.
- Attachments.

Sections are independently structured and may be omitted when they are not relevant to a profile.

Example:

    {
      "sections": {
        "summary": {
          "text": "IT Operations professional."
        },
        "skills": [
          {
            "name": "Linux"
          }
        ]
      }
    }

---

## Section Containers

The JSON Schema currently includes experimental reusable definitions for Section Containers.

These definitions support the RFC-0002 proposal:

- `ExperienceSection`
- `SkillSection`
- `TechnologySection`
- `LanguageSection`
- `LinkSection`

These structures are experimental and are not part of the stable Core Model.

---

## Components

Components are reusable building blocks used inside sections.

They allow different sections to share common structures.

Examples include:

- Person.
- Organization.
- Skill.
- Technology.
- Credential.
- Identifier.
- Evidence.
- Date range.
- Link.

Components are referenced by sections through the JSON Schema definitions.

---

# Validation Rules

The JSON Schema defines validation rules required for a valid ResumeSpec document.

## Required properties

At the document level, the schema requires:

    {
      "required": [
        "metadata",
        "sections"
      ]
    }

The `metadata` object currently requires:

    {
      "required": [
        "resumespecVersion",
        "schemaVersion",
        "language"
      ]
    }

Individual sections and their entries define their own supported properties and validation rules.

---

## Data types

Supported data types include:

- String.
- Number.
- Boolean.
- Array.
- Object.
- Null when explicitly allowed.

---

## Enumerations

Controlled values use enumerations where appropriate to maintain consistency.

---

## Standard formats

Where applicable, ResumeSpec uses standard formats.

Examples include:

- Dates.
- URIs.
- Email addresses.
- Language codes.
- Country codes.

---

# Versioning

The JSON Schema follows the ResumeSpec versioning model defined in:

`spec/versioning.md`

ResumeSpec metadata distinguishes between the specification version and the schema version.

Example:

    {
      "metadata": {
        "resumespecVersion": "1.0",
        "schemaVersion": "1.0",
        "language": "en"
      }
    }

Schema and specification versioning follow the rules defined by the ResumeSpec governance and versioning documentation.

---

## Major Versions

Major versions represent breaking changes.

Examples include:

- Removing existing fields.
- Changing the data model.
- Modifying required structures.
- Introducing incompatible changes.

---

## Minor Versions

Minor versions represent backward-compatible improvements.

Examples include:

- Adding optional fields.
- Adding new sections.
- Adding new components.
- Expanding supported capabilities.

---

## Patch Versions

Patch versions represent maintenance improvements.

Examples include:

- Documentation improvements.
- Validation fixes.
- Clarifications.
- Non-structural corrections.

---

# Extensibility Model

ResumeSpec supports extensions without modifying the stable core model.

Extensions may introduce:

- New sections.
- New component types.
- Industry-specific information.
- Additional metadata.
- Localization capabilities.

Extensions should:

- Preserve compatibility.
- Avoid conflicts with the core model.
- Clearly identify ownership.
- Provide documentation.

The extension mechanism is evolving alongside the ResumeSpec governance and specification model.

---

# Compatibility Requirements

A ResumeSpec implementation should:

- Validate documents against the appropriate schema version.
- Reject invalid documents.
- Preserve unknown extensions where supported.
- Support compatible previous versions.
- Provide meaningful validation errors.

---

# Minimal Example

A minimal ResumeSpec document contains the required `metadata` and `sections` properties.

    {
      "metadata": {
        "resumespecVersion": "1.0",
        "schemaVersion": "1.0",
        "language": "en"
      },
      "sections": {
        "summary": {
          "text": "IT Operations professional."
        }
      }
    }

The canonical reference example is available at:

`examples/json/minimal.json`

---

# Future Evolution

The ResumeSpec JSON Schema will evolve together with the standard.

Future versions may introduce:

- Professional knowledge graphs.
- Skill relationship modeling.
- Verified achievements.
- Digital credentials.
- AI-powered career intelligence.
- Portable professional identity.

The JSON Schema is not only a validation file.

It is the technical foundation that enables ResumeSpec to become an interoperable standard for professional identity.