from pathlib import Path

from resumespec.parser import parse_xml
from resumespec.validator import validate_resume


ROOT = Path(__file__).parent.parent


def test_minimal_xml_example_parses_to_valid_profile_data():
    file = ROOT / "examples/xml/minimal.xml"

    profile = parse_xml(file)

    assert validate_resume(profile.data)
