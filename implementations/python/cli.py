"""
ResumeSpec CLI Validator

Command line interface for validating ResumeSpec documents.

This module uses validator.py as the validation engine.
"""


import argparse
import sys

from validator import (
    get_validation_result
)


def create_parser() -> argparse.ArgumentParser:
    """
    Create CLI argument parser.
    """

    parser = argparse.ArgumentParser(
        prog="resumespec-validator",
        description=(
            "Validate ResumeSpec documents "
            "against a JSON Schema."
        )
    )

    parser.add_argument(
        "resume",
        help=(
            "Path to ResumeSpec JSON document"
        )
    )

    parser.add_argument(
        "schema",
        help=(
            "Path to ResumeSpec JSON Schema"
        )
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help=(
            "Output validation result as JSON"
        )
    )

    return parser


def main() -> int:
    """
    Execute CLI application.

    Returns:
        Exit code.
    """

    parser = create_parser()

    args = parser.parse_args()

    result = get_validation_result(
        args.resume,
        args.schema
    )

    if args.json:

        import json

        print(
            json.dumps(
                result,
                indent=2,
                ensure_ascii=False
            )
        )

    else:

        if result["valid"]:

            print(
                "✓ ResumeSpec document is valid"
            )

        else:

            print(
                "✗ ResumeSpec validation failed\n"
            )

            for error in result["errors"]:
                print(
                    f"- {error}"
                )


    return (
        0
        if result["valid"]
        else 1
    )


if __name__ == "__main__":

    sys.exit(
        main()
    )
