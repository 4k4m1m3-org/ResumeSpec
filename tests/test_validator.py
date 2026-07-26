from pathlib import Path

import pytest

from implementations.python.validator import (
    validate_files,
    ResumeSpecValidationError,
)


ROOT = Path(__file__).parent.parent


SCHEMA = (
    ROOT
    / "schemas"
    / "json"
    / "resumespec.schema.json"
)


def test_valid_document():

    document = (
        ROOT
        / "tests"
        / "fixtures"
        / "valid"
        / "minimal-profile.json"
    )

    result = validate_files(
        document,
        SCHEMA
    )

    assert result is True


def test_invalid_document():

    document = (
        ROOT
        / "tests"
        / "fixtures"
        / "invalid"
        / "missing_version.json"
    )

    with pytest.raises(
        ResumeSpecValidationError
    ):

        validate_files(
            document,
            SCHEMA
        )
