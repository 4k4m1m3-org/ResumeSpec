# ResumeSpec v1.0.0 Core Model

The Core Model defines the semantics of ResumeSpec v1.0.0. The JSON Schema is the executable contract for these definitions.

## Identity

Represents the person described by the profile.

Supported components:

- `person`: `givenName`, `familyName`, `preferredName`.
- `contact`: `email`, `phone`.
- `location`: `country`, `city`, `timeZone`.

## Summary

Represents a concise professional overview.

Required fields:

- `text`: string.

## Experience

Represents professional work history or comparable professional activity.

Supported fields:

- `position`: role or job title.
- `organization`: organization name.
- `dateRange`: start/end/current dates.
- `employmentType`: `full-time`, `part-time`, `contract`, `freelance`, `internship`, or `volunteer`.
- `workMode`: `remote`, `hybrid`, or `onsite`.
- `responsibilities`: array of strings.
- `achievements`: array of strings.
- `evidence`: array of Evidence objects.

## Education

Represents formal academic background.

ResumeSpec v1 uses:

- `institution`: organization that provided the education.
- `degree`: credential or study level, such as `Bachelor`.
- `fieldOfStudy`: academic area, such as `Computer Science`.
- `dateRange`
- `credential`
- `achievements`
- `evidence`

The fields `studyType` and `area` are not part of v1.

## Certifications

Represents professional certifications issued by an organization.

Supported fields:

- `name`
- `issuer`
- `credential`
- `dateRange`
- `identifier`
- `verificationUrl`

## Projects

Represents professional, academic, or personal projects.

ResumeSpec v1 uses `links`, an array of `Link` objects, for project URLs. A single scalar project `url` field is not part of v1.

Supported fields:

- `name`
- `description`
- `role`
- `organization`
- `technologies`
- `skills`
- `links`
- `results`
- `evidence`

## Skills And Technologies

`skills` represent capabilities. `technologies` represent tools, platforms, languages, or technical systems.

Skill levels:

- `beginner`
- `intermediate`
- `advanced`
- `expert`

## Languages

Represents human languages and proficiency.

Language levels:

- `basic`
- `intermediate`
- `advanced`
- `native`

## Other Sections

ResumeSpec v1 also defines:

- `courses`
- `publications`
- `awards`
- `volunteer`
- `references`
- `social`
- `links`
- `achievements`
- `interests`
- `attachments`

Their exact fields and reusable components are defined by the JSON Schema.

## Reusable Components

Core reusable components include:

- `Person`
- `Organization`
- `Position`
- `DateRange`
- `Contact`
- `Location`
- `Link`
- `Skill`
- `Technology`
- `Language`
- `Credential`
- `Identifier`
- `Evidence`

## Extensibility

Objects that allow extension fields accept properties named `x-*`.

Extensions are non-core data. They may be preserved by implementations, but they must not redefine core fields or be required for basic ResumeSpec interoperability.
