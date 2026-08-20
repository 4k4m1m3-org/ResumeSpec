# ResumeSpec Python Reference Implementation

Reference parser, validator, and CLI for ResumeSpec v1.0.0.

The implementation follows the official JSON Schema. It does not define the standard.

## Install

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e "implementations/python[dev]"
```

## CLI

Validate using the official schema:

```bash
resumespec validate examples/json/minimal.json
```

Validate with JSON output:

```bash
resumespec validate examples/json/minimal.json --json
```

Parse a document:

```bash
resumespec parse examples/json/minimal.json --json
```

Exit codes:

- `0`: valid document or successful parse.
- `1`: validation failed.
- `2`: CLI usage error or parse failure.

## Format Support

- JSON: canonical v1 format.
- YAML: secondary implementation format.
- XML: experimental implementation format parsed with `defusedxml`.

Parsing is not validation.

## Python API

```python
from resumespec import parse, validate_files, validate_resume

validate_files("examples/json/minimal.json")

profile = parse("examples/json/minimal.json")
validate_resume(profile.data)
```

Machine-readable validation result:

```python
from resumespec import get_validation_result

result = get_validation_result("examples/json/minimal.json")
```

The public API intentionally stays small:

- `parse`
- `parse_data`
- `parse_yaml`
- `parse_xml`
- `validate_files`
- `validate_resume`
- `get_validation_result`
- `load_schema`
- `get_default_schema_path`
- `ResumeProfile`
- `ResumeSpecParseError`
- `ResumeSpecValidationError`
