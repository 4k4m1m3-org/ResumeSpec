# Getting Started

This guide explains how to start working with ResumeSpec, create a profile document and validate it against the official schema.

## Overview

ResumeSpec defines a structured format for representing professional profiles using a machine-readable document.

A ResumeSpec profile can describe different professional scenarios, including software development, cybersecurity, IT operations, education and other career paths.

## Repository Structure

The main components of the repository are:

```text
examples/
├── json/
│   ├── minimal.json
│   ├── developer.json
│   ├── cybersecurity.json
│   ├── it-operations.json
│   └── student.json

schemas/
└── json/
    └── resumespec.schema.json
```

* `examples/` contains reference profiles demonstrating ResumeSpec usage.
* `schemas/` contains validation schemas.
* `spec/` contains the formal specification documentation.

## Reference Examples

ResumeSpec provides reference profiles demonstrating different professional scenarios.

| File                 | Purpose                                                      |
| -------------------- | ------------------------------------------------------------ |
| `minimal.json`       | Minimal valid professional profile                           |
| `developer.json`     | Software development, technologies, projects and open source |
| `cybersecurity.json` | Cybersecurity, security operations and defensive practices   |
| `it-operations.json` | Infrastructure, systems administration and IT operations     |
| `student.json`       | Education, learning path and early career profiles           |

These examples are intended to demonstrate ResumeSpec capabilities. They use demonstration data and should be adapted for real professional profiles.

## Creating a Profile

The recommended approach is to start from an existing example and adapt it to your needs.

For example:

```bash
cp examples/json/minimal.json my-profile.json
```

Then update the document with your own information while keeping the ResumeSpec structure.

## Validating a Profile

A ResumeSpec document can be validated against the official JSON Schema.

Example:

```bash
python implementations/python/cli.py \
examples/json/minimal.json \
schemas/json/resumespec.schema.json
```

A valid document should return:

```text
✓ ResumeSpec document is valid
```

## Next Steps

After creating and validating a profile, explore:

* The specification documentation in `spec/`
* JSON schema definitions in `schemas/json/`
* Serialization formats in `serializations/`
* Community and official extensions in `extensions/`
