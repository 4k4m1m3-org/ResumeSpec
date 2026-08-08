from pathlib import Path

from resumespec.validator import validate_files


ROOT = Path(__file__).parent.parent


def test_minimal_json_example_is_valid():
    resume_file = ROOT / "examples/json/minimal.json"
    schema_file = ROOT / "schemas/json/resumespec.schema.json"

    assert validate_files(
        resume_file,
        schema_file
    )