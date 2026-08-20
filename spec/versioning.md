# ResumeSpec Versioning

ResumeSpec follows Semantic Versioning:

`MAJOR.MINOR.PATCH`

Current stable release: **1.0.0**

## Version Fields

ResumeSpec v1.0.0 documents must include:

```json
{
  "metadata": {
    "resumespecVersion": "1.0.0",
    "schemaVersion": "1.0.0",
    "language": "en"
  },
  "sections": {}
}
```

- `resumespecVersion` identifies the specification version.
- `schemaVersion` identifies the JSON Schema contract version.
- `profileVersion` may identify the version of an individual profile and is controlled by the document owner.

For v1.0.0, `resumespecVersion` and `schemaVersion` are both exactly `1.0.0`.

## Schema Identity

The v1.0.0 JSON Schema uses this `$id`:

`https://resumespec.org/schemas/json/v1.0.0/resumespec.schema.json`

## Python Package Version

The Python reference implementation is released as `1.0.0` with the v1.0.0 specification. Future implementation patch releases may update code or packaging without changing the standard, but any such release must document the relationship clearly.

## Compatibility Rules

Patch releases may clarify documentation, fix examples, improve tests, or improve implementation behavior without changing the document contract.

Minor releases may add optional fields or sections while preserving the meaning of existing v1 fields.

Major releases may introduce breaking changes and require migration guidance.

## Extension Compatibility

Extensions use `x-*` fields. Implementations may preserve extension data, but extension fields are not part of the core v1 contract and must not be required for core interoperability.
