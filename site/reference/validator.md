# Validator

The validator checks documents against the official ResumeSpec JSON Schema.

## API

- `load_schema(path=None)`
- `validate_resume(resume_data, schema=None)`
- `validate_files(resume_file, schema_file=None)`
- `get_validation_result(resume_file, schema_file=None)`

## Behavior

- Uses the official schema by default.
- Applies `jsonschema.FormatChecker`.
- Produces deterministic, human-readable validation errors.
- Does not add semantic rules that contradict the schema.

