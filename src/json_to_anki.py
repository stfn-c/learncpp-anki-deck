#!/usr/bin/env python3
"""
Convert AI-generated JSON cards to Anki deck with subdecks for each chapter
"""

import json
import os
import genanki
import random
import re
from typing import Dict, List, Any
from pathlib import Path

class JsonToAnkiConverter:
    def __init__(self, json_dir: str, output_file: str = "LearnCPP_Complete.apkg"):
        self.json_dir = json_dir
        self.output_file = output_file
        self.media_files = []

        # Main deck
        self.main_deck_id = random.randrange(1 << 30, 1 << 31)
        self.main_deck = genanki.Deck(
            self.main_deck_id,
            'LearnCPP'
        )

        # Store subdecks - both chapter and lesson level
        self.chapter_decks = {}
        self.lesson_decks = {}

        # Define note models for each card type
        self._create_note_models()

    def _create_note_models(self):
        """Create Anki note models for each card type"""

        # Basic Q&A Model
        self.basic_model = genanki.Model(
            random.randrange(1 << 30, 1 << 31),
            'LearnCPP Basic',
            fields=[
                {'name': 'Front'},
                {'name': 'Back'},
                {'name': 'Source'},
            ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '''
                        <div class="question">{{Front}}</div>
                        <div class="source">{{Source}}</div>
                    ''',
                    'afmt': '''
                        {{FrontSide}}
                        <hr id="answer">
                        <div class="answer">{{Back}}</div>
                    ''',
                },
            ],
            css=self._get_css()
        )

        # Cloze Model
        self.cloze_model = genanki.Model(
            random.randrange(1 << 30, 1 << 31),
            'LearnCPP Cloze',
            model_type=genanki.Model.CLOZE,
            fields=[
                {'name': 'Text'},
                {'name': 'Source'},
                {'name': 'Extra'},
            ],
            templates=[
                {
                    'name': 'Cloze',
                    'qfmt': '''
                        <div class="cloze">{{cloze:Text}}</div>
                        <div class="source">{{Source}}</div>
                    ''',
                    'afmt': '''
                        <div class="cloze">{{cloze:Text}}</div>
                        <div class="source">{{Source}}</div>
                        {{#Extra}}
                        <hr>
                        <div class="extra">{{Extra}}</div>
                        {{/Extra}}
                    ''',
                },
            ],
            css=self._get_css()
        )

        # Code Model
        self.code_model = genanki.Model(
            random.randrange(1 << 30, 1 << 31),
            'LearnCPP Code',
            fields=[
                {'name': 'Question'},
                {'name': 'Code'},
                {'name': 'Answer'},
                {'name': 'Explanation'},
                {'name': 'Source'},
            ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '''
                        <div class="question">{{Question}}</div>
                        <pre class="code">{{Code}}</pre>
                        <div class="source">{{Source}}</div>
                    ''',
                    'afmt': '''
                        {{FrontSide}}
                        <hr id="answer">
                        <div class="answer">{{Answer}}</div>
                        {{#Explanation}}
                        <div class="explanation">{{Explanation}}</div>
                        {{/Explanation}}
                    ''',
                },
            ],
            css=self._get_css()
        )

        # Reverse Model (bidirectional)
        self.reverse_model = genanki.Model(
            random.randrange(1 << 30, 1 << 31),
            'LearnCPP Reverse',
            fields=[
                {'name': 'Front'},
                {'name': 'Back'},
                {'name': 'Source'},
            ],
            templates=[
                {
                    'name': 'Forward',
                    'qfmt': '''
                        <div class="question">{{Front}}</div>
                        <div class="source">{{Source}}</div>
                    ''',
                    'afmt': '''
                        {{FrontSide}}
                        <hr id="answer">
                        <div class="answer">{{Back}}</div>
                    ''',
                },
                {
                    'name': 'Reverse',
                    'qfmt': '''
                        <div class="question">{{Back}}</div>
                        <div class="source">{{Source}}</div>
                    ''',
                    'afmt': '''
                        {{FrontSide}}
                        <hr id="answer">
                        <div class="answer">{{Front}}</div>
                    ''',
                },
            ],
            css=self._get_css()
        )

        # Concept Model
        self.concept_model = genanki.Model(
            random.randrange(1 << 30, 1 << 31),
            'LearnCPP Concept',
            fields=[
                {'name': 'Concept'},
                {'name': 'Explanation'},
                {'name': 'Examples'},
                {'name': 'Source'},
            ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '''
                        <div class="concept-q">Explain: {{Concept}}</div>
                        <div class="source">{{Source}}</div>
                    ''',
                    'afmt': '''
                        {{FrontSide}}
                        <hr id="answer">
                        <div class="explanation">{{Explanation}}</div>
                        {{#Examples}}
                        <div class="examples">
                            <strong>Examples:</strong>
                            <pre>{{Examples}}</pre>
                        </div>
                        {{/Examples}}
                    ''',
                },
            ],
            css=self._get_css()
        )

    def _get_css(self):
        """Get CSS styling for cards (minimalist, no gradients or rounded corners)"""
        return '''
            .card {
                font-family: 'SF Mono', Monaco, 'Cascadia Code', monospace;
                font-size: 16px;
                text-align: left;
                color: #333;
                background-color: white;
                padding: 20px;
                max-width: 800px;
                margin: 0 auto;
            }

            .question, .concept-q {
                font-size: 18px;
                margin-bottom: 15px;
                color: #000;
                font-weight: 500;
            }

            .answer, .explanation {
                font-size: 16px;
                line-height: 1.6;
                color: #333;
            }

            .source {
                font-size: 12px;
                color: #666;
                margin-top: 15px;
                padding-top: 10px;
                border-top: 1px solid #e0e0e0;
            }

            .code, pre {
                font-family: 'SF Mono', Monaco, 'Cascadia Code', monospace;
                background: #f5f5f5;
                border: 1px solid #ddd;
                padding: 15px;
                margin: 15px 0;
                overflow-x: auto;
                font-size: 14px;
                line-height: 1.4;
            }

            .cloze {
                font-size: 17px;
                line-height: 1.6;
                margin-bottom: 15px;
            }

            .cloze .cloze-deletion {
                font-weight: bold;
                color: #0066cc;
            }

            .examples {
                margin-top: 15px;
                padding-top: 15px;
                border-top: 1px solid #e0e0e0;
            }

            .extra {
                font-size: 14px;
                color: #555;
                margin-top: 15px;
            }

            hr {
                border: none;
                border-top: 1px solid #ddd;
                margin: 20px 0;
            }

            strong {
                font-weight: 600;
            }

            /* Night mode support */
            .nightMode .card {
                background-color: #1e1e1e;
                color: #e0e0e0;
            }

            .nightMode .question, .nightMode .concept-q {
                color: #fff;
            }

            .nightMode .answer, .nightMode .explanation {
                color: #e0e0e0;
            }

            .nightMode .source {
                color: #999;
                border-top-color: #444;
            }

            .nightMode .code, .nightMode pre {
                background: #2d2d2d;
                border-color: #444;
                color: #e0e0e0;
            }

            .nightMode hr {
                border-top-color: #444;
            }

            .nightMode .examples {
                border-top-color: #444;
            }
        '''

    def _get_or_create_lesson_deck(self, chapter_name: str, lesson_num: str, lesson_source: str) -> genanki.Deck:
        """Get or create a subdeck for a specific lesson"""
        # Create chapter deck if doesn't exist
        if chapter_name not in self.chapter_decks:
            deck_id = random.randrange(1 << 30, 1 << 31)
            deck_name = f"LearnCPP::{chapter_name}"
            self.chapter_decks[chapter_name] = genanki.Deck(deck_id, deck_name)

        # Create unique key for lesson
        lesson_key = f"{chapter_name}::{lesson_num}"

        if lesson_key not in self.lesson_decks:
            # Generate unique deck ID
            deck_id = random.randrange(1 << 30, 1 << 31)

            # Extract lesson title from source (format: "1.1 - Title")
            lesson_title = lesson_source
            if ' - ' in lesson_source:
                lesson_title = lesson_source.split(' - ', 1)[1]

            # Create hierarchical deck name
            deck_name = f"LearnCPP::{chapter_name}::{lesson_num} - {lesson_title}"
            self.lesson_decks[lesson_key] = genanki.Deck(deck_id, deck_name)

        return self.lesson_decks[lesson_key]

    def _convert_cloze_format(self, text: str) -> str:
        """Convert {{c1::text}} format to Anki's {{c1::text}} format"""
        # Already in correct format, just ensure it's properly formatted
        return text

    def _create_note_from_card(self, card: Dict[str, Any]) -> genanki.Note:
        """Create an Anki note from a card dictionary"""
        card_type = card.get('type', 'basic')
        source = card.get('source', '')

        if card_type == 'basic':
            return genanki.Note(
                model=self.basic_model,
                fields=[
                    card.get('front', ''),
                    card.get('back', ''),
                    source
                ],
                tags=card.get('tags', [])
            )

        elif card_type == 'cloze':
            # Convert cloze format if needed
            cloze_text = self._convert_cloze_format(card.get('text', ''))
            return genanki.Note(
                model=self.cloze_model,
                fields=[
                    cloze_text,
                    source,
                    card.get('extra', '')
                ],
                tags=card.get('tags', [])
            )

        elif card_type == 'code':
            # Fallback: if agents used front/back instead of question/answer
            question = card.get('question', card.get('front', ''))
            answer = card.get('answer', card.get('back', ''))

            return genanki.Note(
                model=self.code_model,
                fields=[
                    question,
                    card.get('code', ''),
                    answer,
                    card.get('explanation', ''),
                    source
                ],
                tags=card.get('tags', [])
            )

        elif card_type == 'reverse':
            return genanki.Note(
                model=self.reverse_model,
                fields=[
                    card.get('front', ''),
                    card.get('back', ''),
                    source
                ],
                tags=card.get('tags', [])
            )

        elif card_type == 'concept':
            # Fallback: if agents used front/back instead of concept/explanation
            concept = card.get('concept', card.get('front', ''))
            explanation = card.get('explanation', card.get('back', ''))

            # Format examples as a single string
            examples = card.get('examples', [])
            if isinstance(examples, list):
                examples_text = '\n'.join(examples)
            else:
                examples_text = str(examples) if examples else ''

            return genanki.Note(
                model=self.concept_model,
                fields=[
                    concept,
                    explanation,
                    examples_text,
                    source
                ],
                tags=card.get('tags', [])
            )

        else:
            # Default to basic if unknown type
            return genanki.Note(
                model=self.basic_model,
                fields=[
                    card.get('front', card.get('question', '')),
                    card.get('back', card.get('answer', '')),
                    source
                ],
                tags=card.get('tags', [])
            )

    def convert(self):
        """Convert all JSON files to Anki deck"""
        json_path = Path(self.json_dir)

        if not json_path.exists():
            print(f"JSON directory {self.json_dir} does not exist!")
            return

        # Find all JSON files (can be organized by chapter folders or flat)
        json_files = sorted(json_path.rglob("*.json"))

        if not json_files:
            print(f"No JSON files found in {self.json_dir}")
            return

        total_cards = 0
        lessons_processed = 0

        for json_file in json_files:
            print(f"Processing {json_file.name}...")

            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # Get lesson info
                chapter_name = data.get('chapter', 'Unknown')
                chapter_title = data.get('chapter_title', '')
                lesson_num = data.get('lesson', '')
                lesson_title = data.get('lesson_title', '')

                # Format chapter deck name
                if chapter_title:
                    chapter_deck_name = f"{chapter_name} - {chapter_title}"
                else:
                    chapter_deck_name = chapter_name

                # Process each card
                cards = data.get('cards', [])
                lesson_card_count = 0

                for card in cards:
                    try:
                        # Get the source for lesson title if not provided
                        source = card.get('source', f"{lesson_num} - {lesson_title}")

                        # Get or create lesson deck
                        lesson_deck = self._get_or_create_lesson_deck(
                            chapter_deck_name,
                            card.get('lesson', lesson_num),
                            source
                        )

                        # Create and add note
                        note = self._create_note_from_card(card)
                        lesson_deck.add_note(note)
                        lesson_card_count += 1
                        total_cards += 1
                    except Exception as e:
                        print(f"  Error creating card {card.get('id', 'unknown')}: {e}")

                print(f"  Added {lesson_card_count} cards from {lesson_num}")
                lessons_processed += 1

            except Exception as e:
                print(f"  Error processing {json_file.name}: {e}")

        # Create package with all decks
        all_decks = [self.main_deck] + list(self.chapter_decks.values()) + list(self.lesson_decks.values())
        package = genanki.Package(all_decks)

        # Add media files if any
        if self.media_files:
            package.media_files = self.media_files

        # Write the package
        package.write_to_file(self.output_file)

        print(f"\nSuccessfully created Anki deck: {self.output_file}")
        print(f"Total cards: {total_cards}")
        print(f"Lessons processed: {lessons_processed}")
        print(f"Chapters: {len(self.chapter_decks)}")
        print(f"Lesson subdecks: {len(self.lesson_decks)}")

        # Print subdeck summary
        print("\nChapter decks created:")
        for chapter_name in sorted(self.chapter_decks.keys()):
            print(f"  - {chapter_name}")

        print("\nLesson subdecks created:")
        for lesson_name in sorted(self.lesson_decks.keys()):
            deck = self.lesson_decks[lesson_name]
            print(f"  - {deck.name}")

    def convert_single_chapter(self, chapter_file: str):
        """Convert a single chapter JSON to see if it works"""
        print(f"Testing with {chapter_file}...")

        try:
            with open(chapter_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Get chapter info
            chapter_name = data.get('chapter', 'Test Chapter')
            chapter_title = data.get('chapter_title', 'Test')

            # Format chapter deck name
            deck_name = f"{chapter_name} - {chapter_title}"

            # Create test deck
            test_deck = genanki.Deck(
                random.randrange(1 << 30, 1 << 31),
                f"LearnCPP::{deck_name}"
            )

            # Process cards
            cards = data.get('cards', [])
            for card in cards[:5]:  # Test with first 5 cards
                note = self._create_note_from_card(card)
                test_deck.add_note(note)
                print(f"  Added card: {card.get('id')}")

            # Create test package
            package = genanki.Package([test_deck])
            test_output = "test_chapter.apkg"
            package.write_to_file(test_output)

            print(f"Test deck created: {test_output}")

        except Exception as e:
            print(f"Error in test: {e}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Convert AI-generated JSON to Anki deck')
    parser.add_argument(
        'json_dir',
        help='Directory containing JSON files (one per chapter)'
    )
    parser.add_argument(
        '-o', '--output',
        default='LearnCPP_Complete.apkg',
        help='Output Anki package file'
    )
    parser.add_argument(
        '-t', '--test',
        help='Test with a single chapter file'
    )

    args = parser.parse_args()

    converter = JsonToAnkiConverter(args.json_dir, args.output)

    if args.test:
        converter.convert_single_chapter(args.test)
    else:
        converter.convert()


if __name__ == "__main__":
    main()