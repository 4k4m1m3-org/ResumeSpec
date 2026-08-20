# Python Reference Implementation

The reference Python package lives in [`implementations/python/`](https://github.com/4k4m1m3-org/ResumeSpec/tree/v1.0.0/implementations/python).

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e "implementations/python[dev]"
```

## Use

```python
from resumespec import parse, validate_files, validate_resume

validate_files("examples/json/minimal.json")
profile = parse("examples/json/minimal.json")
validate_resume(profile.data)
```

## Supported Formats

- JSON
- YAML
- XML

## Testing

```bash
python -m pytest
```

## Public API

The package exports the parser and validator entry points used by the reference implementation. The site documents the public API as implemented in v1.0.0; it does not invent new functions.
