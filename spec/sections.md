# ResumeSpec Sections

Sections define the official categories of information that can be represented inside a ResumeSpec profile.

A Section represents a specific area of a person's professional identity, experience, knowledge or achievements.

Sections are independent and optional. A profile does not need to contain every available section.

Implementations may support all sections or only a subset depending on their purpose.

---

# Section Principles

ResumeSpec Sections follow these principles:

- Sections represent meaningful professional concepts.
- Sections should remain focused on a single domain of information.
- Sections may evolve independently across versions.
- Unknown sections should be ignored by implementations when possible.
- The order of sections has no semantic meaning.
- Sections should not duplicate information already represented by reusable Components or Types.

---

# Official Sections

## Identity

Represents the basic identity information of a person.

Possible information:

- Full name
- Preferred name
- Contact information
- Location
- Profile image
- Nationality
- Personal identifiers

Common Components:

- Person
- Contact
- Location

---

## Summary

Represents a high-level professional overview.

Possible information:

- Professional introduction
- Career summary
- Areas of expertise
- Professional goals
- Industry focus

---

## Experience

Represents professional work experience.

Possible information:

- Position or role
- Organization
- Employment period
- Responsibilities
- Achievements
- Technologies used
- Work environment
- Evidence

Common Components:

- Organization
- DateRange
- Location
- Technology
- Evidence

---

## Education

Represents formal academic background.

Possible information:

- Institution
- Degree
- Field of study
- Academic level
- Dates
- Achievements
- Certifications obtained

Common Components:

- Organization
- DateRange
- Evidence

---

## Certifications

Represents professional certifications issued by recognized organizations.

Possible information:

- Certification name
- Issuing organization
- Credential identifier
- Verification URL
- Issue date
- Expiration date

Common Components:

- Organization
- Identifier
- Link
- DateRange

---

## Courses

Represents completed learning activities.

Possible information:

- Course name
- Provider
- Instructor
- Duration
- Completion date
- Certificate

Common Components:

- Organization
- DateRange
- Attachment

---

## Skills

Represents professional capabilities and competencies.

Possible information:

- Skill name
- Category
- Proficiency level
- Years of experience
- Related evidence

Common Components:

- Skill
- Evidence

---

## Technologies

Represents specific tools, platforms and technologies.

Possible information:

- Technology name
- Category
- Experience level
- Usage context

Examples:

- Programming languages
- Operating systems
- Cloud platforms
- Security tools
- Databases
- Frameworks

Common Components:

- Technology

---

## Projects

Represents personal, professional or open-source projects.

Possible information:

- Project name
- Description
- Role
- Organization
- Technologies
- Repository
- Website
- Results
- Evidence

Common Components:

- Organization
- Technology
- Link
- Evidence

---

## Publications

Represents published content.

Possible information:

- Articles
- Books
- Research papers
- Blog posts
- Videos
- Podcasts

Common Components:

- Link
- Organization
- DateRange

---

## Awards

Represents professional awards and recognitions.

Possible information:

- Award name
- Issuing organization
- Date
- Description
- Evidence

Common Components:

- Organization
- DateRange
- Evidence

---

## Volunteer

Represents volunteer activities and community contributions.

Possible information:

- Organization
- Role
- Activities
- Duration
- Achievements

Common Components:

- Organization
- DateRange
- Evidence

---

## Languages

Represents spoken and written languages.

Possible information:

- Language name
- Proficiency level
- Certification
- Native language indicator

Common Components:

- Language
- Evidence

---

## References

Represents professional references.

Possible information:

- Person
- Organization
- Relationship
- Contact information
- Recommendation

Common Components:

- Person
- Organization
- Contact

---

## Social

Represents public professional profiles.

Possible information:

- Platform
- Username
- Profile URL

Examples:

- GitHub
- LinkedIn
- Personal website

Common Components:

- Link

---

## Links

Represents relevant external resources.

Possible information:

- Portfolio
- Documentation
- Demo
- Repository
- Presentation
- Media

Common Components:

- Link

---

## Achievements

Represents measurable professional accomplishments.

Possible information:

- Achievement description
- Impact
- Metrics
- Context
- Evidence

Common Components:

- Evidence
- DateRange

---

## Interests

Represents professional interests and areas of exploration.

Possible information:

- Research areas
- Technologies of interest
- Professional communities
- Topics

---

## Attachments

Represents files associated with the profile.

Possible information:

- File name
- File type
- Description
- Location
- Verification information

Common Components:

- Attachment

---

# Extension Sections

ResumeSpec allows future sections to be introduced as the ecosystem evolves.

Examples:

- OpenSourceContributions
- Research
- Patents
- Speaking
- Conferences
- Grants
- Licenses
- SecurityClearances

New sections should:

- Follow the ResumeSpec model.
- Avoid duplicating existing concepts.
- Use existing Components and Types whenever possible.
- Maintain backward compatibility.

---

# Custom Sections

Organizations may define custom sections for internal or specialized use cases.

Examples:

- InternalTraining
- CustomerProjects
- CompanyAchievements
- GovernmentRequirements

Custom sections are not considered part of the official ResumeSpec specification unless adopted through the RFC process.

---

# Implementation Notes

This document defines the official section catalog of ResumeSpec.

The internal structure of each section is defined using:

- Components
- Types
- JSON Schemas

The JSON representation of sections is maintained separately from this conceptual documentation.
