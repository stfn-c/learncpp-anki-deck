#!/usr/bin/env python3
"""
Build script for LearnCPP Anki Deck

Reads all JSON files from deck/ folder and builds a versioned .apkg file
"""

import os
import sys
import re
from pathlib import Path

# Import the converter
sys.path.insert(0, os.path.dirname(__file__))
from json_to_anki import JsonToAnkiConverter


def get_next_version(build_dir: str) -> int:
    """Get the next version number by looking at existing builds"""
    build_path = Path(build_dir)

    if not build_path.exists():
        return 1

    # Find all version_X.apkg files
    version_files = list(build_path.glob("version_*.apkg"))

    if not version_files:
        return 1

    # Extract version numbers
    versions = []
    for f in version_files:
        match = re.search(r'version_(\d+)\.apkg', f.name)
        if match:
            versions.append(int(match.group(1)))

    return max(versions) + 1 if versions else 1


def count_json_files(deck_dir: str) -> int:
    """Count total JSON files in deck directory"""
    deck_path = Path(deck_dir)
    return len(list(deck_path.rglob("*.json")))


def build_deck(deck_dir: str, build_dir: str, version: int = None):
    """Build the Anki deck from JSON files"""

    # Ensure directories exist
    deck_path = Path(deck_dir)
    build_path = Path(build_dir)

    if not deck_path.exists():
        print(f"Error: Deck directory {deck_dir} does not exist!")
        return False

    build_path.mkdir(parents=True, exist_ok=True)

    # Count JSON files
    json_count = count_json_files(deck_dir)

    if json_count == 0:
        print(f"Error: No JSON files found in {deck_dir}")
        print("\nPlace your lesson JSON files in the deck/ folder organized by chapter:")
        print("  deck/chapter_0/0_1.json")
        print("  deck/chapter_1/1_1.json")
        print("  etc...")
        return False

    # Get version number
    if version is None:
        version = get_next_version(build_dir)

    output_file = build_path / f"version_{version}.apkg"

    print(f"Building LearnCPP Anki Deck")
    print(f"Version: {version}")
    print(f"Source: {deck_dir}")
    print(f"JSON files found: {json_count}")
    print(f"Output: {output_file}")
    print("-" * 60)

    # Create converter and build
    converter = JsonToAnkiConverter(deck_dir, str(output_file))
    converter.convert()

    print("-" * 60)
    print(f"✓ Build complete: {output_file}")
    print(f"✓ Version {version} created successfully")

    return True


def main():
    import argparse

    # Get script directory
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent

    deck_dir = project_dir / "deck"
    build_dir = project_dir / "build"

    parser = argparse.ArgumentParser(
        description='Build LearnCPP Anki Deck from JSON files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python build_deck.py                    # Auto-increment version
  python build_deck.py --version 2        # Build specific version
  python build_deck.py --deck ../deck     # Custom deck directory
        """
    )

    parser.add_argument(
        '--deck',
        default=str(deck_dir),
        help=f'Deck directory containing JSON files (default: {deck_dir})'
    )

    parser.add_argument(
        '--build',
        default=str(build_dir),
        help=f'Build output directory (default: {build_dir})'
    )

    parser.add_argument(
        '--version',
        type=int,
        help='Specific version number (default: auto-increment)'
    )

    args = parser.parse_args()

    success = build_deck(args.deck, args.build, args.version)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
