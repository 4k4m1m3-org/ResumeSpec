ResumeSpec RFCs

Request for Comments (RFC) Process


ResumeSpec is designed to evolve as an open standard. This evolution requires a transparent, structured, and community-driven process for proposing, discussing, and adopting changes.

This directory contains the Request for Comments (RFC) documents that describe proposed modifications, extensions, and improvements to the ResumeSpec standard.

The RFC process allows contributors to introduce new ideas while preserving compatibility, consistency, and long-term maintainability.


What is an RFC?

An RFC (Request for Comments) is a formal proposal for changing or extending ResumeSpec.

An RFC can introduce:

- New profile capabilities
- Changes to the ResumeSpec data model
- New sections or components
- New metadata fields
- Improvements to validation rules
- Changes to versioning behavior
- New interoperability features
- Extensions for future use cases

RFCs are not only technical documents. They are design proposals that explain the motivation, reasoning, impact, and expected adoption path of a change.


Why Does ResumeSpec Use RFCs?

ResumeSpec aims to become a long-lived standard for representing professional identity and career information.

Standards that evolve without a clear process usually face problems such as:

- Inconsistent implementations
- Breaking changes
- Fragmentation between tools
- Poor interoperability
- Difficult migration paths

The RFC process provides:

- Transparency
- Community participation
- Technical discussion
- Historical documentation
- Controlled evolution

Every important change to ResumeSpec should have a clear origin, discussion, and decision record.


RFC Lifecycle

Draft

A contributor creates a new RFC proposal.

At this stage:

- The idea is documented
- The problem is explained
- Possible solutions are explored
- Feedback is requested

A Draft RFC does not represent an approved change.


Review

The community and maintainers review the proposal.

Discussion may include:

- Technical feasibility
- Compatibility impact
- Alternative approaches
- Security considerations
- User experience implications
- Long-term maintenance costs

The RFC may be modified during this phase.


Accepted

An RFC is accepted when there is enough agreement that the proposal should become part of ResumeSpec.

Acceptance means:

- The design direction is approved
- Implementation can begin
- Related specifications can be updated

Acceptance does not necessarily mean immediate release.


Implemented

The approved change is incorporated into:

- The ResumeSpec specification
- JSON Schema definitions
- Reference implementations
- Documentation
- Tooling

The corresponding version change is documented according to the versioning policy.


Deprecated

Some RFCs may later become obsolete.

A deprecated RFC:

- Remains part of the historical record
- Should not be used for new implementations
- May be replaced by a newer RFC

Deprecation decisions should include migration guidance.


RFC Naming Convention

RFC documents use a sequential numbering system:

RFC-0001
RFC-0002
RFC-0003


Each RFC should have a unique identifier.

Recommended structure:

RFCs/

README.md

RFC-0001-title.md

RFC-0002-title.md

RFC-0003-title.md


Example:

RFC-0001-profile-extensions.md


RFC Structure

Every RFC should follow a common structure:

RFC-XXXX: Title


Status

Draft | Review | Accepted | Implemented | Deprecated


Author(s)

Contributor names or organization


Created

YYYY-MM-DD


Summary

Short explanation of the proposal.


Motivation

Why is this change needed?


Proposal

Detailed description of the solution.


Specification Changes

What parts of ResumeSpec are affected?


Compatibility

Potential impact on existing profiles or implementations.


Alternatives Considered

Other approaches that were evaluated.


Security Considerations

Potential security implications.


Migration Plan

How existing implementations can adopt the change.


Open Questions

Remaining discussion points.


Types of RFCs

ResumeSpec RFCs can be categorized into different areas.


Core RFCs

Changes to the fundamental specification.

Examples:

- Data model changes
- Required fields
- Core entities
- Validation rules


Extension RFCs

New optional capabilities.

Examples:

- New professional sections
- Additional profile metadata
- New industry-specific information


Technical RFCs

Implementation-related improvements.

Examples:

- JSON Schema changes
- Serialization formats
- API interoperability
- Validation mechanisms


Governance RFCs

Changes to how ResumeSpec is maintained.

Examples:

- Contribution process
- Decision-making procedures
- Maintainer responsibilities


Compatibility Principles

ResumeSpec prioritizes long-term compatibility.

RFC proposals should consider:

- Existing profile preservation
- Migration complexity
- Backward compatibility
- Forward compatibility
- Implementation impact

Breaking changes should require strong justification and appropriate versioning.


Relationship with Versioning

RFCs and versioning are closely connected.

An accepted RFC may result in:

- Patch version changes for corrections
- Minor version changes for backward-compatible additions
- Major version changes for breaking changes

The complete evolution policy is defined in:

spec/versioning.md


Creating a New RFC

Before creating an RFC:

1. Check existing RFCs

2. Confirm that the proposal does not already exist

3. Explain the problem clearly

4. Consider compatibility implications

5. Provide examples when possible


A good RFC should answer:

- What problem does this solve?

- Why is this important?

- How should ResumeSpec change?

- What are the consequences?


RFC Repository

The RFC directory is the historical and technical record of ResumeSpec evolution.

It should contain:

- Active proposals
- Accepted changes
- Rejected ideas
- Historical decisions

Every important decision should remain discoverable for future contributors.


Future of the RFC Process

As ResumeSpec grows, the RFC process may evolve to include:

- Community voting mechanisms
- Working groups
- Reference implementation reviews
- Formal governance structures
- Public standards discussions

The goal is to ensure ResumeSpec remains open, adaptable, and sustainable for decades.
