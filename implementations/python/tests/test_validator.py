import json

import pytest

from resumespec.validator import (
    ResumeSpecValidationError,
    get_validation_result,
    load_json_file,
    load_schema,
    load_yaml_file,
    validate_files,
    validate_resume,
)


def test_load_json_file(tmp_path):
    data = {
        "metadata": {
            "resumespecVersion": "1.0.0",
            "schemaVersion": "1.0.0",
            "language": "en",
        },
        "sections": {},
    }

    file_path = tmp_path / "resume.json"
    file_path.write_text(
        json.dumps(data),
        encoding="utf-8",
    )

    result = load_json_file(file_path)

    assert result == data


def test_load_yaml_file(tmp_path):
    file_path = tmp_path / "resume.yaml"
    file_path.write_text(
        "metadata:\n"
        "  resumespecVersion: '1.0.0'\n"
        "  schemaVersion: '1.0.0'\n"
        "  language: en\n"
        "sections: {}\n",
        encoding="utf-8",
    )

    result = load_yaml_file(file_path)

    assert result == {
        "metadata": {
            "resumespecVersion": "1.0.0",
            "schemaVersion": "1.0.0",
            "language": "en",
        },
        "sections": {},
    }


def test_load_yaml_file_rejects_invalid_yaml(tmp_path):
    file_path = tmp_path / "invalid.yaml"
    file_path.write_text(
        "metadata:\n"
        "  language: [invalid\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_yaml_file(file_path)


def test_load_yaml_file_rejects_non_mapping(tmp_path):
    file_path = tmp_path / "invalid.yaml"
    file_path.write_text(
        "- one\n"
        "- two\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_yaml_file(file_path)


def test_load_json_file_missing_file(tmp_path):
    file_path = tmp_path / "missing.json"

    with pytest.raises(FileNotFoundError):
        load_json_file(file_path)


def test_load_schema(tmp_path):
    schema = {
        "type": "object",
        "required": ["metadata"],
    }

    file_path = tmp_path / "schema.json"
    file_path.write_text(
        json.dumps(schema),
        encoding="utf-8",
    )

    result = load_schema(file_path)

    assert result == schema


def test_validate_resume_accepts_valid_document():
    schema = {
        "type": "object",
        "required": ["metadata", "sections"],
    }

    document = {
        "metadata": {},
        "sections": {},
    }

    assert validate_resume(document, schema) is True


def test_validate_resume_rejects_invalid_document():
    schema = {
        "type": "object",
        "required": ["metadata", "sections"],
    }

    document = {
        "metadata": {},
    }

    with pytest.raises(ResumeSpecValidationError):
        validate_resume(document, schema)

def test_validate_files_accepts_yaml_document(tmp_path):
    resume_file = tmp_path / "resume.yaml"
    schema_file = tmp_path / "schema.json"

    resume_file.write_text(
        "metadata:\n"
        "  resumespecVersion: '1.0.0'\n"
        "  schemaVersion: '1.0.0'\n"
        "  language: en\n"
        "sections: {}\n",
        encoding="utf-8",
    )

    schema_file.write_text(
        json.dumps(
            {
                "type": "object",
                "required": ["metadata", "sections"],
            }
        ),
        encoding="utf-8",
    )

    assert validate_files(
        resume_file,
        schema_file,
    ) is True


def test_get_validation_result_returns_machine_readable_result(tmp_path):
    resume_file = tmp_path / "resume.json"
    schema_file = tmp_path / "schema.json"

    resume_file.write_text(
        json.dumps(
            {
                "metadata": {},
                "sections": {},
            }
        ),
        encoding="utf-8",
    )

    schema_file.write_text(
        json.dumps(
            {
                "type": "object",
                "required": ["metadata", "sections"],
            }
        ),
        encoding="utf-8",
    )

    result = get_validation_result(
        resume_file,
        schema_file,
    )

    assert result == {
        "valid": True,
        "errors": [],
    }