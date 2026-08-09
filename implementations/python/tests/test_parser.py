import json

import pytest

from resumespec.parser import (
    ResumeProfile,
    ResumeSpecParseError,
    parse,
    parse_data,
    parse_yaml,
)

def test_parse_valid_json_file(tmp_path):
    data = {
        "person": {
            "name": "Wuilmer Bolivar"
        }
    }

    file_path = tmp_path / "resume.json"
    file_path.write_text(json.dumps(data), encoding="utf-8")

    profile = parse(file_path)

    assert isinstance(profile, ResumeProfile)
    assert profile.data == data


def test_parse_data_returns_resume_profile():
    data = {
        "person": {
            "name": "Wuilmer Bolivar"
        }
    }

    profile = parse_data(data)

    assert isinstance(profile, ResumeProfile)
    assert profile.data == data


def test_parse_missing_file_raises_error(tmp_path):
    file_path = tmp_path / "missing.json"

    with pytest.raises(ResumeSpecParseError):
        parse(file_path)


def test_parse_invalid_json_raises_error(tmp_path):
    file_path = tmp_path / "invalid.json"
    file_path.write_text("{invalid json}", encoding="utf-8")

    with pytest.raises(ResumeSpecParseError):
        parse(file_path)


def test_parse_data_rejects_non_object():
    with pytest.raises(ResumeSpecParseError):
        parse_data(["not", "a", "profile"])

def test_parse_valid_yaml_file(tmp_path):
    data = {
        "person": {
            "name": "Wuilmer Bolivar"
        }
    }

    file_path = tmp_path / "resume.yaml"
    file_path.write_text(
        "person:\n"
        "  name: Wuilmer Bolivar\n",
        encoding="utf-8",
    )

    profile = parse_yaml(file_path)

    assert isinstance(profile, ResumeProfile)
    assert profile.data == data


def test_parse_invalid_yaml_raises_error(tmp_path):
    file_path = tmp_path / "invalid.yaml"
    file_path.write_text(
        "person:\n"
        "  name: [invalid",
        encoding="utf-8",
    )

    with pytest.raises(ResumeSpecParseError):
        parse_yaml(file_path)


def test_parse_yaml_rejects_non_object(tmp_path):
    file_path = tmp_path / "invalid.yaml"
    file_path.write_text(
        "- not\n"
        "- a\n"
        "- profile\n",
        encoding="utf-8",
    )

    with pytest.raises(ResumeSpecParseError):
        parse_yaml(file_path)


def test_resume_profile_exposes_metadata_and_sections():
    data = {
        "metadata": {
            "resumespecVersion": "1.0",
            "schemaVersion": "1.0",
            "language": "en",
        },
        "sections": {
            "summary": {
                "text": "IT Operations professional."
            }
        },
    }

    profile = parse_data(data)

    assert profile.metadata == data["metadata"]
    assert profile.sections == data["sections"]
    assert profile.data == data


def test_parse_yaml_is_public_api():
    from resumespec import parse_yaml

    assert callable(parse_yaml)
