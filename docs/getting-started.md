# Getting Started

ResumeSpec v1.0.0 represents one professional identity as structured data.

JSON is the canonical format.

## Install

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e "implementations/python[dev]"
```

## Validate An Example

```bash
resumespec validate examples/json/minimal.json
```

The CLI uses the official schema by default.

## Create A Profile

Start from the minimal JSON example:

```bash
cp examples/json/minimal.json my-profile.json
```

Then edit the document while preserving:

- `metadata.resumespecVersion`: `1.0.0`
- `metadata.schemaVersion`: `1.0.0`
- `metadata.language`
- `sections`

## Validate Your Profile

```bash
resumespec validate my-profile.json
```

Use JSON output for automation:

```bash
resumespec validate my-profile.json --json
```

## Parse Without Validating

```bash
resumespec parse my-profile.json --json
```

Parsing loads a document. Validation checks conformance.
