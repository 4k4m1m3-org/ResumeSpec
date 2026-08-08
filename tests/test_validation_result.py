from pathlib import Path

from resumespec.validator import (
    get_validation_result,
)

ROOT = Path(__file__).parent.parent


SCHEMA = (
    ROOT
    / "schemas"
    / "json"
    / "resumespec.schema.json"
)


def test_validation_result_success():

    document = (
        ROOT
        / "tests"
        / "fixtures"
        / "valid"
        / "minimal-profile.json"
    )

    result = get_validation_result(
        document,
        SCHEMA
    )

    assert result["valid"] is True
    assert result["errors"] == []


def test_validation_result_failure():

    document = (
        ROOT
        / "tests"
        / "fixtures"
        / "invalid"
        / "missing_version.json"
    )

    result = get_validation_result(
        document,
        SCHEMA
    )

    assert result["valid"] is False
    assert len(result["errors"]) > 0
