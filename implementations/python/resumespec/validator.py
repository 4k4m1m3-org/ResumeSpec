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

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import ValidationError

try:
    from importlib.resources import files
except ImportError:  # pragma: no cover
    files = None


SCHEMA_RESOURCE = "schemas/json/resumespec.schema.json"


class ResumeSpecValidationError(Exception):
    """
    Custom exception for ResumeSpec validation failures.
    """

    pass


def get_default_schema_path() -> Path:
    """
    Return the official ResumeSpec JSON Schema path.

    Editable installs use the repository schema as the source of truth.
    Packaged installs fall back to the schema included with the Python package.
    """

    repository_schema = (
        Path(__file__).resolve().parents[3]
        / "schemas"
        / "json"
        / "resumespec.schema.json"
    )

    if repository_schema.exists():
        return repository_schema

    if files is None:
        raise FileNotFoundError(
            "Unable to locate the official ResumeSpec JSON Schema"
        )

    package_schema = files("resumespec").joinpath(SCHEMA_RESOURCE)
    return Path(str(package_schema))


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


def load_schema(path: str | Path | None = None) -> dict[str, Any]:
    """
    Load ResumeSpec JSON Schema.

    Args:
        path:
            Path to JSON Schema file. If omitted, the official v1 schema is used.

    Returns:
        Parsed JSON Schema.
    """

    schema_path = get_default_schema_path() if path is None else Path(path)

    return load_json_file(schema_path)


def validate_resume(
    resume_data: dict[str, Any],
    schema: dict[str, Any] | None = None
) -> bool:
    """
    Validate a ResumeSpec document.

    Args:
        resume_data:
            ResumeSpec document.

        schema:
            JSON Schema definition. If omitted, the official v1 schema is used.

    Returns:
        True if valid.

    Raises:
        ResumeSpecValidationError:
            If validation fails.
    """

    active_schema = load_schema() if schema is None else schema

    Draft202012Validator.check_schema(active_schema)

    validator = Draft202012Validator(
        active_schema,
        format_checker=FormatChecker(),
    )

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
    schema_file: str | Path | None = None
) -> bool:
    """
    Validate a ResumeSpec JSON or YAML file against a schema file.

    Args:
        resume_file:
            ResumeSpec JSON or YAML document.

        schema_file:
            JSON Schema file. If omitted, the official v1 schema is used.

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
    schema_file: str | Path | None = None
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
        nargs="?",
        help="Path to JSON Schema file. Defaults to the official ResumeSpec schema."
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
