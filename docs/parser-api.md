# ResumeSpec Parser API

## Status

**Phase:** 3 — Reference Implementation
**Task:** 3.1.1 — Design Parser API
**Status:** Draft

---

## 1. Purpose

The ResumeSpec parser provides the entry point for loading professional identity documents into the reference implementation.

The parser is responsible for reading a ResumeSpec document, interpreting its representation format, and returning a structured `ResumeProfile` representation that can be consumed by other ResumeSpec components.

The parser is intentionally designed as a small and stable API.

It should serve as the foundation for:

* Validation
* CLI commands
* SDK functionality
* Serialization
* Future integrations
* Documentation tools

---

## 2. Design Goals

The initial parser API should be:

* Simple
* Predictable
* Format-aware
* Extensible
* Independent from the CLI
* Independent from serialization
* Independent from the future domain model
* Suitable for use by both applications and higher-level ResumeSpec tooling

The parser should not contain application-specific logic.

---

## 3. Public API

The initial public API consists of two functions.

### `parse()`

Loads a ResumeSpec document from a file.

```python
from resumespec import parse

profile = parse("resume.json")
```

The parser determines the representation format from the file or from explicit parser configuration when required.

The returned value is a `ResumeProfile`.

---

### `parse_data()`

Parses ResumeSpec data that has already been loaded into memory.

```python
from resumespec import parse_data

profile = parse_data(data)
```

This separates document parsing from filesystem access and allows the parser to be used by:

* APIs
* Web applications
* CLI tools
* Tests
* Other SDK components

---

## 4. Result

Both functions return a `ResumeProfile`.

Conceptually:

```text
ResumeSpec document
        │
        ▼
     Parser
        │
        ▼
 ResumeProfile
```

`ResumeProfile` represents the parsed professional identity and provides the structured data required by the rest of the reference implementation.

The detailed internal model of `ResumeProfile` is intentionally outside the scope of this task.

That model will be defined in **Phase 3.2 — Internal Model**.

---

## 5. Initial Format Support

The parser will initially support:

| Format | Phase 3.1       |
| ------ | --------------- |
| JSON   | Supported first |
| YAML   | Planned         |
| XML    | Planned         |

JSON is the first implementation target because it is currently the primary machine-readable representation validated against the official ResumeSpec JSON Schema.

YAML and XML support will be added incrementally without changing the conceptual public parser API.

For example:

```python
profile = parse("resume.yaml")
```

and:

```python
profile = parse("resume.xml")
```

should eventually use the same parser entry point.

---

## 6. Parser Responsibilities

The parser is responsible for:

1. Reading the input document.
2. Determining or receiving the document format.
3. Parsing the representation.
4. Producing a structured `ResumeProfile`.
5. Reporting parsing-related errors through ResumeSpec-specific exceptions.

The parser is not responsible for:

* Schema validation
* CLI argument handling
* Rendering
* PDF generation
* HTML generation
* Serialization
* Domain-specific business logic

Validation will remain a separate concern and will later integrate with the parser.

---

## 7. Error Model

The reference implementation will expose ResumeSpec-specific parser errors.

### `ResumeSpecParseError`

Base exception for parser failures.

Example:

```python
from resumespec import ResumeSpecParseError

try:
    profile = parse("resume.json")
except ResumeSpecParseError as error:
    print(error)
```

### `UnsupportedFormatError`

Raised when the parser receives a format that is not supported.

Example:

```text
Unsupported ResumeSpec format: txt
```

Other specialized exceptions may be introduced when implementation requirements justify them.

The initial API should avoid exposing implementation-specific exceptions directly to consumers.

---

## 8. Separation of Concerns

The parser should remain independent from the internal domain model.

The intended architecture is:

```text
             ResumeSpec Document
                      │
                      ▼
               ┌─────────────┐
               │    Parser   │
               └──────┬──────┘
                      │
                      ▼
               ResumeProfile
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
      Validator       CLI        SDK
```

The parser answers:

> How do we load a ResumeSpec document?

The internal model answers:

> How do we represent a professional identity inside the implementation?

These concerns must remain separate.

---

## 9. API Evolution

The initial API intentionally exposes only:

```python
parse(path)
parse_data(data)
```

Additional functions or configuration options should only be introduced when they solve a concrete requirement.

The reference implementation should avoid premature abstractions such as:

```python
ParserFactory
ParserRegistry
DocumentPipeline
FormatManager
```

unless future requirements demonstrate a need for them.

The initial implementation should favor a small public surface.

---

## 10. Future Direction

The parser is expected to become the common entry point for all ResumeSpec representations.

Future usage should be conceptually equivalent to:

```python
profile = parse("resume.json")
profile = parse("resume.yaml")
profile = parse("resume.xml")
```

while maintaining the same resulting `ResumeProfile` abstraction.

This allows applications to work with ResumeSpec professional identities without depending on the original representation format.

---

## 11. Scope of This Task

This document defines the API contract only.

The following are explicitly outside the scope of this task:

* JSON parser implementation
* YAML parser implementation
* XML parser implementation
* Internal domain model implementation
* Validator integration
* CLI integration
* SDK packaging
* Serialization

Those concerns will be addressed by subsequent Phase 3 tasks.

---

## 12. Definition of Done

This design task is complete when:

* `parse()` is defined.
* `parse_data()` is defined.
* `ResumeProfile` is established as the parser result.
* JSON is identified as the first implementation target.
* YAML and XML are identified as future formats.
* Parser responsibilities are defined.
* Parser boundaries are defined.
* Public parser exceptions are defined.
* Internal model responsibilities remain separate.
* No implementation details unnecessarily constrain future development.
