# ResumeSpec

**One professional identity. Unlimited representations.**

ResumeSpec is an open standard for representing a professional identity as structured, portable, machine-readable data.

ResumeSpec v1.0.0 defines the information model, semantics, JSON Schema contract, validation behavior, reference examples, and a small Python reference implementation.

It does not define visual CV design, PDF generation, portfolio generation, ATS scoring, AI features, exporters, platform integrations, or multi-language SDKs. Those are post-v1 implementation concerns.

## Status

Current stable version: **1.0.0**

Canonical format: **JSON**

Secondary implementation formats: **YAML and XML parsing are supported by the Python reference implementation, but they are not normative v1 formats.**

## Source Of Truth

ResumeSpec v1 uses this authority order:

1. `spec/` defines normative semantics.
2. `schemas/json/resumespec.schema.json` defines the machine-readable v1 contract.
3. `examples/` show conforming and intentionally invalid documents.
4. `tests/` verify conformance.
5. `implementations/python/` implements the standard.

Code does not define the standard. Examples must not introduce fields that the schema does not define.

## Minimal JSON Document

```json
{
  "metadata": {
    "resumespecVersion": "1.0.0",
    "schemaVersion": "1.0.0",
    "language": "en"
  },
  "sections": {
    "summary": {
      "text": "IT Operations professional."
    },
    "skills": [
      {
        "name": "Linux"
      }
    ]
  }
}
```

## Install The Python Reference Implementation

From a clean checkout:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e "implementations/python[dev]"
```

## Validate A Document

Use the official schema by default:

```bash
resumespec validate examples/json/minimal.json
```

Machine-readable validation result:

```bash
resumespec validate examples/json/minimal.json --json
```

Validate with an explicit schema path:

```bash
resumespec validate examples/json/minimal.json --schema schemas/json/resumespec.schema.json
```

Exit codes:

- `0`: valid document or successful parse.
- `1`: validation failed.
- `2`: CLI usage error or parse failure.

## Parse A Document

Parsing loads a document. It does not validate it.

```bash
resumespec parse examples/json/minimal.json --json
```

Supported parser inputs:

- JSON: canonical v1 format.
- YAML: secondary implementation format.
- XML: experimental implementation format, parsed with `defusedxml`.

## Examples

- `examples/json/minimal.json`: minimal valid profile.
- `examples/json/developer.json`: realistic complete profile.
- `examples/json/edge-extension.json`: valid `x-*` extension example.
- `examples/json/invalid-unknown-field.json`: intentionally invalid document.
- `examples/yaml/minimal.yaml`: secondary YAML representation.
- `examples/xml/minimal.xml`: experimental XML representation.

## Extensibility

ResumeSpec v1 rejects unknown core fields by default. Extension fields are allowed only when their names start with `x-`.

This preserves interoperability while allowing implementations to carry non-core data without redefining ResumeSpec semantics.

## Development Checks

```bash
python -m pytest
git diff --check
```

## Roadmap

ResumeSpec v1.0.0 closes the small stable core. Future work may include a documentation website, additional SDKs, generators, exporters, ATS integrations, scoring, AI features, XSD, and a complete extension registry, but those are outside v1.
