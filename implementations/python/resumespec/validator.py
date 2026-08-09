"""
ResumeSpec Python Validator

Validates ResumeSpec documents against the official JSON Schema.

This module provides the core validation logic.
The CLI interface should be implemented separately in cli.py.
"""

from pathlib import Path
import json
from typing import Any

import yaml

from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError


class ResumeSpecValidationError(Exception):
    """
    Custom exception for ResumeSpec validation failures.
    """

    pass


def load_json_file(path: str | Path) -> dict[str, Any]:
    """
    Load a JSON document from a file.

    Args:
        path: Path to JSON file.

    Returns:
        Parsed JSON object.

    Raises:
        FileNotFoundError:
            If the file does not exist.
        ValueError:
            If JSON is invalid.
    """

    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    try:
        with file_path.open(
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid JSON file: {error}"
        ) from error

def load_yaml_file(path: str | Path) -> dict[str, Any]:
    """
    Load a ResumeSpec YAML document from a file.

    Args:
        path:
            Path to YAML document.

    Returns:
        Parsed YAML object.

    Raises:
        FileNotFoundError:
            If the file does not exist.
        ValueError:
            If YAML is invalid.
    """

    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    try:
        with file_path.open(
            "r",
            encoding="utf-8"
        ) as file:
            data = yaml.safe_load(file)

    except yaml.YAMLError as error:
        raise ValueError(
            f"Invalid YAML file: {error}"
        ) from error

    if not isinstance(data, dict):
        raise ValueError(
            "ResumeSpec YAML document must be a mapping"
        )

    return data


def load_schema(path: str | Path) -> dict[str, Any]:
    """
    Load ResumeSpec JSON Schema.

    Args:
        path:
            Path to JSON Schema file.

    Returns:
        Parsed JSON Schema.
    """

    return load_json_file(path)


def validate_resume(
    resume_data: dict[str, Any],
    schema: dict[str, Any]
) -> bool:
    """
    Validate a ResumeSpec document.

    Args:
        resume_data:
            ResumeSpec document.

        schema:
            JSON Schema definition.

    Returns:
        True if valid.

    Raises:
        ResumeSpecValidationError:
            If validation fails.
    """

    validator = Draft202012Validator(schema)

    errors = sorted(
        validator.iter_errors(resume_data),
        key=lambda error: list(error.path)
    )

    if errors:
        messages = []

        for error in errors:
            location = ".".join(
                str(part)
                for part in error.path
            )

            if not location:
                location = "root"

            messages.append(
                f"{location}: {error.message}"
            )

        raise ResumeSpecValidationError(
            "\n".join(messages)
        )

    return True


def validate_files(
    resume_file: str | Path,
    schema_file: str | Path
) -> bool:
    """
    Validate a ResumeSpec JSON or YAML file against a schema file.

    Args:
        resume_file:
            ResumeSpec JSON or YAML document.

        schema_file:
            JSON Schema file.

    Returns:
        True if valid.
    """

    resume_path = Path(resume_file)

    if resume_path.suffix.lower() in {".yaml", ".yml"}:
        resume = load_yaml_file(resume_path)
    else:
        resume = load_json_file(resume_path)

    schema = load_schema(schema_file)

    return validate_resume(
        resume,
        schema
    )


def get_validation_result(
    resume_file: str | Path,
    schema_file: str | Path
) -> dict[str, Any]:
    """
    Validate a ResumeSpec file and return
    a machine-readable result.

    Useful for CLI tools,
    APIs and web integrations.

    Returns:
        Dictionary with validation status.
    """

    try:
        validate_files(
            resume_file,
            schema_file
        )

        return {
            "valid": True,
            "errors": []
        }

    except Exception as error:

        return {
            "valid": False,
            "errors": [
                str(error)
            ]
        }


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description="Validate ResumeSpec document"
    )

    parser.add_argument(
        "resume",
        help="Path to ResumeSpec JSON file"
    )

    parser.add_argument(
        "schema",
        help="Path to JSON Schema file"
    )

    args = parser.parse_args()

    result = get_validation_result(
        args.resume,
        args.schema
    )

    if result["valid"]:
        print(
            "✓ ResumeSpec document is valid"
        )

    else:
        print(
            "✗ ResumeSpec validation failed:"
        )

        for error in result["errors"]:
            print(error)
