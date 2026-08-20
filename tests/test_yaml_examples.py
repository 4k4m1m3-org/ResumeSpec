from pathlib import Path

from resumespec.validator import validate_files


ROOT = Path(__file__).parent.parent


def test_minimal_yaml_example_is_valid():
    file = ROOT / "examples/yaml/minimal.yaml"

    assert validate_files(file)
