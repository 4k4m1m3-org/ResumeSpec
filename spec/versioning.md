# ResumeSpec Versioning

## Purpose

ResumeSpec is designed to become a long-lived open standard for representing professional profiles.

As the ecosystem grows, the specification will evolve. This document defines how ResumeSpec versions are managed, how compatibility is preserved, and how changes are introduced over time.

The purpose of versioning is to provide:

- Stability for existing profiles.
- Predictability for implementers.
- Clear migration paths between versions.
- Long-term interoperability.
- Confidence that professional information remains portable over time.

ResumeSpec versioning focuses on evolving the standard without losing the meaning and value of the professional data represented within it.


# Version Format

ResumeSpec follows Semantic Versioning principles.

Version format:

MAJOR.MINOR.PATCH

Example:

1.4.2

Where:

MAJOR:
Introduces breaking changes that may require migrations.

MINOR:
Introduces backward-compatible features and extensions.

PATCH:
Introduces corrections, clarifications, and improvements that do not affect compatibility.


# Version Lifecycle

ResumeSpec evolves through three levels of change:

- Patch releases.
- Minor releases.
- Major releases.

Each level has different compatibility expectations.


# Patch Releases

Format:

MAJOR.MINOR.PATCH

Example:

1.2.0 → 1.2.1

Patch releases contain changes that do not modify the structure or meaning of ResumeSpec data.

Examples:

- Fixing documentation errors.
- Improving examples.
- Clarifying definitions.
- Correcting schema descriptions.
- Improving validation messages.
- Adding missing explanations.

Patch releases must not require profile migrations.

A ResumeSpec document created with version 1.2.0 remains valid under version 1.2.1.


# Minor Releases

Format:

MAJOR.MINOR.0

Example:

1.2.0 → 1.3.0

Minor releases introduce new capabilities while preserving backward compatibility.

Examples:

- Adding new optional sections.
- Adding new optional fields.
- Introducing additional metadata.
- Supporting new profile representations.
- Adding new extension mechanisms.

Minor releases must follow these principles:

- Existing fields must preserve their original meaning.
- New fields should be optional by default.
- Existing implementations should safely ignore unknown fields.
- Existing profiles should remain valid.


Example:

A profile created using:

ResumeSpec 1.2

should continue working with:

ResumeSpec 1.3


# Major Releases

Format:

MAJOR.0.0

Example:

1.0.0 → 2.0.0

Major releases introduce changes that may break compatibility.

Examples:

- Changing the fundamental data model.
- Removing existing fields.
- Renaming core concepts.
- Changing relationships between entities.
- Modifying validation rules.
- Altering the meaning of existing properties.

Major releases require:

- Migration documentation.
- Compatibility notes.
- Updated schemas.
- Migration guidance.
- Clear explanation of breaking changes.


# Pre-1.0 Development Phase

Before the first stable release, ResumeSpec uses:

0.x.y

versions.

During this phase:

- The specification is considered experimental.
- The data model may evolve significantly.
- Breaking changes may occur.
- Community feedback has a strong influence on design decisions.

The purpose of the 0.x phase is to discover a stable foundation before committing to long-term compatibility guarantees.


Example:

0.3.0 → 0.4.0

may include structural changes that would normally require a major version after 1.0.0.


# Stability Guarantees After 1.0.0

Once ResumeSpec reaches:

1.0.0

the standard commits to long-term compatibility principles.


## Data Compatibility

Profiles created using a previous minor version should remain readable by newer implementations.

Example:

A profile created with:

ResumeSpec 1.2

should be processable by software supporting:

ResumeSpec 1.5


## Field Evolution Rules

The evolution of fields follows strict compatibility rules.


Adding Fields

Adding new optional fields is allowed in minor releases.

Example:

Before:

{
  "profile": {
    "name": "John Doe",
    "skills": []
  }
}

After:

{
  "profile": {
    "name": "John Doe",
    "skills": [],
    "availability": "open"
  }
}

This change is backward compatible.


Removing Fields

Removing existing fields is only allowed in major releases.

Deprecated fields should remain available during a transition period.


Changing Field Meaning

Changing the meaning of an existing field is considered a breaking change.

Example:

Version 1:

experience:
"Years working in the industry"

Version 2:

experience:
"Professional projects completed"

Although the field name remains the same, the meaning changed.

This requires a major version.


# Deprecation Policy

ResumeSpec may deprecate features when better alternatives become available.

A deprecated feature:

- Remains valid for a defined period.
- Is clearly documented.
- Includes migration guidance.
- May be removed only in a future major release.


Example:

ResumeSpec 1.x

Old field:

deprecated_field

Status:

Deprecated

Replacement:

new_field


# Schema Versioning

ResumeSpec schemas are versioned independently according to the specification version.

Example:

schemas/

v0/

profile.schema.json


v1/

profile.schema.json


Each schema version defines the validation rules for a specific ResumeSpec version.

Applications should validate documents against the schema version declared by the profile.


# Profile Version Declaration

Every ResumeSpec document should declare the specification version it follows.

Example:

{
  "resumeSpec": "1.0"
}


This allows tools to:

- Identify compatibility requirements.
- Validate documents correctly.
- Apply migrations when necessary.
- Provide meaningful compatibility errors.


# Migration Philosophy

ResumeSpec migrations should be:

- Explicit.
- Documented.
- Predictable.
- Automatable whenever possible.

A migration should transform a profile from one version to another without losing meaningful professional information.


Example:

ResumeSpec v1 Profile

        |

        v

Migration Process

        |

        v

ResumeSpec v2 Profile


The migration process should preserve:

- Professional history.
- Skills.
- Experience.
- Achievements.
- Relationships between entities.


# Backward and Forward Compatibility

ResumeSpec distinguishes between two compatibility concepts.


Backward Compatibility

A newer implementation can read older ResumeSpec documents.

Example:

Software supporting ResumeSpec 1.5 can read a ResumeSpec 1.2 profile.


Forward Compatibility

An older implementation can safely handle newer documents.

This is more limited and depends on whether new versions introduce unknown structures.

Implementations should ignore unknown optional fields whenever possible.


# Extension Compatibility

ResumeSpec may support extensions that allow organizations, communities, or industries to add specialized information.

Extensions must:

- Avoid changing the meaning of existing fields.
- Use unique namespaces.
- Remain optional.
- Document compatibility requirements.

Extensions should not create fragmentation of the core standard.


# Long-Term Compatibility Goal

ResumeSpec aims to preserve professional identity information across decades.

A profile created today should remain understandable by future systems.

The representation may evolve, but the professional history should remain portable.

Versioning exists to protect this principle.


# Future Considerations

As ResumeSpec grows, future versions may introduce:

- Compatibility matrices.
- Official migration tools.
- Version negotiation protocols.
- Extension registries.
- Automated migration systems.
- Community governance mechanisms.

These mechanisms will be defined through future RFC documents.


# Summary

ResumeSpec versioning provides a controlled evolution model:

Patch versions improve clarity without changing compatibility.

Minor versions expand capabilities without breaking existing profiles.

Major versions allow fundamental improvements while providing migration paths.

The objective is not only to evolve the format, but to guarantee that professional information remains portable, understandable, and valuable throughout the lifetime of the ecosystem.
