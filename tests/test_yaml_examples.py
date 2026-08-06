import yaml
from pathlib import Path


ROOT = Path(__file__).parent.parent


def test_minimal_yaml_example_is_valid():
    file = ROOT / "examples/yaml/minimal.yaml"

    with file.open() as f:
        data = yaml.safe_load(f)

    assert data is not None
    assert "resumeSpec" in data