# ResumeSpec Parser API

The Python parser loads a ResumeSpec document and returns a `ResumeProfile`.

Parsing is not validation. A parsed document may still be invalid under the v1 JSON Schema.

## Public API

```python
from resumespec import parse, parse_data

profile = parse("examples/json/minimal.json")
data_profile = parse_data({"metadata": {}, "sections": {}})
```

The stable public parser API is:

- `parse(path)`: load JSON, YAML, or XML from disk.
- `parse_data(data)`: wrap already loaded mapping data.
- `ResumeProfile`: parsed document wrapper with `data`, `metadata`, and `sections`.
- `ResumeSpecParseError`: parser error type.

`parse_yaml` and `parse_xml` are exported for the reference implementation, but JSON remains the canonical v1 format.

## Format Support

| Format | Status |
| --- | --- |
| JSON | Canonical v1 format |
| YAML | Secondary implementation format |
| XML | Experimental implementation format |

XML parsing uses `defusedxml`. ResumeSpec v1 does not define an XSD or independent XML normative contract.

## Responsibilities

The parser:

- reads a document;
- determines the format from the file extension;
- parses it into Python data;
- returns a `ResumeProfile`;
- raises `ResumeSpecParseError` for parse failures.

The parser does not:

- validate against the schema;
- apply semantic rules;
- render documents;
- generate PDF, HTML, or portfolio output;
- execute document content.

Use the validator for conformance:

```python
from resumespec import parse, validate_resume

profile = parse("examples/json/minimal.json")
validate_resume(profile.data)
```
