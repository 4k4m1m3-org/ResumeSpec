# ResumeSpec Tests

The test suite verifies ResumeSpec v1.0.0 conformance across schema, examples, validator, parser, CLI, and packaging metadata.

## Run

From the repository root:

```bash
python -m pytest
```

For a clean local setup:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e "implementations/python[dev]"
python -m pytest
```

## Coverage

- JSON Schema Draft 2020-12 validity.
- Minimal and realistic valid documents.
- Required properties.
- Type constraints.
- Enum constraints.
- Unknown field rejection.
- Email, date, and URL validation.
- `x-*` extensibility.
- Valid and invalid examples.
- Validator success and failure behavior.
- Parser support for JSON, secondary YAML, and experimental XML.
- CLI exit codes for valid and invalid documents.
- Packaged schema copy matching the repository schema.

Tests are part of the release gate. Do not mark a v1 release ready while related tests fail.
