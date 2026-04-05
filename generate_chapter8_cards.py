#!/usr/bin/env python3
"""
Generate Anki flashcards for all Chapter 8 lessons.
Following HTML formatting rules and 40% cloze card distribution.
"""

import os
import json
import re

def escape_html(text):
    """Escape HTML special characters."""
    if not text:
        return text
    return (text.replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;'))

def read_all_lessons():
    """Read all Chapter 8 lesson files."""
    base_dir = '/Users/stefan/Desktop/learnCPP/learncpp-anki-deck/content/lessons/'
    chapter_dir = [d for d in os.listdir(base_dir) if '8' in d and 'Chapter' in d and '18' not in d and '28' not in d][0]
    full_path = os.path.join(base_dir, chapter_dir)

    lessons = {}
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'x']:
        file_path = os.path.join(full_path, f'8_{i}.json')
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                lessons[f'8_{i}'] = json.load(f)

    return lessons

def extract_text_content(data):
    """Extract all text content from lesson data."""
    texts = []
    if isinstance(data, dict):
        if 'text' in data and data['text']:
            texts.append(data['text'])
        if 'content' in data:
            for item in data.get('content', []):
                texts.extend(extract_text_content(item))
        if 'sections' in data:
            for section in data.get('sections', []):
                texts.extend(extract_text_content(section))
    elif isinstance(data, list):
        for item in data:
            texts.extend(extract_text_content(item))
    return texts

# Store all lessons data
lessons_data = read_all_lessons()

# Print summary
print("=" * 80)
print("CHAPTER 8 LESSONS LOADED")
print("=" * 80)
for key in sorted(lessons_data.keys(), key=lambda x: (len(x), x)):
    title = lessons_data[key].get('title', 'No title')
    print(f"{key}: {title}")
print(f"\nTotal lessons: {len(lessons_data)}")
print("=" * 80)

# Export for external use
with open('/tmp/chapter8_lessons.json', 'w') as f:
    json.dump(lessons_data, f, indent=2)

print("\nLesson data exported to /tmp/chapter8_lessons.json")
print("Ready to generate flashcards!")
