from pathlib import Path

import pytest

from resumespec.validator import validate_files


ROOT = Path(__file__).parent.parent


VALID_EXAMPLES = [
    ROOT / "examples/json/cybersecurity.json",
    ROOT / "examples/json/developer.json",
    ROOT / "examples/json/edge-extension.json",
    ROOT / "examples/json/it-operations.json",
    ROOT / "examples/json/minimal.json",
    ROOT / "examples/json/student.json",
]


@pytest.mark.parametrize("resume_file", VALID_EXAMPLES)
def test_json_example_is_valid(resume_file):
    assert validate_files(resume_file)
