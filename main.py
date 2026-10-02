"""YAML Merge Overlay — Deep-merge a YAML overlay onto a base file and write the result."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='yaml_merge_overlay',
        description='Deep-merge a YAML overlay onto a base file and write the result.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('YAML Merge Overlay')
    print('Base config plus local overrides.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
