# ResumeSpec JSON Schema

`resumespec.schema.json` is the canonical machine-readable contract for ResumeSpec v1.0.0.

The schema uses JSON Schema Draft 2020-12.

## Contract

Required root properties:

- `metadata`
- `sections`

Required metadata properties:

- `resumespecVersion`: exactly `1.0.0`
- `schemaVersion`: exactly `1.0.0`
- `language`

Individual sections are optional.

## Formats

- `metadata.created` and `metadata.updated` use JSON Schema `date`.
- Professional profile dates use `YYYY`, `YYYY-MM`, or `YYYY-MM-DD`.
- Links use HTTP or HTTPS URLs.
- Contact email uses JSON Schema `email`.

The Python validator applies `jsonschema.FormatChecker`.

## Unknown Fields And Extensions

Unknown fields are rejected by default with `additionalProperties: false`.

Extension fields are allowed only when their names start with `x-`.

This keeps the core v1 contract stable while allowing implementations to preserve non-core data.

## Validation

```bash
resumespec validate examples/json/minimal.json
```

Or directly from Python:

```python
from resumespec import validate_files

validate_files("examples/json/minimal.json")
```
