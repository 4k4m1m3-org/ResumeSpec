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

The goal is to allow any compatible application, service, or platform to create, validate, exchange, and consume ResumeSpec documents independently of the programming language, framework, or technology stack used.

---

## Purpose

The JSON Schema exists to provide a technical foundation for ResumeSpec implementations.

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

The schema should represent professional information in a way that can be consumed by:

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

A ResumeSpec document is organized around several core concepts:

## Document Identity

Every ResumeSpec document should include metadata that identifies:

- The ResumeSpec version.
- The document identifier.
- Document metadata.

Example:

{
  "spec_version": "1.0.0",
  "id": "resume-example-001"
}

---

## Profile

The profile represents the professional identity of the person.

It may contain:

- Name.
- Professional headline.
- Summary.
- Contact information.
- Location.
- External links.
- Personal branding information.

Example:

{
  "profile": {
    "name": "Jane Smith",
    "headline": "Cloud Security Engineer",
    "summary": "Security professional focused on cloud infrastructure and incident response."
  }
}

---

## Sections

Sections represent meaningful areas of professional information.

Examples include:

- Experience.
- Education.
- Skills.
- Certifications.
- Projects.
- Publications.
- Languages.
- Achievements.

The available sections and their behavior are defined in:

spec/sections.md

Example:

{
  "sections": [
    {
      "type": "experience",
      "items": []
    }
  ]
}

---

## Components

Components are reusable building blocks used inside sections.

They allow different sections to share common structures.

Examples:

- Experience entries.
- Organizations.
- Skills.
- Certifications.
- Achievements.
- Credentials.

Example:

{
  "type": "achievement",
  "title": "Improved deployment reliability",
  "impact": "Reduced operational incidents by 40%"
}

---

# Validation Rules

The JSON Schema defines validation rules required for a valid ResumeSpec document.

Validation includes:

## Required properties

Mandatory fields required for a valid document.

Example:

{
  "required": [
    "spec_version",
    "profile"
  ]
}

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

Controlled values should use enumerations to maintain consistency.

Example:

{
  "type": "string",
  "enum": [
    "experience",
    "education",
    "skills",
    "projects"
  ]
}

---

## Standard formats

Where possible, ResumeSpec uses standard formats.

Examples:

- Date.
- URI.
- Email.
- Language codes.
- Country codes.

---

# Versioning

The JSON Schema follows the ResumeSpec versioning model defined in:

spec/versioning.md

Schema versions follow:

MAJOR.MINOR.PATCH

Example:

{
  "spec_version": "1.0.0"
}

---

## Major Versions

Major versions represent breaking changes.

Examples:

- Removing existing fields.
- Changing the data model.
- Modifying required structures.
- Introducing incompatible changes.

---

## Minor Versions

Minor versions represent backward-compatible improvements.

Examples:

- Adding optional fields.
- Adding new sections.
- Adding new components.
- Expanding supported capabilities.

---

## Patch Versions

Patch versions represent maintenance improvements.

Examples:

- Documentation improvements.
- Validation fixes.
- Clarifications.
- Non-structural corrections.

---

# Extensibility Model

ResumeSpec supports extensions without modifying the core schema.

Extensions should use namespaces or unique identifiers.

Example:

{
  "extensions": {
    "organization.example": {
      "custom_field": "value"
    }
  }
}

Extensions must:

- Preserve compatibility.
- Avoid conflicts with the core model.
- Clearly identify ownership.
- Provide documentation.

---

# Compatibility Requirements

A ResumeSpec implementation should:

- Validate documents against the appropriate schema version.
- Reject invalid documents.
- Preserve unknown extensions.
- Support compatible previous versions.
- Provide meaningful validation errors.

---

# Minimal Example

Example of a minimal ResumeSpec document:

{
  "spec_version": "1.0.0",

  "profile": {
    "name": "John Doe",
    "headline": "Software Engineer"
  },

  "sections": [
    {
      "type": "skills",
      "items": [
        {
          "name": "Python",
          "level": "advanced"
        }
      ]
    }
  ]
}

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
