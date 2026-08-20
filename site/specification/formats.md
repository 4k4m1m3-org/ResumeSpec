# Formats

## Canonical

JSON is the canonical ResumeSpec v1.0.0 format.

## Secondary

YAML is supported by the Python reference implementation as a secondary convenience format.

## Experimental

XML is supported by the Python reference implementation as an experimental format and is parsed with `defusedxml`.

## Important Distinction

Parsing a document is not the same as validating a document. The schema defines conformance; the parser only loads data.

