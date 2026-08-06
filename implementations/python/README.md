# ResumeSpec Python Implementation

Reference Python implementation for the ResumeSpec standard.

This package provides tools to validate ResumeSpec documents against the official JSON Schema definition.

The goal of this implementation is to provide a simple, reliable and extensible validator that can be used by developers, automation tools, and future ResumeSpec applications.

---

## Overview

ResumeSpec defines a machine-readable format for representing professional profiles, resumes and career information.

This Python implementation provides:

- JSON document validation.
- JSON Schema compatibility.
- Command-line validation.
- Reusable validation functions.
- Structured validation results.

The validator uses the official ResumeSpec JSON Schema as the source of truth.

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

```bash
git clone https://github.com/4k4m1m3/ResumeSpec.git

cd ResumeSpec/implementations/python
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Command Line Interface

Validate any ResumeSpec document:

```bash
python cli.py \
path/to/profile.json \
path/to/resumespec.schema.json
```

Example using a reference profile:

```bash
python cli.py \
../../examples/json/developer.json \
../../schemas/json/resumespec.schema.json
```

Successful validation:

```text
✓ ResumeSpec document is valid
```

Invalid document example:

```text
✗ ResumeSpec validation failed

- sections.identity: required property missing
```

---

## Reference Examples

The implementation can validate any official ResumeSpec example.

Available examples:

| File                 | Purpose                                                      |
| -------------------- | ------------------------------------------------------------ |
| `minimal.json`       | Minimal valid professional profile                           |
| `developer.json`     | Software development, technologies, projects and open source |
| `cybersecurity.json` | Cybersecurity, security operations and defensive practices   |
| `it-operations.json` | Infrastructure, systems administration and IT operations     |
| `student.json`       | Education, learning path and early career profiles           |

Example:

```bash
python cli.py \
../../examples/json/cybersecurity.json \
../../schemas/json/resumespec.schema.json
```

---

## JSON Output

The CLI can return machine-readable JSON output:

```bash
python cli.py profile.json resumespec.schema.json --json
```

Example:

```json
{
  "valid": true,
  "errors": []
}
```

This mode is useful for:

* CI/CD pipelines.
* Web applications.
* API integrations.
* Automated testing.

---

## Python API

The validator can also be used directly from Python code.

Example:

```python
from validator import validate_files

validate_files(
    "profile.json",
    "resumespec.schema.json"
)
```

For structured validation results:

```python
from validator import get_validation_result

result = get_validation_result(
    "profile.json",
    "resumespec.schema.json"
)

if result["valid"]:
    print("Valid")
else:
    print(result["errors"])
```

---

## Project Structure

```text
python/
├── validator.py
│   Core ResumeSpec validation engine.
│
├── cli.py
│   Command-line interface.
│
├── requirements.txt
│   Python dependencies.
│
├── tests/
│   Automated validation tests.
│
└── README.md
    Implementation documentation.
```

---

## Design Principles

### Schema First

The JSON Schema is the source of truth.

The validator does not duplicate ResumeSpec rules internally.

All structural validation rules must exist in:

```text
schemas/json/resumespec.schema.json
```

---

### Separation of Concerns

Validation logic and user interfaces are separated.

Architecture:

```text
cli.py

   |

   v

validator.py

   |

   v

JSON Schema
```

This allows future integrations such as:

* Web APIs.
* Resume builders.
* Browser applications.
* Other programming languages.

---

## Standard Compatibility

Current compatibility:

* JSON Schema Draft 2020-12.

This ensures compatibility with modern validation tools and libraries.

---

## Development

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

Manual validation:

```bash
python cli.py example.json schema.json
```

---

## Roadmap

Future improvements may include:

* Package distribution through PyPI.
* Official `resumespec` command-line tool.
* Schema version detection.
* Improved validation messages.
* JSON/YAML support.
* Integration tests.
* JavaScript/TypeScript implementation.

---

## Relationship With ResumeSpec

This implementation is part of the ResumeSpec ecosystem.

The Python implementation is not the specification itself.

The relationship is:

```text
ResumeSpec Standard

├── spec/
│
├── schemas/
│
└── implementations/
    │
    └── python/
```

The standard lives in:

* Specification documents.
* Schema definitions.

Implementations provide tools that consume and validate ResumeSpec documents.

---

## License

This project follows the license defined in the root ResumeSpec repository.

---

## Status

Current status:

**Experimental reference implementation**

The API and internal structure may evolve until ResumeSpec reaches a stable specification version.
