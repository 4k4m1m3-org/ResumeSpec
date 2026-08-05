# ResumeSpec Core Model

ResumeSpec defines a professional profile as a collection of reusable, interoperable and extensible building blocks.

Rather than representing a resume as a fixed document format, ResumeSpec separates professional information into independent concepts that can be combined, validated, extended and reused across different implementations.

The Core Model defines the conceptual foundation of the standard.

The model consists of four primary layers:

Resume
│
├── Metadata
├── Sections
├── Components
└── Types

Each layer has a specific responsibility within the specification.

---

# Metadata

Metadata describes the profile document itself rather than the professional information it contains.

Metadata allows implementations to identify, validate, manage and exchange ResumeSpec documents consistently.

Typical metadata includes:

- Identifier
- ResumeSpec version
- Schema version
- Schema URI
- Profile version
- Language
- Created date
- Updated date
- Author
- License
- Visibility
- Tags

Example concepts:

- ResumeSpec version defines the specification version used by the document.
- Schema version defines the validation schema version.
- Profile version defines the evolution of the individual profile.

Metadata enables compatibility between different ResumeSpec implementations.

---

# Sections

Sections represent the major categories of professional information contained in a ResumeSpec profile.

Each section is an independent conceptual unit.

Sections:

- May appear zero or more times depending on implementation requirements.
- May be extended through official or community extensions.
- Do not have a mandatory ordering.
- Should remain semantically independent.

The order of sections has no semantic meaning.

---

# Section Containers

Section Containers are a proposed extension to the current Sections model.

They introduce an optional structural layer for organizing Section entries and associated metadata.

Section Containers are not part of the stable Core Model yet.

Their definition and adoption are being evaluated through RFC-0002.

---

# Identity

Represents basic information about the person described by the profile.

Typical information includes:

- Name
- Preferred name
- Contact information
- Location
- Nationality
- Photo
- Professional identifiers

Identity references reusable Components such as:

- Person
- Contact
- Location
- Identifier

---

# Summary

Represents a professional overview of the profile.

Typical information includes:

- Professional summary
- Career objectives
- Areas of expertise
- Professional positioning

---

# Experience

Represents professional work history and employment experiences.

Experience is one of the core sections of ResumeSpec.

An Experience entry may contain:

- Position
- Organization
- DateRange
- EmploymentType
- WorkMode
- Location
- Responsibilities
- Achievements
- Skills used
- Technologies used
- Evidence

Experience should support different professional contexts including:

- Employment
- Contract work
- Freelance work
- Consulting
- Entrepreneurship
- Internships
- Volunteer professional activities

---

# Education

Represents academic and educational background.

Typical information includes:

- Institution
- Degree
- Field of study
- Period
- Achievements
- Evidence

Education references reusable Components such as:

- Organization
- DateRange
- Credential
- Evidence

---

# Credentials

Represents verifiable professional achievements related to learning, qualifications or recognition.

Credentials provide a unified concept for:

- Degrees
- Certifications
- Courses
- Licenses
- Digital badges
- Professional qualifications

This abstraction allows ResumeSpec to support modern credential ecosystems.

Credentials may include:

- Issuer
- Date obtained
- Expiration date
- Credential identifier
- Verification URL
- Evidence

---

# Certifications

Represents professional certifications issued by recognized organizations.

Typical information includes:

- Certification name
- Issuing organization
- Date obtained
- Expiration date
- Credential identifier
- Verification information

Certifications may reference the Credential component.

---

# Courses

Represents completed training programs and educational courses.

Typical information includes:

- Course name
- Provider
- Completion date
- Duration
- Skills acquired

Courses may reference the Credential component.

---

# Skills

Represents professional capabilities, knowledge areas and competencies.

A Skill represents a capability independent from specific tools or technologies.

Typical information includes:

- Skill name
- Skill level
- Years of experience
- Evidence
- Related technologies

Examples:

- Incident Management
- Leadership
- Network Security
- Project Management

Skills reference reusable Components such as:

- Skill
- Evidence

---

# Technologies

Represents specific technologies, platforms, tools and systems.

Technologies are different from Skills.

Example:

Skill:

Cybersecurity Operations

Related Technologies:

- Wazuh
- Suricata
- Linux
- Elastic

Technologies may include:

- Technology name
- Category
- Version
- Experience level
- Evidence

---

# Projects

Represents professional, academic or personal projects.

Typical information includes:

- Project name
- Description
- Role
- Technologies
- Skills
- Responsibilities
- Results
- Links
- Evidence

Projects allow profiles to represent practical experience beyond traditional employment.

---

# Publications

Represents published professional or academic materials.

Examples:

- Books
- Articles
- Research papers
- Technical blogs
- Documentation

Typical information includes:

- Title
- Publication date
- Publisher
- URL
- Authors

---

# Awards

Represents professional or academic recognitions.

Typical information includes:

- Award name
- Issuing organization
- Date
- Description
- Evidence

---

# Volunteer

Represents volunteer activities and community contributions.

Typical information includes:

- Organization
- Role
- Period
- Contributions
- Achievements

---

# Languages

Represents spoken and written languages.

Typical information includes:

- Language
- Proficiency level
- Certification
- Evidence

Languages reference reusable Components such as:

- Language

---

# References

Represents professional references.

Typical information includes:

- Person
- Organization
- Relationship
- Contact information

References use reusable Components:

- Person
- Organization
- Contact

---

# Social

Represents professional social profiles.

Examples:

- LinkedIn
- GitHub
- ORCID
- Personal websites

Social profiles reference:

- Link
- Identifier

---

# Links

Represents external resources associated with the profile.

Examples:

- Portfolio
- Personal website
- Repository
- Publications

Links use the reusable Link component.

---

# Achievements

Represents measurable professional accomplishments.

Typical information includes:

- Achievement title
- Description
- Impact
- Metrics
- Evidence

Achievements may appear inside:

- Experience
- Projects
- Education
- Volunteer

---

# Interests

Represents professional areas of interest.

Examples:

- Research areas
- Technology interests
- Professional communities

---

# Attachments

Represents files associated with the profile.

Examples:

- Certificates
- Documents
- Portfolios
- Evidence files

Attachments reference the Attachment component.

---

# Components

Components are reusable structures shared across multiple sections.

A Component represents a single reusable concept that should not be duplicated throughout the specification.

Components define entities and objects used by Sections.

---

# Person

Represents an individual.

Used by:

- Identity
- References
- Awards
- Volunteer

---

# Organization

Represents an organization.

Used by:

- Experience
- Education
- Certifications
- Projects
- Awards
- Volunteer

---

# Position

Represents a professional role or job position.

Typical information:

- Title
- Level
- Responsibilities

Used by:

- Experience

---

# DateRange

Represents a period of time.

Typical information:

- Start date
- End date
- Current status

---

# Contact

Represents contact information.

Typical information:

- Email
- Phone
- Address
- Communication channels

---

# Location

Represents a geographical location.

Typical information:

- Country
- Region
- City
- Time zone

---

# Link

Represents an external resource.

Typical information:

- URL
- Type
- Description

---

# Attachment

Represents an associated file.

Typical information:

- File name
- File type
- URL
- Description

---

# Skill

Represents a professional capability.

Typical information:

- Name
- Level
- Category
- Evidence

---

# Technology

Represents a technology, platform or tool.

Typical information:

- Name
- Category
- Version
- Experience level

---

# Language

Represents a spoken or written language.

Typical information:

- Language name
- Proficiency level

---

# Identifier

Represents an identifier issued by an external organization.

Examples:

- Certification ID
- ORCID ID
- Professional registration number

---

# Credential

Represents a verifiable qualification or achievement.

Typical information:

- Issuer
- Credential ID
- Issue date
- Expiration date
- Verification URL

---

# Evidence

Represents verifiable information supporting a profile element.

Examples:

- Documents
- Links
- References
- Measurements
- External verification

Evidence improves trust and interoperability.

---

# Types

Types define controlled values shared across the specification.

Unlike Components, Types do not represent entities.

Types define standardized value sets.

Examples include:

- EmploymentType
- WorkMode
- SeniorityLevel
- SkillLevel
- LanguageLevel
- EducationLevel
- DegreeType
- Currency
- CountryCode
- TimeZone
- LicenseType
- Visibility
- ProficiencyScale

Using shared Types guarantees consistency across implementations.

Example:

Every Experience section should use the same EmploymentType values defined by the specification.

---

# Relationships

The conceptual model is organized as follows:

Layer | Purpose

Metadata | Describes the profile document itself

Sections | Organize professional information

Components | Define reusable entities

Types | Define reusable controlled values

---

# Extensibility

ResumeSpec is designed to evolve without breaking existing implementations.

Implementations may introduce:

- New Sections
- New Components
- New Types

Extensions should follow the compatibility rules defined by the specification.

Official and community extensions should maintain clear namespaces.

---

# Compatibility

ResumeSpec implementations should ignore unknown Sections, Components and Types whenever possible.

This allows newer versions of the specification to coexist with older implementations.

Backward compatibility is a core design principle of ResumeSpec.

---

# Implementation

This document defines the conceptual model of ResumeSpec.

The exact data representation of Metadata, Sections, Components and Types is defined by the official schemas.

The JSON Schema, XML Schema and YAML Schema specifications provide machine-readable validation rules based on this Core Model.
