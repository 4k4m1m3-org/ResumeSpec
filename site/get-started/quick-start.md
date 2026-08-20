# Quick Start

This quick start uses the exact v1.0.0 example that ships in the repository.

## 1. Minimal ResumeSpec Document

```json
{
  "metadata": {
    "resumespecVersion": "1.0.0",
    "schemaVersion": "1.0.0",
    "language": "en"
  },
  "sections": {
    "identity": {
      "person": {
        "givenName": "Wuilmer",
        "familyName": "Bolivar"
      }
    },
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

This is the same shape as [`examples/json/minimal.json`](https://github.com/4k4m1m3-org/ResumeSpec/blob/v1.0.0/examples/json/minimal.json).

## 2. Install The Reference Implementation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e "implementations/python[dev]"
```

## 3. Validate

```bash
resumespec validate examples/json/minimal.json
```

Expected result:

```text
ResumeSpec document is valid: examples/json/minimal.json
```

The CLI then prints the absolute path to the official schema in your checkout.

## 4. Parse

```bash
resumespec parse examples/json/minimal.json --json
```

Expected result:

```json
{
  "metadata": {
    "resumespecVersion": "1.0.0",
    "schemaVersion": "1.0.0",
    "language": "en"
  },
  "sections": {
    "identity": {
      "person": {
        "givenName": "Wuilmer",
        "familyName": "Bolivar"
      }
    },
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

## 5. See The Contract

- [Specification Overview](/specification/)
- [JSON Schema](/specification/json-schema)
- [Python Reference](/reference/python)
