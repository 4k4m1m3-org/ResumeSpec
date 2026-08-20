import json

import pytest

from resumespec.parser import (
    ResumeProfile,
    ResumeSpecParseError,
    parse,
    parse_data,
    parse_xml,
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
            "resumespecVersion": "1.0.0",
            "schemaVersion": "1.0.0",
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


def test_parse_valid_xml_file(tmp_path):
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<resumeSpec>
  <metadata>
    <resumespecVersion>1.0.0</resumespecVersion>
    <schemaVersion>1.0.0</schemaVersion>
    <profileVersion>1.0.0</profileVersion>
    <language>en</language>
    <tags>
      <tag>professional-profile</tag>
    </tags>
  </metadata>
  <sections>
    <identity>
      <person>
        <givenName>Wuilmer</givenName>
        <familyName>Bolivar</familyName>
      </person>
    </identity>
    <skills>
      <item>
        <name>Linux</name>
      </item>
    </skills>
  </sections>
</resumeSpec>
"""

    file_path = tmp_path / "resume.xml"
    file_path.write_text(xml, encoding="utf-8")

    profile = parse_xml(file_path)

    assert isinstance(profile, ResumeProfile)
    assert profile.metadata["resumespecVersion"] == "1.0.0"
    assert profile.metadata["tags"] == ["professional-profile"]
    assert profile.sections["identity"]["person"]["givenName"] == "Wuilmer"
    assert profile.sections["skills"] == [{"name": "Linux"}]


def test_parse_invalid_xml_raises_error(tmp_path):
    file_path = tmp_path / "invalid.xml"
    file_path.write_text(
        "<resumeSpec><metadata></resumeSpec>",
        encoding="utf-8",
    )

    with pytest.raises(ResumeSpecParseError):
        parse_xml(file_path)


def test_parse_xml_rejects_invalid_root(tmp_path):
    file_path = tmp_path / "invalid.xml"
    file_path.write_text(
        "<profile><name>Wuilmer Bolivar</name></profile>",
        encoding="utf-8",
    )

    with pytest.raises(ResumeSpecParseError):
        parse_xml(file_path)

def test_parse_xml_converts_boolean_values(tmp_path):
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<resumeSpec>
  <metadata>
    <resumespecVersion>1.0.0</resumespecVersion>
    <schemaVersion>1.0.0</schemaVersion>
    <language>en</language>
  </metadata>
  <sections>
    <experience>
      <item>
        <dateRange>
          <current>true</current>
        </dateRange>
      </item>
    </experience>
  </sections>
</resumeSpec>
"""

    file_path = tmp_path / "resume.xml"
    file_path.write_text(xml, encoding="utf-8")

    profile = parse_xml(file_path)

    current = profile.sections["experience"][0]["dateRange"]["current"]

    assert current is True
    assert isinstance(current, bool)

def test_parse_dispatches_yaml(tmp_path):
    file_path = tmp_path / "resume.yaml"
    file_path.write_text(
        "metadata:\n"
        "  resumespecVersion: '1.0.0'\n"
        "  schemaVersion: '1.0.0'\n"
        "  language: en\n"
        "sections:\n"
        "  summary:\n"
        "    text: IT Operations professional.\n",
        encoding="utf-8",
    )

    profile = parse(file_path)

    assert profile.metadata["resumespecVersion"] == "1.0.0"
    assert profile.sections["summary"]["text"] == (
        "IT Operations professional."
    )


def test_parse_dispatches_xml(tmp_path):
    file_path = tmp_path / "resume.xml"
    file_path.write_text(
        """<?xml version="1.0" encoding="UTF-8"?>
<resumeSpec>
  <metadata>
    <resumespecVersion>1.0.0</resumespecVersion>
    <schemaVersion>1.0.0</schemaVersion>
    <language>en</language>
  </metadata>
  <sections>
    <identity>
      <person>
        <givenName>Wuilmer</givenName>
      </person>
    </identity>
  </sections>
</resumeSpec>
""",
        encoding="utf-8",
    )

    profile = parse(file_path)

    assert profile.metadata["resumespecVersion"] == "1.0.0"
    assert profile.sections["identity"]["person"]["givenName"] == "Wuilmer"


def test_parse_keeps_json_support(tmp_path):
    file_path = tmp_path / "resume.json"
    file_path.write_text(
        '{"metadata": {"resumespecVersion": "1.0.0"}, "sections": {}}',
        encoding="utf-8",
    )

    profile = parse(file_path)

    assert profile.metadata["resumespecVersion"] == "1.0.0"
    assert profile.sections == {}