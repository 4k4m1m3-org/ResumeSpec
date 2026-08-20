# ResumeSpec v1.0.0 Structure

ResumeSpec represents one professional identity as structured data.

## Root Object

The root object requires:

- `metadata`: document metadata.
- `sections`: professional information sections.

No other root properties are allowed unless they use the `x-` extension prefix.

## Metadata

Required metadata:

- `resumespecVersion`: string, exactly `1.0.0`.
- `schemaVersion`: string, exactly `1.0.0`.
- `language`: string, BCP 47 style language tag.

Optional metadata:

- `profileVersion`: string.
- `created`: full date, `YYYY-MM-DD`.
- `updated`: full date, `YYYY-MM-DD`.
- `visibility`: one of `public`, `private`, `restricted`.
- `tags`: array of unique strings.
- `x-*`: extension fields.

Metadata describes the document and processing context. It is not a professional section.

## Sections

`sections` is an object with named optional sections:

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
- `x-*` extension sections

Section ordering has no semantic meaning.

## Dates

Metadata dates use full JSON Schema `date` values: `YYYY-MM-DD`.

Professional event dates use `ProfileDate`, which allows:

- `YYYY`
- `YYYY-MM`
- `YYYY-MM-DD`

This supports common resume precision without requiring false day-level accuracy.

## URLs

URLs are represented through the reusable `Link` component. A `Link` requires `url` and may include `type` and `description`.

ResumeSpec v1 links are HTTP or HTTPS URLs validated by the JSON Schema.

## Unknown Fields

Unknown fields are invalid unless their names start with `x-`.

This rule keeps the v1 contract interoperable while allowing implementations to preserve non-core data.

## Section Containers

Section Containers remain an RFC concept and are not required by ResumeSpec v1.0.0.
