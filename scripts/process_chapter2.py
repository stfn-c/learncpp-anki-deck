#!/usr/bin/env python3
"""
Generate Anki flashcards for all Chapter 2 lessons.
This script handles the non-breaking space in the directory name.
"""

import json
import pathlib
import sys

def create_cards_2_1(lesson):
    """Create flashcards for lesson 2.1 - Introduction to functions"""
    cards = []

    cards.append({
        "id": "ch2_1_001",
        "lesson": "2.1",
        "type": "basic",
        "tags": ["cpp", "functions", "fundamentals"],
        "front": "What is a function in C++?",
        "back": "A reusable sequence of statements designed to do a particular job.",
        "source": "2.1 - Introduction to functions",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_1_002",
        "lesson": "2.1",
        "type": "reverse",
        "tags": ["cpp", "functions", "terminology"],
        "front": "caller",
        "back": "The function that initiates a function call",
        "source": "2.1 - Introduction to functions",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_1_003",
        "lesson": "2.1",
        "type": "reverse",
        "tags": ["cpp", "functions", "terminology"],
        "front": "callee",
        "back": "The function being called (executed) by another function",
        "source": "2.1 - Introduction to functions",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_1_004",
        "lesson": "2.1",
        "type": "cloze",
        "tags": ["cpp", "functions", "syntax"],
        "text": "The basic syntax for a user-defined function is {{c1::returnType functionName() { /* function body */ }}}",
        "source": "2.1 - Introduction to functions",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_1_005",
        "lesson": "2.1",
        "type": "basic",
        "tags": ["cpp", "functions", "syntax"],
        "front": "What is the function header?",
        "back": "The first line of a function definition that tells the compiler about the existence of the function, including its name and return type.",
        "source": "2.1 - Introduction to functions",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_1_006",
        "lesson": "2.1",
        "type": "basic",
        "tags": ["cpp", "functions", "syntax"],
        "front": "In a function definition, what are the curly braces and statements in-between called?",
        "back": "The function body",
        "source": "2.1 - Introduction to functions",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_1_007",
        "lesson": "2.1",
        "type": "cloze",
        "tags": ["cpp", "functions", "syntax"],
        "text": "To call a function, use {{c1::the function's name followed by parentheses}}, e.g., functionName()",
        "source": "2.1 - Introduction to functions",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_1_008",
        "lesson": "2.1",
        "type": "concept",
        "tags": ["cpp", "functions", "common-mistakes"],
        "concept": "Calling a function",
        "explanation": "When calling a function, always include the parentheses () after the function name. Forgetting them may cause the program not to compile, or if it does compile, the function will not be called.",
        "examples": [
            "doPrint();     // correct: calls the function",
            "doPrint;       // wrong: does not call the function"
        ],
        "source": "2.1 - Introduction to functions",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_1_009",
        "lesson": "2.1",
        "type": "basic",
        "tags": ["cpp", "functions", "limitations"],
        "front": "Can you define a function inside another function in C++?",
        "back": "No. C++ does not support nested functions. All function definitions must be at the same scope level.",
        "source": "2.1 - Introduction to functions",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_1_010",
        "lesson": "2.1",
        "type": "code",
        "tags": ["cpp", "functions", "common-mistakes"],
        "question": "What's wrong with this code?",
        "code": "#include <iostream>\n\nint main()\n{\n    void foo()\n    {\n        std::cout << \"foo!\\n\";\n    }\n    foo();\n    return 0;\n}",
        "answer": "Function foo() is nested inside main(). C++ does not support nested functions.",
        "explanation": "In C++, all functions must be defined at the same scope level. The function foo() should be defined outside of main().",
        "source": "2.1 - Introduction to functions",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_1_011",
        "lesson": "2.1",
        "type": "code",
        "tags": ["cpp", "functions", "execution-flow"],
        "question": "What does this program output?",
        "code": "#include <iostream>\n\nvoid doPrint()\n{\n    std::cout << \"In doPrint()\\n\";\n}\n\nint main()\n{\n    std::cout << \"Starting main()\\n\";\n    doPrint();\n    doPrint();\n    std::cout << \"Ending main()\\n\";\n    return 0;\n}",
        "answer": "Starting main()\nIn doPrint()\nIn doPrint()\nEnding main()",
        "explanation": "The program starts in main(), prints \"Starting main()\", calls doPrint() twice (each prints \"In doPrint()\"), then prints \"Ending main()\".",
        "source": "2.1 - Introduction to functions",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_1_012",
        "lesson": "2.1",
        "type": "code",
        "tags": ["cpp", "functions", "execution-flow"],
        "question": "What does this program output?",
        "code": "#include <iostream>\n\nvoid doB()\n{\n    std::cout << \"In doB()\\n\";\n}\n\nvoid doA()\n{\n    std::cout << \"In doA()\\n\";\n    doB();\n}\n\nint main()\n{\n    std::cout << \"Starting main()\\n\";\n    doA();\n    doB();\n    std::cout << \"Ending main()\\n\";\n    return 0;\n}",
        "answer": "Starting main()\nIn doA()\nIn doB()\nIn doB()\nEnding main()",
        "explanation": "main() calls doA() which prints \"In doA()\" then calls doB() (first \"In doB()\"). Then main() directly calls doB() again (second \"In doB()\").",
        "source": "2.1 - Introduction to functions",
        "difficulty": "hard"
    })

    cards.append({
        "id": "ch2_1_013",
        "lesson": "2.1",
        "type": "basic",
        "tags": ["cpp", "functions", "best-practices"],
        "front": "When must a function be defined relative to when it is called?",
        "back": "A function must be defined before it can be called (though forward declarations can work around this limitation).",
        "source": "2.1 - Introduction to functions",
        "difficulty": "medium"
    })

    return cards

def create_cards_2_2(lesson):
    """Create flashcards for lesson 2.2 - Function return values"""
    cards = []

    cards.append({
        "id": "ch2_2_001",
        "lesson": "2.2",
        "type": "basic",
        "tags": ["cpp", "functions", "return-values"],
        "front": "What is a return value in C++?",
        "back": "A value that is passed back from the called function to the caller when a function completes execution.",
        "source": "2.2 - Function return values",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_2_002",
        "lesson": "2.2",
        "type": "cloze",
        "tags": ["cpp", "functions", "syntax"],
        "text": "To return a value from a function, use the {{c1::return}} keyword followed by the value to return.",
        "source": "2.2 - Function return values",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_2_003",
        "lesson": "2.2",
        "type": "basic",
        "tags": ["cpp", "functions", "return-values"],
        "front": "What is the return type of a function?",
        "back": "The type specified at the beginning of the function header that indicates what type of value the function will return to the caller.",
        "source": "2.2 - Function return values",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_2_004",
        "lesson": "2.2",
        "type": "code",
        "tags": ["cpp", "functions", "return-values"],
        "question": "What does this function return?",
        "code": "int returnFive()\n{\n    return 5;\n}\n\nint main()\n{\n    std::cout << returnFive();\n    return 0;\n}",
        "answer": "5",
        "explanation": "The function returnFive() has a return type of int and returns the value 5. When called in main(), it prints 5.",
        "source": "2.2 - Function return values",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_2_005",
        "lesson": "2.2",
        "type": "concept",
        "tags": ["cpp", "functions", "best-practices"],
        "concept": "Function return values",
        "explanation": "Functions that return values are called value-returning functions. The return type must match the actual value being returned.",
        "examples": [
            "int getInt() { return 5; }      // returns int",
            "bool isEven() { return true; }  // returns bool",
            "double getPI() { return 3.14; } // returns double"
        ],
        "source": "2.2 - Function return values",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_2_006",
        "lesson": "2.2",
        "type": "basic",
        "tags": ["cpp", "functions", "return-values"],
        "front": "What happens when a return statement is executed?",
        "back": "The function terminates immediately and returns control to the caller, passing back the return value.",
        "source": "2.2 - Function return values",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_2_007",
        "lesson": "2.2",
        "type": "basic",
        "tags": ["cpp", "functions", "main"],
        "front": "What does a return value of 0 from main() indicate?",
        "back": "That the program executed successfully.",
        "source": "2.2 - Function return values",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_2_008",
        "lesson": "2.2",
        "type": "basic",
        "tags": ["cpp", "functions", "main"],
        "front": "What does a non-zero return value from main() indicate?",
        "back": "That the program failed or encountered an error.",
        "source": "2.2 - Function return values",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_2_009",
        "lesson": "2.2",
        "type": "code",
        "tags": ["cpp", "functions", "common-mistakes"],
        "question": "What's wrong with this code?",
        "code": "int getValue()\n{\n    int x = 5;\n    // forgot return statement\n}",
        "answer": "Missing return statement. A function with a non-void return type must return a value.",
        "explanation": "If a value-returning function doesn't return a value, the behavior is undefined. Always include a return statement.",
        "source": "2.2 - Function return values",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_2_010",
        "lesson": "2.2",
        "type": "cloze",
        "tags": ["cpp", "functions", "syntax"],
        "text": "A function whose return type is not void is called a {{c1::value-returning function}}.",
        "source": "2.2 - Function return values",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_2_011",
        "lesson": "2.2",
        "type": "basic",
        "tags": ["cpp", "functions", "best-practices"],
        "front": "Can you ignore (not use) the return value of a function?",
        "back": "Yes, you can call a value-returning function without using its return value, though this may waste the computation.",
        "source": "2.2 - Function return values",
        "difficulty": "medium"
    })

    return cards

def main():
    # Find the Chapter 2 directory (handles non-breaking space)
    lessons_dir = pathlib.Path('/Users/stefan/Desktop/learnCPP/learncpp-anki-deck/content/lessons')
    chapter2_dirs = list(lessons_dir.glob('Chapter*2'))
    chapter2_dir = [d for d in chapter2_dirs if d.name.endswith('2')][0]

    output_dir = pathlib.Path('/Users/stefan/Desktop/learnCPP/learncpp-anki-deck/deck/chapter_2')
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process lesson 2.1
    lesson_file = chapter2_dir / '2_1.json'
    if lesson_file.exists():
        with open(lesson_file, 'r', encoding='utf-8') as f:
            lesson = json.load(f)

        cards = create_cards_2_1(lesson)
        output = {
            "chapter": "Chapter 2",
            "chapter_title": "Functions and Files",
            "lesson": "2.1",
            "lesson_title": lesson['title'],
            "total_cards": len(cards),
            "cards": cards
        }

        with open(output_dir / '2_1.json', 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        print(f"✓ Created {len(cards)} cards for lesson 2.1")

    # Process lesson 2.2
    lesson_file = chapter2_dir / '2_2.json'
    if lesson_file.exists():
        with open(lesson_file, 'r', encoding='utf-8') as f:
            lesson = json.load(f)

        cards = create_cards_2_2(lesson)
        output = {
            "chapter": "Chapter 2",
            "chapter_title": "Functions and Files",
            "lesson": "2.2",
            "lesson_title": lesson['title'],
            "total_cards": len(cards),
            "cards": cards
        }

        with open(output_dir / '2_2.json', 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        print(f"✓ Created {len(cards)} cards for lesson 2.2")

if __name__ == "__main__":
    main()
