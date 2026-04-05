#!/usr/bin/env python3
"""
Generate Anki flashcards for all Chapter 8 lessons from LearnCPP.com
Following the guidelines in CARD_GENERATION_PROMPT.md
"""

import os
import json
import re

def find_chapter_dir(base_path, chapter_marker='8_1.json'):
    """Find the Chapter 8 directory (handles special characters in directory names)"""
    for item in os.listdir(base_path):
        full_path = os.path.join(base_path, item)
        if os.path.isdir(full_path):
            try:
                if chapter_marker in os.listdir(full_path):
                    return full_path
            except:
                pass
    return None

def extract_code_examples(sections):
    """Extract code examples from lesson sections"""
    code_examples = []
    for section in sections:
        for content in section.get('content', []):
            if 'code' in content:
                code_examples.append(content['code'])
    return code_examples

def generate_cards_8_2(lesson):
    """Generate cards for lesson 8.2 - If statements and blocks"""
    cards = []
    card_num = 1

    # Card 1: Block definition
    cards.append({
        "id": f"ch8_2_{card_num:03d}",
        "lesson": "8.2",
        "type": "basic",
        "tags": ["cpp", "blocks", "scope"],
        "front": "What is a block (compound statement) in C++?",
        "back": "A group of zero or more statements treated by the compiler as if it were a single statement, defined using curly braces {}.",
        "source": "8.2 - If statements and blocks",
        "difficulty": "easy"
    })
    card_num += 1

    # Card 2: Block scope
    cards.append({
        "id": f"ch8_2_{card_num:03d}",
        "lesson": "8.2",
        "type": "basic",
        "tags": ["cpp", "blocks", "scope"],
        "front": "What is the scope of variables declared inside a block?",
        "back": "Variables declared inside a block have block scope and can only be accessed within that block (and nested blocks).",
        "source": "8.2 - If statements and blocks",
        "difficulty": "easy"
    })
    card_num += 1

    # Card 3: If statement syntax
    cards.append({
        "id": f"ch8_2_{card_num:03d}",
        "lesson": "8.2",
        "type": "cloze",
        "tags": ["cpp", "conditionals", "syntax"],
        "text": "The syntax for an if statement is: {{c1::if (condition)}} {{c2::statement;}}",
        "source": "8.2 - If statements and blocks",
        "difficulty": "easy"
    })
    card_num += 1

    # Card 4: Dangling else
    cards.append({
        "id": f"ch8_2_{card_num:03d}",
        "lesson": "8.2",
        "type": "basic",
        "tags": ["cpp", "conditionals", "common-mistakes"],
        "front": "What is the dangling else problem?",
        "back": "When an else statement could match multiple if statements, it matches the closest unmatched if statement in the same block.",
        "source": "8.2 - If statements and blocks",
        "difficulty": "medium"
    })
    card_num += 1

    # Card 5: Best practice - blocks
    cards.append({
        "id": f"ch8_2_{card_num:03d}",
        "lesson": "8.2",
        "type": "concept",
        "tags": ["cpp", "blocks", "best-practices"],
        "concept": "Always Use Blocks with If Statements",
        "explanation": "Even for single statements, always use blocks {} with if/else statements to prevent errors when adding more statements later.",
        "examples": [
            "// Bad: no block",
            "if (x > 5)",
            "    std::cout << \"x is greater\";",
            "",
            "// Good: uses block",
            "if (x > 5)",
            "{",
            "    std::cout << \"x is greater\";",
            "}"
        ],
        "source": "8.2 - If statements and blocks",
        "difficulty": "easy"
    })
    card_num += 1

    # Card 6: Null statement
    cards.append({
        "id": f"ch8_2_{card_num:03d}",
        "lesson": "8.2",
        "type": "code",
        "tags": ["cpp", "conditionals", "common-mistakes"],
        "question": "What's wrong with this code?",
        "code": "if (x > 5);\n{\n    std::cout << \"x is greater\";  \n}",
        "answer": "The semicolon after the if statement creates a null statement. The block will always execute regardless of the condition.",
        "explanation": "The semicolon terminates the if statement with an empty statement. The block is not part of the if statement.",
        "source": "8.2 - If statements and blocks",
        "difficulty": "medium"
    })
    card_num += 1

    # Card 7: Nested if statements
    cards.append({
        "id": f"ch8_2_{card_num:03d}",
        "lesson": "8.2",
        "type": "basic",
        "tags": ["cpp", "conditionals", "nesting"],
        "front": "Can if statements be nested inside other if statements?",
        "back": "Yes, if statements can be nested inside other if statements to any depth, though deep nesting can make code harder to read.",
        "source": "8.2 - If statements and blocks",
        "difficulty": "easy"
    })
    card_num += 1

    # Card 8: Block with multiple statements
    cards.append({
        "id": f"ch8_2_{card_num:03d}",
        "lesson": "8.2",
        "type": "cloze",
        "tags": ["cpp", "blocks", "syntax"],
        "text": "A block can contain {{c1::zero or more}} statements.",
        "source": "8.2 - If statements and blocks",
        "difficulty": "easy"
    })
    card_num += 1

    # Card 9: If-else syntax
    cards.append({
        "id": f"ch8_2_{card_num:03d}",
        "lesson": "8.2",
        "type": "cloze",
        "tags": ["cpp", "conditionals", "syntax"],
        "text": "The if-else statement syntax is: if (condition) {{c1::true_statement}} else {{c2::false_statement}}",
        "source": "8.2 - If statements and blocks",
        "difficulty": "easy"
    })
    card_num += 1

    # Card 10: Block limitations
    cards.append({
        "id": f"ch8_2_{card_num:03d}",
        "lesson": "8.2",
        "type": "basic",
        "tags": ["cpp", "blocks", "scope"],
        "front": "Can you access a variable declared inside a block from outside that block?",
        "back": "No, variables declared inside a block go out of scope at the end of the block and cannot be accessed from outside.",
        "source": "8.2 - If statements and blocks",
        "difficulty": "easy"
    })
    card_num += 1

    # Card 11: Empty block
    cards.append({
        "id": f"ch8_2_{card_num:03d}",
        "lesson": "8.2",
        "type": "basic",
        "tags": ["cpp", "blocks", "syntax"],
        "front": "Is an empty block {} valid in C++?",
        "back": "Yes, an empty block is valid and does nothing when executed.",
        "source": "8.2 - If statements and blocks",
        "difficulty": "easy"
    })
    card_num += 1

    # Card 12: Implicit block
    cards.append({
        "id": f"ch8_2_{card_num:03d}",
        "lesson": "8.2",
        "type": "concept",
        "tags": ["cpp", "blocks", "gotchas"],
        "concept": "Implicit Blocks vs Explicit Blocks",
        "explanation": "Without curly braces, only the next single statement is part of the if/else. Additional statements will not be conditional.",
        "examples": [
            "// Implicit: only first statement is conditional",
            "if (x > 5)",
            "    std::cout << \"Greater\";",
            "    std::cout << \"Always runs\";  // NOT part of if!",
            "",
            "// Explicit: both statements are conditional",
            "if (x > 5)",
            "{",
            "    std::cout << \"Greater\";",
            "    std::cout << \"Conditional\";  // Part of if",
            "}"
        ],
        "source": "8.2 - If statements and blocks",
        "difficulty": "medium"
    })

    return cards

def generate_cards_8_3(lesson):
    """Generate cards for lesson 8.3 - Common if statement problems"""
    cards = []
    card_num = 1

    # Card 1: Nested if vs logical AND
    cards.append({
        "id": f"ch8_3_{card_num:03d}",
        "lesson": "8.3",
        "type": "concept",
        "tags": ["cpp", "conditionals", "best-practices"],
        "concept": "Nested If vs Logical AND",
        "explanation": "Use logical AND (&&) instead of nested if statements for better readability when checking multiple conditions.",
        "examples": [
            "// Nested if (harder to read)",
            "if (x > 5)",
            "{",
            "    if (y < 10)",
            "    {",
            "        doSomething();",
            "    }",
            "}",
            "",
            "// Logical AND (clearer)",
            "if (x > 5 && y < 10)",
            "{",
            "    doSomething();",
            "}"
        ],
        "source": "8.3 - Common if statement problems",
        "difficulty": "easy"
    })
    card_num += 1

    # Card 2: Equality vs assignment
    cards.append({
        "id": f"ch8_3_{card_num:03d}",
        "lesson": "8.3",
        "type": "code",
        "tags": ["cpp", "conditionals", "common-mistakes"],
        "question": "What's wrong with this code?",
        "code": "int x{5};\nif (x = 10)\n{\n    std::cout << \"x is 10\";\n}",
        "answer": "Using assignment operator (=) instead of equality operator (==). This assigns 10 to x and evaluates to true.",
        "explanation": "The condition uses = (assignment) instead of == (equality). The assignment returns 10 (truthy), so the if statement always executes and x is modified.",
        "source": "8.3 - Common if statement problems",
        "difficulty": "medium"
    })
    card_num += 1

    # Card 3: Confusing == and =
    cards.append({
        "id": f"ch8_3_{card_num:03d}",
        "lesson": "8.3",
        "type": "basic",
        "tags": ["cpp", "operators", "common-mistakes"],
        "front": "What's the difference between = and == in C++?",
        "back": "= is the assignment operator (assigns a value to a variable)\n== is the equality operator (compares two values for equality)",
        "source": "8.3 - Common if statement problems",
        "difficulty": "easy"
    })
    card_num += 1

    # Card 4: Constant on left side
    cards.append({
        "id": f"ch8_3_{card_num:03d}",
        "lesson": "8.3",
        "type": "concept",
        "tags": ["cpp", "conditionals", "best-practices"],
        "concept": "Place Constants on Left Side of Comparison",
        "explanation": "Placing constants on the left side of comparisons can catch accidental assignment errors at compile time.",
        "examples": [
            "// Traditional way",
            "if (x == 5)  // If you typo: if (x = 5), compiles but wrong!",
            "",
            "// Safer way (Yoda conditions)",
            "if (5 == x)  // If you typo: if (5 = x), won't compile!",
            "",
            "// Note: Modern compilers warn about if (x = 5) anyway"
        ],
        "source": "8.3 - Common if statement problems",
        "difficulty": "medium"
    })
    card_num += 1

    # Card 5: Multiple statements without block
    cards.append({
        "id": f"ch8_3_{card_num:03d}",
        "lesson": "8.3",
        "type": "code",
        "tags": ["cpp", "conditionals", "common-mistakes"],
        "question": "What does this code print when x is 3?",
        "code": "int x{3};\nif (x > 5)\n    std::cout << \"x is greater than 5\\n\";\n    std::cout << \"This always prints\\n\";",
        "answer": "This always prints",
        "explanation": "Without braces, only the first statement is part of the if. The second statement always executes regardless of the condition.",
        "source": "8.3 - Common if statement problems",
        "difficulty": "medium"
    })
    card_num += 1

    # Card 6: Non-Boolean conditionals
    cards.append({
        "id": f"ch8_3_{card_num:03d}",
        "lesson": "8.3",
        "type": "basic",
        "tags": ["cpp", "conditionals", "type-conversion"],
        "front": "What happens when you use a non-boolean value in an if condition?",
        "back": "The value is implicitly converted to boolean: 0 becomes false, any non-zero value becomes true.",
        "source": "8.3 - Common if statement problems",
        "difficulty": "medium"
    })
    card_num += 1

    # Card 7: Semicolon after if
    cards.append({
        "id": f"ch8_3_{card_num:03d}",
        "lesson": "8.3",
        "type": "code",
        "tags": ["cpp", "conditionals", "common-mistakes"],
        "question": "What's the problem with this code?",
        "code": "if (x > 5);\n    std::cout << \"x is greater than 5\";",
        "answer": "The semicolon after if creates a null statement. The cout always executes.",
        "explanation": "The semicolon terminates the if with an empty statement. The cout is a separate statement that always runs.",
        "source": "8.3 - Common if statement problems",
        "difficulty": "medium"
    })
    card_num += 1

    # Card 8: Using bitwise operators
    cards.append({
        "id": f"ch8_3_{card_num:03d}",
        "lesson": "8.3",
        "type": "code",
        "tags": ["cpp", "operators", "common-mistakes"],
        "question": "What's wrong with using & instead of && in this condition?",
        "code": "if (x > 5 & y < 10)\n    doSomething();",
        "answer": "& is bitwise AND, not logical AND. Use && for logical operations.",
        "explanation": "& performs bitwise AND on the boolean values (treating them as integers). && is the logical AND operator and includes short-circuit evaluation.",
        "source": "8.3 - Common if statement problems",
        "difficulty": "medium"
    })
    card_num += 1

    # Card 9: Redundant if-else
    cards.append({
        "id": f"ch8_3_{card_num:03d}",
        "lesson": "8.3",
        "type": "concept",
        "tags": ["cpp", "conditionals", "best-practices"],
        "concept": "Avoid Redundant If-Else for Boolean Returns",
        "explanation": "Don't use if-else to return true/false. Return the condition directly.",
        "examples": [
            "// Bad: redundant if-else",
            "if (x > 5)",
            "    return true;",
            "else",
            "    return false;",
            "",
            "// Good: return condition directly",
            "return (x > 5);"
        ],
        "source": "8.3 - Common if statement problems",
        "difficulty": "medium"
    })
    card_num += 1

    # Card 10: Floating point equality
    cards.append({
        "id": f"ch8_3_{card_num:03d}",
        "lesson": "8.3",
        "type": "basic",
        "tags": ["cpp", "conditionals", "floating-point", "gotchas"],
        "front": "Why should you avoid using == with floating point values?",
        "back": "Floating point values often have rounding errors, so == comparisons may fail even when values are conceptually equal. Use an epsilon comparison instead.",
        "source": "8.3 - Common if statement problems",
        "difficulty": "hard"
    })
    card_num += 1

    # Card 11: Else after return
    cards.append({
        "id": f"ch8_3_{card_num:03d}",
        "lesson": "8.3",
        "type": "concept",
        "tags": ["cpp", "conditionals", "best-practices"],
        "concept": "Early Return vs Else After Return",
        "explanation": "Else after return is redundant. Use early return for cleaner code.",
        "examples": [
            "// Redundant else",
            "if (x > 5)",
            "    return true;",
            "else  // unnecessary",
            "    return false;",
            "",
            "// Better: early return",
            "if (x > 5)",
            "    return true;",
            "",
            "return false;"
        ],
        "source": "8.3 - Common if statement problems",
        "difficulty": "medium"
    })
    card_num += 1

    # Card 12: Null statement pitfall
    cards.append({
        "id": f"ch8_3_{card_num:03d}",
        "lesson": "8.3",
        "type": "cloze",
        "tags": ["cpp", "conditionals", "common-mistakes"],
        "text": "A semicolon by itself creates a {{c1::null statement}} (or {{c1::empty statement}}) that does nothing.",
        "source": "8.3 - Common if statement problems",
        "difficulty": "easy"
    })

    return cards

# Continue with more card generation functions...

def main():
    """Main function to generate all Chapter 8 flashcards"""

    # Paths
    base_path = '/Users/stefan/Desktop/learnCPP/learncpp-anki-deck/content/lessons'
    output_dir = '/Users/stefan/Desktop/learnCPP/learncpp-anki-deck/deck/chapter_8'

    # Find Chapter 8 directory
    chapter_dir = find_chapter_dir(base_path)
    if not chapter_dir:
        print("ERROR: Could not find Chapter 8 directory")
        return

    print(f"Found Chapter 8 at: {chapter_dir}")

    # Track statistics
    total_lessons = 0
    total_cards = 0

    # Process 8.2
    print("\nProcessing lesson 8.2...")
    with open(os.path.join(chapter_dir, '8_2.json'), 'r') as f:
        lesson = json.load(f)
    cards = generate_cards_8_2(lesson)
    output = {
        "chapter": "Chapter 8",
        "chapter_title": "Control Flow",
        "lesson": "8.2",
        "lesson_title": lesson['title'].split('—')[1].strip() if '—' in lesson['title'] else lesson['title'],
        "total_cards": len(cards),
        "cards": cards
    }
    with open(os.path.join(output_dir, '8_2.json'), 'w') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  Generated {len(cards)} cards for lesson 8.2")
    total_lessons += 1
    total_cards += len(cards)

    # Process 8.3
    print("\nProcessing lesson 8.3...")
    with open(os.path.join(chapter_dir, '8_3.json'), 'r') as f:
        lesson = json.load(f)
    cards = generate_cards_8_3(lesson)
    output = {
        "chapter": "Chapter 8",
        "chapter_title": "Control Flow",
        "lesson": "8.3",
        "lesson_title": lesson['title'].split('—')[1].strip() if '—' in lesson['title'] else lesson['title'],
        "total_cards": len(cards),
        "cards": cards
    }
    with open(os.path.join(output_dir, '8_3.json'), 'w') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  Generated {len(cards)} cards for lesson 8.3")
    total_lessons += 1
    total_cards += len(cards)

    # Summary
    print(f"\n{'='*60}")
    print(f"PARTIAL SUMMARY (Lessons 8.2-8.3)")
    print(f"{'='*60}")
    print(f"Lessons processed: {total_lessons}")
    print(f"Total cards generated: {total_cards}")
    print(f"Average cards per lesson: {total_cards/total_lessons:.1f}")
    print(f"\nNote: This script processes 8.2 and 8.3 only.")
    print(f"Additional lessons need to be processed separately.")

if __name__ == "__main__":
    main()
