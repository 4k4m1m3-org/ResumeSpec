# ResumeSpec Python Implementation

Reference Python implementation for the ResumeSpec standard.

This package provides tools to validate ResumeSpec documents against the official JSON Schema definition.

The goal of this implementation is to provide a simple, reliable and extensible validator that can be used by developers, automation tools, and future ResumeSpec applications.

---

## Overview

ResumeSpec defines a machine-readable standard for representing professional profiles, resumes and career information.

This Python implementation provides:

- JSON document validation.
- JSON Schema compatibility.
- Command-line validation.
- Reusable validation functions.
- Structured validation results.

The validation engine is based on the official JSON Schema specification.

---

## Requirements

- Python 3.12+
- pip
- virtual environment support

Dependencies:

- jsonschema

---

## Installation

Clone the repository:

git clone https://github.com/4k4m1m3/ResumeSpec.git

cd ResumeSpec/implementations/python


Create a virtual environment:

python -m venv .venv


Activate the environment:

Linux/macOS:

source .venv/bin/activate


Windows:

.venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt

---

## Usage

## Command Line Interface

Validate a ResumeSpec document:

python cli.py <resume.json> <schema.json>


Example:

python cli.py ../../examples/json/minimal.json ../../schemas/json/resumespec.schema.json


Successful validation:

✓ ResumeSpec document is valid


Invalid document example:

✗ ResumeSpec validation failed

- basics.name: 'name' is a required property

---

## JSON Output

The CLI can also return machine-readable JSON output:

python cli.py profile.json resumespec.schema.json --json


Example:

{
  "valid": true,
  "errors": []
}


This mode is useful for:

- CI/CD pipelines.
- Web applications.
- API integrations.
- Automated testing.

---

## Python API

The validator can also be used directly from Python code.

Example:

from validator import validate_files

validate_files(
    "profile.json",
    "resumespec.schema.json"
)

print("Valid ResumeSpec document")


For structured results:

from validator import get_validation_result


result = get_validation_result(
    "profile.json",
    "resumespec.schema.json"
)

if result["valid"]:
    print("Valid")
else:
    print(result["errors"])

---

## Project Structure

python/
|
├── validator.py
|   Core ResumeSpec validation engine.
|
├── cli.py
|   Command-line interface.
|
├── requirements.txt
|   Python dependencies.
|
├── tests/
|   Automated validation tests.
|
└── README.md
    Implementation documentation.

---

## Design Principles

This implementation follows these principles:

## Schema First

The JSON Schema is the source of truth.

The validator does not define ResumeSpec rules internally.

All structural rules must exist in the official schema.

---

## Separation of Concerns

Validation logic and user interfaces are separated.

Architecture:

cli.py

    |

    v

validator.py

    |

    v

JSON Schema


This allows future integrations such as:

- Web APIs.
- Resume builders.
- Browser applications.
- Other programming languages.

---

## Standard Compatibility

The implementation uses:

- JSON Schema Draft 2020-12.

This ensures compatibility with modern validators and tooling.

---

## Development

Install dependencies:

pip install -r requirements.txt


Run validation manually:

python cli.py example.json schema.json


Run tests:

pytest

---

## Roadmap

Future improvements may include:

- Package distribution through PyPI.
- Official resumespec command.
- Schema version detection.
- Improved validation messages.
- JSON/YAML support.
- Integration tests.
- JavaScript/TypeScript equivalent implementation.

---

## Relationship With ResumeSpec

This repository contains the standard definition and reference implementations.

The Python implementation is not the standard itself.

The relationship is:

ResumeSpec Standard

    |

    +-- spec/

    |

    +-- schemas/

    |

    +-- implementations/

            |

            +-- python/


The standard lives in the specification and schema files.

Implementations provide tools to consume and validate that standard.

---

## License

This project follows the license defined in the root ResumeSpec repository.

---

## Status

Current status:

Experimental reference implementation.

The API and internal structure may evolve until ResumeSpec reaches a stable specification version.
