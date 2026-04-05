#!/usr/bin/env python3
"""
Generate Anki flashcards for Chapter 21 of LearnCPP
Following the CARD_GENERATION_PROMPT.md guidelines
"""

import os
import glob
import json
import re
from typing import List, Dict, Any

def escape_html(text: str) -> str:
    """Escape HTML special characters"""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;'))

def format_code(code: str) -> str:
    """Format code with HTML escaping"""
    return escape_html(code)

def create_card_id(chapter: int, lesson: int, card_num: int) -> str:
    """Create card ID in format ch{chapter}_{lesson}_{number}"""
    return f"ch{chapter}_{lesson}_{card_num:03d}"

def load_lesson(filepath: str) -> Dict[str, Any]:
    """Load lesson JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_deck(filepath: str, deck_data: Dict[str, Any]) -> None:
    """Save deck JSON file"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(deck_data, f, indent=2, ensure_ascii=False)

# Card generation will be done lesson by lesson
# This is a template - actual implementation will read from lessons

def main():
    # Find Chapter 21 directory
    lesson_dirs = glob.glob('/Users/stefan/Desktop/learnCPP/learncpp-anki-deck/content/lessons/Chapter*21*')
    if not lesson_dirs:
        print("Chapter 21 directory not found!")
        return

    chapter_dir = lesson_dirs[0]
    lesson_files = sorted(glob.glob(os.path.join(chapter_dir, '*.json')))

    output_dir = '/Users/stefan/Desktop/learnCPP/learncpp-anki-deck/deck/chapter_21'

    print(f"Found {len(lesson_files)} lesson files in Chapter 21")
    print(f"Output directory: {output_dir}")

    # Process each lesson file
    for lesson_file in lesson_files:
        basename = os.path.basename(lesson_file)
        print(f"\nProcessing: {basename}")

        # Load lesson data
        try:
            lesson_data = load_lesson(lesson_file)
            print(f"  Loaded: {lesson_data.get('title', 'Unknown')}")
        except Exception as e:
            print(f"  Error loading {basename}: {e}")
            continue

if __name__ == '__main__':
    main()
