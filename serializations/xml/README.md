# XML Serialization

XML is an experimental implementation format in ResumeSpec v1.0.0.

The Python reference parser can load the minimal XML representation used by the examples and tests.

XML does not have an independent normative v1 specification or XSD. Conformance is determined by parsing XML into the ResumeSpec data model and validating that data against the canonical JSON Schema. XML parsing uses `defusedxml` in the reference implementation.
