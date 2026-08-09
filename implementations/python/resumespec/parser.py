import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

class ResumeSpecParseError(Exception):
    """Base exception for ResumeSpec parsing errors."""

@dataclass(frozen=True)
class ResumeProfile:
    """Parsed ResumeSpec document."""

    data: dict[str, Any]

    @property
    def metadata(self) -> dict[str, Any]:
        """Return ResumeSpec document metadata."""

        return self.data["metadata"]

    @property
    def sections(self) -> dict[str, Any]:
        """Return ResumeSpec profile sections."""

        return self.data["sections"]


def parse(path: str | Path) -> ResumeProfile:
    """Parse a ResumeSpec JSON document from a file."""

    file_path = Path(path)

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except (OSError, json.JSONDecodeError) as error:
        raise ResumeSpecParseError(
            f"Unable to parse ResumeSpec document: {file_path}"
        ) from error

    return parse_data(data)

def parse_yaml(path: str | Path) -> ResumeProfile:
    """Parse a ResumeSpec YAML document from a file."""

    file_path = Path(path)

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
    except (OSError, yaml.YAMLError) as error:
        raise ResumeSpecParseError(
            f"Unable to parse ResumeSpec YAML document: {file_path}"
        ) from error

    return parse_data(data)

def parse_data(data: Any) -> ResumeProfile:
    """Parse a ResumeSpec document from already loaded data."""

    if not isinstance(data, dict):
        raise ResumeSpecParseError(
            "ResumeSpec document must be a JSON object"
        )

    return ResumeProfile(data=data)
