# Data Model

ResumeSpec documents are JSON objects with two required top-level properties:

- `metadata`
- `sections`

## Metadata

Required metadata fields:

- `resumespecVersion`
- `schemaVersion`
- `language`

Optional metadata fields:

- `profileVersion`
- `created`
- `updated`
- `visibility`
- `tags`
- `x-*`

## Sections

The `sections` object holds optional named sections. ResumeSpec v1.0.0 defines these section names:

- `identity`
- `summary`
- `experience`
- `education`
- `certifications`
- `courses`
- `skills`
- `technologies`
- `projects`
- `publications`
- `awards`
- `volunteer`
- `languages`
- `references`
- `social`
- `links`
- `achievements`
- `interests`
- `attachments`
- `x-*`

## Extensibility

Unknown core fields are rejected. Extensions use names that begin with `x-`.

## Dates And URLs

- Metadata dates use `YYYY-MM-DD`.
- Professional event dates use `YYYY`, `YYYY-MM`, or `YYYY-MM-DD`.
- URLs are validated as HTTP/HTTPS links through the schema.

