# ResumeSpec Tests

This directory contains the automated test suite for ResumeSpec implementations.

The purpose of these tests is to verify that ResumeSpec implementations correctly validate documents according to the official ResumeSpec JSON Schema.

These tests act as a compatibility layer between:

- ResumeSpec specification
- JSON Schema definitions
- Reference implementations


## Requirements

The current test suite is implemented in Python using pytest.

Install dependencies:

pip install -r implementations/python/requirements.txt


## Running Tests

Execute the test suite from the project root directory:

pytest

A successful execution should show:

============================== test session starts ==============================

tests/test_validation_result.py::test_validation_result_success PASSED
tests/test_validation_result.py::test_validation_result_failure PASSED
tests/test_validator.py::test_valid_document PASSED
tests/test_validator.py::test_invalid_document PASSED

============================== 4 passed ==============================


## Directory Structure

tests/
├── README.md
├── __init__.py
├── test_validator.py
├── test_validation_result.py
└── fixtures/
    ├── valid/
    │   └── minimal-profile.json
    │
    └── invalid/
        └── missing_version.json


## Fixtures

Fixtures are sample ResumeSpec documents used by the test suite.

They represent expected validation outcomes.


### valid/

Contains documents that must successfully pass ResumeSpec validation.

Example:

fixtures/valid/minimal-profile.json

This document represents the minimum required structure according to the ResumeSpec JSON Schema.


### invalid/

Contains documents that must fail validation.

Example:

fixtures/invalid/missing_version.json

These files ensure that required fields and schema constraints are correctly enforced.


## Current Test Coverage

The current suite validates:


### Document Validation

Tests the core validator behavior:

- Valid ResumeSpec documents are accepted.
- Invalid ResumeSpec documents are rejected.
- Schema validation errors are correctly reported.

Implemented in:

test_validator.py


### Machine-Readable Validation Results

Tests the structured validation response.

Successful validation returns:

{
  "valid": true,
  "errors": []
}


Failed validation returns:

{
  "valid": false,
  "errors": [
    "validation error message"
  ]
}


Implemented in:

test_validation_result.py


## Testing Principles

The test suite follows these principles:

- Test expected behavior, not internal implementation details.
- Keep fixtures simple and understandable.
- Ensure compatibility with the ResumeSpec specification.
- Detect schema changes that may introduce breaking behavior.
- Provide confidence before releasing new versions.


## Future Test Coverage

Future versions may include:

- Complete ResumeSpec profile examples.
- Validation of individual sections:

  - identity
  - summary
  - experience
  - skills
  - technologies
  - languages
  - links

- Schema version compatibility tests.
- CLI command tests.
- API integration tests.
- Cross-language implementation compatibility tests.
- Automated execution using GitHub Actions.


## Contributing

When adding new ResumeSpec features:

1. Update the JSON Schema.
2. Add or update fixtures.
3. Add corresponding tests.
4. Ensure all tests pass.

Run:

pytest

before submitting changes.


## Purpose

The ResumeSpec test suite ensures that implementations remain compatible with the specification as the project evolves.

A valid ResumeSpec document should behave consistently across different languages, tools, and platforms.
