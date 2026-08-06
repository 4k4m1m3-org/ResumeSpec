# RFC-0002: Section Containers

**Status:** Accepted

**Author:** Wuilmer Bolívar

**Created:** 2026-08-05

## Summary

This RFC proposes introducing reusable Section Containers as an additional structural concept within ResumeSpec.

Section Containers propose a standardized way to organize and group information represented by existing Sections.

This proposal does not replace existing Sections or Components. It introduces an additional structural layer that may improve extensibility, presentation control, and interoperability between different implementations.

---

# Scope

This RFC covers the introduction of Section Containers as a structural concept.

This RFC does not define:

- Mandatory adoption of Section Containers
- Migration requirements
- Changes to existing ResumeSpec documents
- Replacement of current Section entities

---

# Motivation

ResumeSpec Sections currently represent conceptual categories of professional information.

Examples:

- Experience
- Skills
- Technologies
- Languages
- Links

These concepts define what type of professional information is represented inside a profile.

However, implementations may require additional structure around these categories, including:

- Custom section titles
- Grouping related entries
- Presentation metadata
- Reusable organization patterns
- Multiple representations of the same information

Without a dedicated structural model, implementations may create incompatible approaches for organizing the same professional information.

---

# Problem Statement

The current model represents Sections directly as collections of entities.

Example:

```text
Profile
└── Sections
    └── Experience
        └── Experience entries
```

This approach is simple and compatible, but it does not define a reusable structure for the Section itself.

Different implementations may introduce their own custom wrappers, creating interoperability problems.

---

# Proposal

This RFC proposes introducing the concept of Section Containers.

A Section Container represents a reusable structural definition that organizes one or more entries belonging to a specific Section.

Example proposed model:

```text
Profile
└── Sections
    └── ExperienceSection
        └── Experience entries
```

Proposed Initial Section Containers:

* ExperienceSection
* SkillSection
* TechnologySection
* LanguageSection
* LinkSection

Section Containers may provide:

* A section title
* A description
* A collection of related entries
* Future extensible metadata

---

# Relationship With Existing Concepts

Section Containers do not replace existing ResumeSpec concepts.

The relationship between concepts is:

```text
Section
 |
 └── Section Container
       |
       └── Entity entries
```

Examples:

```text
Experience
 |
 └── ExperienceSection
       |
       └── Experience
```

```text
Skills
 |
 └── SkillSection
       |
       └── Skill
```

Existing entities remain valid and reusable independently.

---

# Compatibility Considerations

This proposal is designed to preserve compatibility.

Existing ResumeSpec documents should continue to represent professional information using current Sections and entities.

Section Containers should initially be considered an optional structural enhancement.

Migration requirements should be defined only after practical implementation experience is collected.

---

# Alternatives Considered

## Keep Sections as Direct Collections

Example:

```text
Sections
└── Experience
    └── Experience[]
```

Advantages:

* Simple model
* Easy validation
* Minimal complexity

Disadvantages:

* Limited extensibility
* No standardized place for section metadata
* Different implementations may create incompatible structures

## Introduce a Generic Section Object

Example:

```text
Section
├── type
├── title
└── items
```

Rejected for now because typed containers provide clearer validation and stronger interoperability.

## Replace Sections Immediately

Rejected because ResumeSpec v1 establishes compatibility expectations and existing implementations should not require immediate migration.

---

# Open Questions

The following topics require further discussion:

* Should Section Containers become mandatory in a future ResumeSpec version?
* Should both direct Sections and Section Containers coexist permanently?
* Should Section Containers support ordering metadata?
* Should Section Containers include presentation-specific information?
* How should migration from existing Section structures be handled?
* Should additional Section Containers be introduced?

---

# Implementation Impact

If accepted, this proposal may require updates to:

* JSON Schema definitions
* Reference examples
* Specification documentation
* Validation rules
* Reference implementations

No implementation changes are introduced by this RFC.

Section Containers are accepted as an architectural extension and may be implemented in future schema versions.

# Implementation Status

Accepted as an architectural extension.

Section Containers are not required in ResumeSpec v1 documents.

Existing ResumeSpec documents continue using direct Sections and remain compatible.

Future schema versions may introduce optional Section Container support based on implementation experience.
