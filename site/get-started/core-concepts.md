# Core Concepts

ResumeSpec v1.0.0 is built around a small set of concepts.

## Professional Identity

The person represented by the profile.

## Metadata

Document-level context such as version, language, timestamps, visibility, and tags.

## Sections

Named containers for professional information:

- identity
- summary
- experience
- education
- certifications
- courses
- skills
- technologies
- projects
- publications
- awards
- volunteer
- languages
- references
- social
- links
- achievements
- interests
- attachments

## Canonical Format

JSON is canonical for v1.0.0. YAML and XML are supported by the reference implementation, but they are not normative formats.

## Validation

Validation is schema-driven. The JSON Schema is the machine-readable contract.

## Extensibility

Core fields are closed by default. Extensions use `x-*` fields.

