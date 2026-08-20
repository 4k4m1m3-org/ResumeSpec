# Changelog

All notable changes to ResumeSpec are documented here.

## [1.0.0] - 2026-08-20

### Added

- Stable ResumeSpec v1.0.0 JSON Schema contract.
- Canonical JSON format declaration.
- Minimal, realistic, invalid, and extension reference examples.
- Python reference parser, validator, and CLI.
- CLI validation using the official schema by default.
- Parser support for JSON, secondary YAML, and experimental XML.
- Tests covering schema contract, examples, validator, parser, CLI, packaging schema copy, and format validation.

### Changed

- Aligned specification, schema, examples, tests, documentation, package metadata, and `VERSION` on `1.0.0`.
- Closed unknown core fields with `additionalProperties: false`.
- Preserved extensibility through `x-*` fields.
- Standardized projects on `links` instead of scalar `url`.
- Standardized education on `degree` and `fieldOfStudy`.
- Documented the authority order: spec, schema, examples, tests, implementation.

### Security

- XML parsing in the Python reference implementation uses `defusedxml`.

### Compatibility

- JSON is the only normative v1 format.
- YAML and XML remain implementation-supported, non-normative formats.

## [0.2.0] - 2026-08-06

### Added

- Initial specification draft.
- Initial JSON Schema.
- Initial examples and validation tests.
- Early Python validator work.

## [0.1.0] - 2026-07-26

### Added

- Initial repository structure.
- Project vision, governance, contribution, and licensing documents.
