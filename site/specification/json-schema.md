# JSON Schema

The canonical machine-readable contract for ResumeSpec v1.0.0 is:

[`schemas/json/resumespec.schema.json`](https://github.com/4k4m1m3-org/ResumeSpec/blob/v1.0.0/schemas/json/resumespec.schema.json)

## What The Schema Does

- requires `metadata` and `sections`
- fixes `resumespecVersion` and `schemaVersion` to `1.0.0`
- validates fields, types, enums, dates, emails, and URLs
- rejects unknown core fields
- allows `x-*` extension fields

## Why This Matters

The schema is the executable form of the standard. A document that does not satisfy the schema is not conformant v1.0.0 data.

## Examples

- [Minimal valid example](https://github.com/4k4m1m3-org/ResumeSpec/blob/v1.0.0/examples/json/minimal.json)
- [Realistic example](https://github.com/4k4m1m3-org/ResumeSpec/blob/v1.0.0/examples/json/developer.json)
- [Invalid example](https://github.com/4k4m1m3-org/ResumeSpec/blob/v1.0.0/examples/json/invalid-unknown-field.json)
