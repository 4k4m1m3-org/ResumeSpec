import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from xml.etree.ElementTree import Element

import yaml
from defusedxml import ElementTree as ET


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
    """Parse a ResumeSpec document from JSON, YAML, or XML."""

    file_path = Path(path)
    suffix = file_path.suffix.lower()

    if suffix in {".yaml", ".yml"}:
        return parse_yaml(file_path)

    if suffix == ".xml":
        return parse_xml(file_path)

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


def parse_xml(path: str | Path) -> ResumeProfile:
    """Parse a ResumeSpec XML document from a file."""

    file_path = Path(path)

    try:
        tree = ET.parse(file_path)
    except (OSError, ET.ParseError) as error:
        raise ResumeSpecParseError(
            f"Unable to parse ResumeSpec XML document: {file_path}"
        ) from error

    root = tree.getroot()

    if root.tag != "resumeSpec":
        raise ResumeSpecParseError(
            "ResumeSpec XML document must have a 'resumeSpec' root element"
        )

    data = _xml_element_to_data(root)

    if not isinstance(data, dict):
        raise ResumeSpecParseError(
            "ResumeSpec XML document must contain an object"
        )

    return parse_data(data)


def _xml_element_to_data(element: Element) -> Any:
    """Convert a ResumeSpec XML element into Python data."""

    children = list(element)

    if not children:
        text = (element.text or "").strip()

        if text == "true":
            return True

        if text == "false":
            return False

        return text

    if all(child.tag == "item" for child in children):
        return [_xml_element_to_data(child) for child in children]

    if all(child.tag == "tag" for child in children):
        return [_xml_element_to_data(child) for child in children]

    data: dict[str, Any] = {}

    for child in children:
        value = _xml_element_to_data(child)

        if child.tag in data:
            existing = data[child.tag]

            if isinstance(existing, list):
                existing.append(value)
            else:
                data[child.tag] = [existing, value]
        else:
            data[child.tag] = value

    return data


def parse_data(data: Any) -> ResumeProfile:
    """Parse a ResumeSpec document from already loaded data."""

    if not isinstance(data, dict):
        raise ResumeSpecParseError(
            "ResumeSpec document must be a JSON object"
        )

    return ResumeProfile(data=data)
