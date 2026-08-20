import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parent.parent


def run_cli(*args):
    return subprocess.run(
        [sys.executable, "-m", "resumespec.cli", *args],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )


def test_cli_validate_valid_document_exits_zero():
    result = run_cli("validate", "examples/json/minimal.json")

    assert result.returncode == 0
    assert "document is valid" in result.stdout


def test_cli_validate_invalid_document_exits_nonzero():
    result = run_cli("validate", "examples/json/invalid-unknown-field.json")

    assert result.returncode == 1
    assert "validation failed" in result.stderr


def test_cli_parse_json_document_exits_zero():
    result = run_cli("parse", "examples/json/minimal.json", "--json")

    assert result.returncode == 0
    assert '"metadata"' in result.stdout
