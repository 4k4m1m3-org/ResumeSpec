from pathlib import Path
import sys
import json

sys.path.insert(
    0,
    str(Path(__file__).parent.parent / "implementations/python")
)

from validator import validate_files


ROOT = Path(__file__).parent.parent


def test_minimal_json_example_is_valid():
    resume_file = ROOT / "examples/json/minimal.json"
    schema_file = ROOT / "schemas/json/resumespec.schema.json"

    assert validate_files(
        resume_file,
        schema_file
    )