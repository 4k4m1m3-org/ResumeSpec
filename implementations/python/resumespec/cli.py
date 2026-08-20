"""
ResumeSpec command line interface.
"""

import argparse
import json
import sys

from resumespec.parser import ResumeSpecParseError, parse
from resumespec.validator import get_default_schema_path, get_validation_result


def create_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""

    parser = argparse.ArgumentParser(
        prog="resumespec",
        description="Validate and parse ResumeSpec documents.",
    )

    subcommands = parser.add_subparsers(dest="command")

    validate_parser = subcommands.add_parser(
        "validate",
        help="Validate a ResumeSpec JSON or YAML document.",
    )
    validate_parser.add_argument(
        "resume",
        help="Path to a ResumeSpec document.",
    )
    validate_parser.add_argument(
        "--schema",
        default=None,
        help=(
            "Path to a JSON Schema file. "
            "Defaults to the official ResumeSpec v1.0.0 schema."
        ),
    )
    validate_parser.add_argument(
        "--json",
        action="store_true",
        help="Output validation result as JSON.",
    )

    parse_parser = subcommands.add_parser(
        "parse",
        help="Parse a ResumeSpec JSON, YAML, or experimental XML document.",
    )
    parse_parser.add_argument(
        "resume",
        help="Path to a ResumeSpec document.",
    )
    parse_parser.add_argument(
        "--json",
        action="store_true",
        help="Output parsed data as JSON.",
    )

    parser.add_argument(
        "--version",
        action="version",
        version="ResumeSpec reference implementation 1.0.0",
    )

    return parser


def _run_validate(args: argparse.Namespace) -> int:
    result = get_validation_result(args.resume, args.schema)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0 if result["valid"] else 1

    if result["valid"]:
        schema = args.schema or get_default_schema_path()
        print(f"ResumeSpec document is valid: {args.resume}")
        print(f"Schema: {schema}")
        return 0

    print(f"ResumeSpec validation failed: {args.resume}", file=sys.stderr)

    for error in result["errors"]:
        print(f"- {error}", file=sys.stderr)

    return 1


def _run_parse(args: argparse.Namespace) -> int:
    try:
        profile = parse(args.resume)
    except ResumeSpecParseError as error:
        print(f"ResumeSpec parse failed: {error}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(profile.data, indent=2, ensure_ascii=False))
    else:
        print(f"ResumeSpec document parsed: {args.resume}")

    return 0


def main() -> int:
    """Execute the CLI application."""

    parser = create_parser()
    args = parser.parse_args()

    if args.command == "validate":
        return _run_validate(args)

    if args.command == "parse":
        return _run_parse(args)

    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
