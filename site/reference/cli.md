# CLI

The reference CLI is installed as `resumespec`.

## Commands

Validate a document:

```bash
resumespec validate examples/json/minimal.json
```

Parse a document:

```bash
resumespec parse examples/json/minimal.json --json
```

## Exit Codes

- `0`: valid document or successful parse
- `1`: validation failure
- `2`: parse failure or CLI usage error

## Notes

- The validator uses the official schema by default.
- The parser and validator are separate concerns.

