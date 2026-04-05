#!/usr/bin/env python3
"""
Generate Anki flashcards from LearnCPP.com lesson JSON files.
Following the guidelines in CARD_GENERATION_PROMPT.md
"""
import json
import subprocess
import os
import re

def read_lesson_file(filepath):
    """Read a lesson JSON file using cat command to handle special characters"""
    result = subprocess.run(
        ['cat', filepath],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise Exception(f"Failed to read {filepath}: {result.stderr}")
    return json.loads(result.stdout)

def extract_code_examples(sections):
    """Extract code examples from lesson sections"""
    code_examples = []
    for section in sections:
        if 'content' in section:
            for item in section['content']:
                if 'code' in item:
                    code_examples.append(item['code'])
    return code_examples

def extract_quiz_questions(quiz):
    """Extract quiz questions from lesson"""
    return quiz if quiz else []

def create_card_id(chapter, lesson, card_num):
    """Create card ID in format ch{chapter}_{lesson}_{number}"""
    return f"ch{chapter}_{lesson}_{card_num:03d}"

def generate_flashcards_for_lesson(lesson_data, lesson_number):
    """Generate flashcards for a single lesson"""
    cards = []
    chapter = "1"

    # Extract information from lesson
    title = lesson_data.get('title', '')
    sections = lesson_data.get('sections', [])
    quiz = lesson_data.get('quiz', [])

    card_counter = 1

    # Lesson 1.1: Statements and the structure of a program
    if lesson_number == "1":
        # Basic cards
        cards.append({
            "id": create_card_id(chapter, lesson_number, card_counter),
            "lesson": f"1.{lesson_number}",
            "type": "basic",
            "tags": ["cpp", "fundamentals", "statements"],
            "front": "What is a statement in C++?",
            "back": "A type of instruction that causes the program to perform some action. It is the smallest independent unit of computation in C++.",
            "source": "1.1 - Statements and the structure of a program",
            "difficulty": "easy"
        })
        card_counter += 1

        cards.append({
            "id": create_card_id(chapter, lesson_number, card_counter),
            "lesson": f"1.{lesson_number}",
            "type": "basic",
            "tags": ["cpp", "fundamentals", "syntax"],
            "front": "What punctuation mark do most C++ statements end with?",
            "back": "A semicolon (;)",
            "source": "1.1 - Statements and the structure of a program",
            "difficulty": "easy"
        })
        card_counter += 1

        cards.append({
            "id": create_card_id(chapter, lesson_number, card_counter),
            "lesson": f"1.{lesson_number}",
            "type": "basic",
            "tags": ["cpp", "functions", "fundamentals"],
            "front": "What is a function in C++?",
            "back": "A collection of statements that get executed sequentially (in order, from top to bottom).",
            "source": "1.1 - Statements and the structure of a program",
            "difficulty": "easy"
        })
        card_counter += 1

        cards.append({
            "id": create_card_id(chapter, lesson_number, card_counter),
            "lesson": f"1.{lesson_number}",
            "type": "basic",
            "tags": ["cpp", "functions", "main"],
            "front": "What function must every C++ program have?",
            "back": "A function named main (all lower case letters)",
            "source": "1.1 - Statements and the structure of a program",
            "difficulty": "easy"
        })
        card_counter += 1

        # Cloze cards
        cards.append({
            "id": create_card_id(chapter, lesson_number, card_counter),
            "lesson": f"1.{lesson_number}",
            "type": "cloze",
            "tags": ["cpp", "main", "syntax"],
            "text": "The basic structure of a C++ program is: {{c1::int main()}}\n{{c2::{\n   // statements\n   return 0;\n}}}",
            "source": "1.1 - Statements and the structure of a program",
            "difficulty": "easy"
        })
        card_counter += 1

        cards.append({
            "id": create_card_id(chapter, lesson_number, card_counter),
            "lesson": f"1.{lesson_number}",
            "type": "cloze",
            "tags": ["cpp", "iostream", "preprocessor"],
            "text": "To use std::cout for console output, you must include {{c1::#include <iostream>}}",
            "source": "1.1 - Statements and the structure of a program",
            "difficulty": "easy"
        })
        card_counter += 1

        # Code cards
        cards.append({
            "id": create_card_id(chapter, lesson_number, card_counter),
            "lesson": f"1.{lesson_number}",
            "type": "code",
            "tags": ["cpp", "hello-world", "output"],
            "question": "What does this program output?",
            "code": '#include <iostream>\n\nint main()\n{\n   std::cout << "Hello world!";\n   return 0;\n}',
            "answer": "Hello world!",
            "explanation": 'The std::cout statement sends the text "Hello world!" to the console for display.',
            "source": "1.1 - Statements and the structure of a program",
            "difficulty": "easy"
        })
        card_counter += 1

        cards.append({
            "id": create_card_id(chapter, lesson_number, card_counter),
            "lesson": f"1.{lesson_number}",
            "type": "code",
            "tags": ["cpp", "syntax", "common-mistakes"],
            "question": "What's wrong with this code?",
            "code": '#include <iostream>\n\nint main()\n{\n   std::cout << "Hello world!"\n   return 0;\n}',
            "answer": "Missing semicolon after the std::cout statement",
            "explanation": "Most statements in C++ must end with a semicolon. The compiler will produce a syntax error when the semicolon is missing.",
            "source": "1.1 - Statements and the structure of a program",
            "difficulty": "easy"
        })
        card_counter += 1

        # Concept cards
        cards.append({
            "id": create_card_id(chapter, lesson_number, card_counter),
            "lesson": f"1.{lesson_number}",
            "type": "concept",
            "tags": ["cpp", "main", "fundamentals"],
            "concept": "The main() function",
            "explanation": "Every C++ program must have a special function named main. When the program runs, the statements inside main are executed in sequential order. Programs typically terminate after the last statement in main has executed.",
            "examples": [
                "int main()          // function declaration",
                "{                   // start of function body",
                "   // statements",
                "   return 0;        // return value to OS",
                "}                   // end of function body"
            ],
            "source": "1.1 - Statements and the structure of a program",
            "difficulty": "medium"
        })
        card_counter += 1

        cards.append({
            "id": create_card_id(chapter, lesson_number, card_counter),
            "lesson": f"1.{lesson_number}",
            "type": "concept",
            "tags": ["cpp", "return", "best-practices"],
            "concept": "Return value from main()",
            "explanation": 'When a program finishes, it sends a value back to the operating system to indicate success or failure. Returning 0 means "everything went okay!"',
            "examples": [
                "return 0;  // indicates successful execution",
                "// non-zero values indicate errors"
            ],
            "source": "1.1 - Statements and the structure of a program",
            "difficulty": "medium"
        })
        card_counter += 1

        # Reverse cards
        cards.append({
            "id": create_card_id(chapter, lesson_number, card_counter),
            "lesson": f"1.{lesson_number}",
            "type": "reverse",
            "tags": ["cpp", "terminology"],
            "front": "identifier",
            "back": "The name of a function, variable, object, type, or template",
            "source": "1.1 - Statements and the structure of a program",
            "difficulty": "easy"
        })
        card_counter += 1

        cards.append({
            "id": create_card_id(chapter, lesson_number, card_counter),
            "lesson": f"1.{lesson_number}",
            "type": "reverse",
            "tags": ["cpp", "errors"],
            "front": "syntax error",
            "back": "Occurs when your program violates the grammar rules of the C++ language",
            "source": "1.1 - Statements and the structure of a program",
            "difficulty": "easy"
        })
        card_counter += 1

    return {
        "chapter": "Chapter 1",
        "chapter_title": "C++ Basics",
        "lesson": f"1.{lesson_number}",
        "lesson_title": title,
        "total_cards": len(cards),
        "cards": cards
    }

def main():
    # Get all Chapter 1 lesson files
    result = subprocess.run(
        ['find', 'learncpp-anki-deck/content/lessons', '-name', '1_*.json', '-type', 'f'],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"Error finding lesson files: {result.stderr}")
        return

    lesson_files = sorted(result.stdout.strip().split('\n'))

    print(f"Found {len(lesson_files)} lesson files")

    total_cards = 0
    processed_lessons = 0

    # Process only lesson 1_1 for now as a test
    for filepath in lesson_files[:1]:  # Start with just the first one
        # Extract lesson number from filename
        filename = os.path.basename(filepath)
        lesson_num = filename.replace('1_', '').replace('.json', '')

        print(f"\\nProcessing {filepath}...")

        try:
            # Read lesson data
            lesson_data = read_lesson_file(filepath)

            # Generate flashcards
            output = generate_flashcards_for_lesson(lesson_data, lesson_num)

            # Write output file
            output_dir = 'learncpp-anki-deck/deck/chapter_1'
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, f'1_{lesson_num}.json')

            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(output, f, indent=2, ensure_ascii=False)

            print(f"Generated {output['total_cards']} cards for lesson 1.{lesson_num}")
            print(f"Output written to {output_file}")

            total_cards += output['total_cards']
            processed_lessons += 1

        except Exception as e:
            print(f"Error processing {filepath}: {e}")
            import traceback
            traceback.print_exc()

    print(f"\\n=== Summary ===")
    print(f"Processed {processed_lessons} lessons")
    print(f"Generated {total_cards} total cards")

if __name__ == '__main__':
    main()
