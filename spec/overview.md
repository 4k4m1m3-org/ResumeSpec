# ResumeSpec v1.0.0 Overview

**One professional identity. Unlimited representations.**

ResumeSpec is an open standard for representing a professional identity as structured, portable, machine-readable data.

ResumeSpec defines professional information, its structure, its semantics, the machine-readable validation contract, and a reference implementation. It intentionally does not define visual resume design, PDF generation, portfolio generation, ATS scoring, AI behavior, exporters, platform integrations, or product workflows.

## Canonical Format

JSON is the canonical format for ResumeSpec v1.0.0.

The normative machine-readable contract is:

`schemas/json/resumespec.schema.json`

YAML and XML may be parsed by the Python reference implementation, but they are secondary implementation formats and do not have independent normative specifications in v1.

## Authority Order

ResumeSpec v1.0.0 uses this authority order:

1. `spec/` defines normative semantics.
2. `schemas/json/resumespec.schema.json` defines the JSON validation contract.
3. `examples/` show conforming and intentionally invalid documents.
4. `tests/` verify conformance.
5. Parser, validator, and CLI implement the standard.

The code does not define the standard. Documentation must not describe core v1 fields that the JSON Schema does not support.

## Core Document

A ResumeSpec document is a JSON object with two required top-level properties:

- `metadata`: information about the ResumeSpec document.
- `sections`: professional information about the person.

Individual sections are optional. A valid profile may contain only the sections relevant to the professional identity being represented.

## Extensibility

Unknown core fields are rejected by default. Extension fields are allowed only when the property name starts with `x-`.

Extension fields may appear on objects that explicitly allow them in the JSON Schema. Extensions must not redefine existing ResumeSpec fields or change core semantics.
