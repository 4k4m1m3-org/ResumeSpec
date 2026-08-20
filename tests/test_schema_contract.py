import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from resumespec.validator import ResumeSpecValidationError, load_schema, validate_resume


ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "schemas/json/resumespec.schema.json"


def minimal_document():
    return {
        "metadata": {
            "resumespecVersion": "1.0.0",
            "schemaVersion": "1.0.0",
            "language": "en",
        },
        "sections": {},
    }


def test_schema_is_valid_draft_2020_12():
    Draft202012Validator.check_schema(load_schema(SCHEMA))


def test_packaged_schema_matches_repository_schema():
    package_schema = (
        ROOT
        / "implementations/python/resumespec/schemas/json/resumespec.schema.json"
    )

    assert json.loads(package_schema.read_text(encoding="utf-8")) == load_schema(SCHEMA)


def test_minimal_document_is_valid():
    assert validate_resume(minimal_document()) is True


def test_complete_document_is_valid():
    document = json.loads(
        (ROOT / "examples/json/developer.json").read_text(encoding="utf-8")
    )

    assert validate_resume(document) is True


def test_required_metadata_fields_are_enforced():
    document = minimal_document()
    del document["metadata"]["resumespecVersion"]

    with pytest.raises(ResumeSpecValidationError, match="resumespecVersion"):
        validate_resume(document)


def test_types_are_enforced():
    document = minimal_document()
    document["sections"]["skills"] = "Python"

    with pytest.raises(ResumeSpecValidationError, match="sections.skills"):
        validate_resume(document)


def test_enums_are_enforced():
    document = minimal_document()
    document["metadata"]["visibility"] = "everyone"

    with pytest.raises(ResumeSpecValidationError, match="visibility"):
        validate_resume(document)


def test_unknown_fields_are_rejected():
    document = minimal_document()
    document["sections"]["unexpectedSection"] = []

    with pytest.raises(ResumeSpecValidationError, match="unexpectedSection"):
        validate_resume(document)


def test_format_checker_rejects_invalid_email_and_url():
    document = minimal_document()
    document["sections"]["identity"] = {
        "contact": {
            "email": "not-an-email"
        }
    }
    document["sections"]["links"] = [
        {
            "url": "http://[invalid"
        }
    ]

    with pytest.raises(ResumeSpecValidationError) as error:
        validate_resume(document)

    message = str(error.value)
    assert "email" in message
    assert "url" in message


def test_profile_dates_accept_year_month_precision():
    document = minimal_document()
    document["sections"]["experience"] = [
        {
            "dateRange": {
                "startDate": "2026-01",
                "endDate": "2026-12",
            }
        }
    ]

    assert validate_resume(document) is True


def test_invalid_profile_date_is_rejected():
    document = minimal_document()
    document["sections"]["experience"] = [
        {
            "dateRange": {
                "startDate": "January 2026",
            }
        }
    ]

    with pytest.raises(ResumeSpecValidationError, match="startDate"):
        validate_resume(document)


def test_extension_fields_must_use_x_prefix():
    document = minimal_document()
    document["sections"]["skills"] = [
        {
            "name": "Linux",
            "x-source": "self-reported",
        }
    ]
    document["x-documentId"] = "profile-001"

    assert validate_resume(document) is True
