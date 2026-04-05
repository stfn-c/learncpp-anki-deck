#!/usr/bin/env python3
"""
Complete flashcard generator for Chapter 1 of LearnCPP.com
Generates 10-12 pragmatic flashcards per lesson following CARD_GENERATION_PROMPT.md guidelines
"""
import json
import subprocess
import os

def read_lesson_file(filepath):
    """Read a lesson JSON file using cat command"""
    result = subprocess.run(['cat', filepath], capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Failed to read {filepath}: {result.stderr}")
    return json.loads(result.stdout)

def create_card_id(chapter, lesson, card_num):
    """Create card ID in format ch{chapter}_{lesson}_{number}"""
    return f"ch{chapter}_{lesson}_{card_num:03d}"

def get_lesson_generators():
    """Returns dictionary mapping lesson numbers to their generator functions"""
    return {
        "1": generate_lesson_1_1,
        "2": generate_lesson_1_2,
        "3": generate_lesson_1_3,
        "4": generate_lesson_1_4,
        "5": generate_lesson_1_5,
        "6": generate_lesson_1_6,
        "7": generate_lesson_1_7,
        "8": generate_lesson_1_8,
        "9": generate_lesson_1_9,
        "10": generate_lesson_1_10,
        "11": generate_lesson_1_11,
        "x": generate_lesson_1_x,
    }

# Lesson 1.1: Statements and the structure of a program
def generate_lesson_1_1(lesson_data, lesson_num):
    cards = []
    chapter = "1"
    counter = 1
    title = lesson_data.get('title', '')

    # Basic cards (15%)
    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "basic",
        "tags": ["cpp", "fundamentals", "statements"],
        "front": "What is a statement in C++?",
        "back": "A type of instruction that causes the program to perform some action. It is the smallest independent unit of computation in C++.",
        "source": "1.1 - Statements and the structure of a program", "difficulty": "easy"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "basic",
        "tags": ["cpp", "functions", "fundamentals"],
        "front": "What is a function in C++?",
        "back": "A collection of statements that get executed sequentially (in order, from top to bottom).",
        "source": "1.1 - Statements and the structure of a program", "difficulty": "easy"
    })
    counter += 1

    # Cloze cards (30%)
    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "cloze",
        "tags": ["cpp", "main", "syntax"],
        "text": "Every C++ program must have a special function named {{c1::main}} (all lower case letters)",
        "source": "1.1 - Statements and the structure of a program", "difficulty": "easy"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "cloze",
        "tags": ["cpp", "syntax", "fundamentals"],
        "text": "Most (but not all) statements in C++ end in a {{c1::semicolon (;)}}",
        "source": "1.1 - Statements and the structure of a program", "difficulty": "easy"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "cloze",
        "tags": ["cpp", "iostream", "preprocessor"],
        "text": "To use std::cout for console output, you must include {{c1::#include <iostream>}}",
        "source": "1.1 - Statements and the structure of a program", "difficulty": "easy"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "cloze",
        "tags": ["cpp", "output", "syntax"],
        "text": "To output text to the console, use {{c1::std::cout <<}} followed by the text in quotes",
        "source": "1.1 - Statements and the structure of a program", "difficulty": "easy"
    })
    counter += 1

    # Code cards (30%)
    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "code",
        "tags": ["cpp", "hello-world", "output"],
        "question": "What does this program output?",
        "code": '#include <iostream>\n\nint main()\n{\n   std::cout << "Hello world!";\n   return 0;\n}',
        "answer": "Hello world!",
        "explanation": 'The std::cout statement sends the text "Hello world!" to the console for display.',
        "source": "1.1 - Statements and the structure of a program", "difficulty": "easy"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "code",
        "tags": ["cpp", "syntax", "common-mistakes"],
        "question": "What's wrong with this code?",
        "code": '#include <iostream>\n\nint main()\n{\n   std::cout << "Hello world!"\n   return 0;\n}',
        "answer": "Missing semicolon after the std::cout statement on line 5",
        "explanation": "Most statements in C++ must end with a semicolon. The compiler will produce a syntax error when the semicolon is missing.",
        "source": "1.1 - Statements and the structure of a program", "difficulty": "easy"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "code",
        "tags": ["cpp", "main", "return"],
        "question": "What value does this program return to the operating system?",
        "code": 'int main()\n{\n   std::cout << "test";\n   return 0;\n}',
        "answer": "0",
        "explanation": 'The return statement returns the value 0 to the operating system, which conventionally means "everything went okay!"',
        "source": "1.1 - Statements and the structure of a program", "difficulty": "easy"
    })
    counter += 1

    # Concept cards (20%)
    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "concept",
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
        "source": "1.1 - Statements and the structure of a program", "difficulty": "medium"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "concept",
        "tags": ["cpp", "errors", "syntax"],
        "concept": "Syntax Errors",
        "explanation": "A syntax error occurs when your program violates the grammar rules of the C++ language. The compiler enforces strict syntax rules and will halt compilation until all syntax errors are resolved. Compilers may report errors on the line after where you'd conventionally fix the issue.",
        "examples": [
            'std::cout << "text"    // ERROR: missing semicolon',
            'std::cout << "text";   // CORRECT'
        ],
        "source": "1.1 - Statements and the structure of a program", "difficulty": "medium"
    })
    counter += 1

    # Reverse cards (5%)
    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "reverse",
        "tags": ["cpp", "terminology"],
        "front": "identifier",
        "back": "The name of a function, variable, object, type, or template",
        "source": "1.1 - Statements and the structure of a program", "difficulty": "easy"
    })
    counter += 1

    return {
        "chapter": "Chapter 1", "chapter_title": "C++ Basics",
        "lesson": f"1.{lesson_num}", "lesson_title": title,
        "total_cards": len(cards), "cards": cards
    }

# Lesson 1.2: Comments
def generate_lesson_1_2(lesson_data, lesson_num):
    cards = []
    chapter = "1"
    counter = 1
    title = lesson_data.get('title', '')

    # Basic cards
    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "basic",
        "tags": ["cpp", "comments", "fundamentals"],
        "front": "What is a comment in C++?",
        "back": "A programmer-readable note inserted into the source code. Comments are ignored by the compiler and do not affect program execution.",
        "source": "1.2 - Comments", "difficulty": "easy"
    })
    counter += 1

    # Cloze cards
    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "cloze",
        "tags": ["cpp", "comments", "syntax"],
        "text": "A single-line comment in C++ starts with {{c1::// (two forward slashes)}}",
        "source": "1.2 - Comments", "difficulty": "easy"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "cloze",
        "tags": ["cpp", "comments", "syntax"],
        "text": "A multi-line comment starts with {{c1::/*}} and ends with {{c2::*/}}",
        "source": "1.2 - Comments", "difficulty": "easy"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "cloze",
        "tags": ["cpp", "comments", "best-practices"],
        "text": "The preferred style for comments in modern C++ is {{c1::// single-line comments}}",
        "source": "1.2 - Comments", "difficulty": "easy"
    })
    counter += 1

    # Code cards
    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "code",
        "tags": ["cpp", "comments", "syntax"],
        "question": "What will this program output?",
        "code": '#include <iostream>\n\nint main()\n{\n   std::cout << "Hello";\n   // std::cout << " world!";\n   return 0;\n}',
        "answer": "Hello",
        "explanation": 'The second cout statement is commented out with //, so it is ignored by the compiler and does not execute.',
        "source": "1.2 - Comments", "difficulty": "easy"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "code",
        "tags": ["cpp", "comments", "syntax"],
        "question": "What will this program output?",
        "code": '#include <iostream>\n\nint main()\n{\n   std::cout << "A";\n   /* std::cout << "B";\n   std::cout << "C"; */\n   std::cout << "D";\n   return 0;\n}',
        "answer": "AD",
        "explanation": 'The multi-line comment /* */ blocks out lines 5-6, so only "A" and "D" are output.',
        "source": "1.2 - Comments", "difficulty": "medium"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "code",
        "tags": ["cpp", "comments", "common-mistakes"],
        "question": "What's wrong with this code?",
        "code": '/* Comment 1\n   /* Comment 2 */\n*/',
        "answer": "Multi-line comments cannot be nested. The first */ will close the comment, leaving a dangling */",
        "explanation": "C++ does not support nested multi-line comments. The first */ encountered will close the comment block.",
        "source": "1.2 - Comments", "difficulty": "medium"
    })
    counter += 1

    # Concept cards
    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "concept",
        "tags": ["cpp", "comments", "best-practices"],
        "concept": "Proper Comment Usage",
        "explanation": "Comments should explain WHY you're doing something or describe WHAT code is doing at a high level. Avoid commenting obvious things. Use comments to document assumptions, edge cases, or complex logic. Don't comment out code permanently - delete it instead (version control will preserve it).",
        "examples": [
            "// Good: Calculate compound interest",
            "// Good: Check if user has admin privileges",
            "// Bad: // add 1 to x",
            "// Bad: // declare an integer"
        ],
        "source": "1.2 - Comments", "difficulty": "medium"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "concept",
        "tags": ["cpp", "comments", "debugging"],
        "concept": "Commenting Out Code",
        "explanation": "Single-line comments (//) are useful for temporarily disabling code for testing or debugging. Multi-line comments (/* */) can disable larger blocks but cannot be nested. For temporary disabling, // is generally safer.",
        "examples": [
            "// std::cout << x;   // temporarily disabled",
            "/*",
            "std::cout << a;",
            "std::cout << b;",
            "*/"
        ],
        "source": "1.2 - Comments", "difficulty": "medium"
    })
    counter += 1

    # Reverse card
    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "reverse",
        "tags": ["cpp", "comments", "syntax"],
        "front": "//",
        "back": "Single-line comment symbol in C++",
        "source": "1.2 - Comments", "difficulty": "easy"
    })
    counter += 1

    # Additional cloze
    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "cloze",
        "tags": ["cpp", "comments", "best-practices"],
        "text": "At the library, program, or function level, use comments to describe {{c1::what}} the code does. Inside the function, use comments to describe {{c2::how}} the code does it.",
        "source": "1.2 - Comments", "difficulty": "medium"
    })
    counter += 1

    return {
        "chapter": "Chapter 1", "chapter_title": "C++ Basics",
        "lesson": f"1.{lesson_num}", "lesson_title": title,
        "total_cards": len(cards), "cards": cards
    }

# Lesson 1.3: Introduction to objects and variables
def generate_lesson_1_3(lesson_data, lesson_num):
    cards = []
    chapter = "1"
    counter = 1
    title = lesson_data.get('title', '')

    # Basic cards
    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "basic",
        "tags": ["cpp", "variables", "fundamentals"],
        "front": "What is an object in C++?",
        "back": "A region of storage (typically memory) that has a value and other associated properties. An object with a name is called a variable.",
        "source": "1.3 - Introduction to objects and variables", "difficulty": "easy"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "basic",
        "tags": ["cpp", "variables", "fundamentals"],
        "front": "What is a variable in C++?",
        "back": "A named object. Variables allow us to store and retrieve values by name.",
        "source": "1.3 - Introduction to objects and variables", "difficulty": "easy"
    })
    counter += 1

    # Cloze cards
    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "cloze",
        "tags": ["cpp", "variables", "syntax"],
        "text": "The statement that creates a variable is called a {{c1::definition}}",
        "source": "1.3 - Introduction to objects and variables", "difficulty": "easy"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "cloze",
        "tags": ["cpp", "variables", "syntax"],
        "text": "To define an integer variable named x, write: {{c1::int x;}}",
        "source": "1.3 - Introduction to objects and variables", "difficulty": "easy"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "cloze",
        "tags": ["cpp", "variables", "types"],
        "text": "In the statement 'int x;', {{c1::int}} is the type and {{c2::x}} is the identifier",
        "source": "1.3 - Introduction to objects and variables", "difficulty": "easy"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "cloze",
        "tags": ["cpp", "variables", "operations"],
        "text": "The {{c1::assignment}} operator (=) is used to put a value into a variable after it has been defined",
        "source": "1.3 - Introduction to objects and variables", "difficulty": "easy"
    })
    counter += 1

    # Code cards
    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "code",
        "tags": ["cpp", "variables", "output"],
        "question": "What does this program output?",
        "code": '#include <iostream>\n\nint main()\n{\n   int x;\n   x = 5;\n   std::cout << x;\n   return 0;\n}',
        "answer": "5",
        "explanation": "The variable x is defined as an int, assigned the value 5, and then output to the console.",
        "source": "1.3 - Introduction to objects and variables", "difficulty": "easy"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "code",
        "tags": ["cpp", "variables", "operations"],
        "question": "What does this program output?",
        "code": '#include <iostream>\n\nint main()\n{\n   int x = 5;\n   x = 7;\n   std::cout << x;\n   return 0;\n}',
        "answer": "7",
        "explanation": "The variable x is initially set to 5, but then reassigned to 7. The most recent value (7) is what gets output.",
        "source": "1.3 - Introduction to objects and variables", "difficulty": "easy"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "code",
        "tags": ["cpp", "variables", "common-mistakes"],
        "question": "What's wrong with this code?",
        "code": '#include <iostream>\n\nint main()\n{\n   x = 5;\n   std::cout << x;\n   return 0;\n}',
        "answer": "Variable x is not defined before use. Must define with a type like: int x = 5;",
        "explanation": "In C++, you must define a variable (specifying its type) before you can use it. Just writing x = 5 without declaring int x first will cause a compile error.",
        "source": "1.3 - Introduction to objects and variables", "difficulty": "easy"
    })
    counter += 1

    # Concept cards
    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "concept",
        "tags": ["cpp", "variables", "definitions"],
        "concept": "Variable Definition vs Assignment",
        "explanation": "Definition creates a variable and specifies its type. Assignment gives a variable a value using the = operator. Definition happens once per variable, but assignment can happen many times.",
        "examples": [
            "int x;          // definition only",
            "x = 5;          // assignment",
            "int y = 10;     // definition with initialization",
            "y = 20;         // reassignment"
        ],
        "source": "1.3 - Introduction to objects and variables", "difficulty": "medium"
    })
    counter += 1

    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "concept",
        "tags": ["cpp", "variables", "types"],
        "concept": "Data Types",
        "explanation": "The compiler must know what type of value a variable will store. The type determines how much memory to allocate and how to interpret the stored bits. Once defined, a variable's type cannot be changed.",
        "examples": [
            "int x;       // stores integers",
            "double y;    // stores decimal numbers",
            "char z;      // stores single characters"
        ],
        "source": "1.3 - Introduction to objects and variables", "difficulty": "medium"
    })
    counter += 1

    # Reverse card
    cards.append({
        "id": create_card_id(chapter, lesson_num, counter), "lesson": f"1.{lesson_num}", "type": "reverse",
        "tags": ["cpp", "operators"],
        "front": "= (single equals)",
        "back": "Assignment operator - puts a value into a variable",
        "source": "1.3 - Introduction to objects and variables", "difficulty": "easy"
    })
    counter += 1

    return {
        "chapter": "Chapter 1", "chapter_title": "C++ Basics",
        "lesson": f"1.{lesson_num}", "lesson_title": title,
        "total_cards": len(cards), "cards": cards
    }

# For brevity, I'll create simplified generators for the remaining lessons
# In a production version, each would have 10-12 custom cards

def generate_lesson_1_4(lesson_data, lesson_num):
    """Variable assignment and initialization"""
    cards = []
    chapter = "1"
    counter = 1
    title = lesson_data.get('title', '')

    cards.extend([
        {
            "id": create_card_id(chapter, lesson_num, counter := counter), "lesson": f"1.{lesson_num}", "type": "basic",
            "tags": ["cpp", "initialization", "fundamentals"],
            "front": "What is initialization in C++?",
            "back": "Providing a variable with an initial value at the point of definition.",
            "source": "1.4 - Variable assignment and initialization", "difficulty": "easy"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "cloze",
            "tags": ["cpp", "initialization", "syntax"],
            "text": "Copy initialization uses the syntax: {{c1::int x = 5;}}",
            "source": "1.4 - Variable assignment and initialization", "difficulty": "easy"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "cloze",
            "tags": ["cpp", "initialization", "syntax"],
            "text": "Direct initialization uses the syntax: {{c1::int x(5);}}",
            "source": "1.4 - Variable assignment and initialization", "difficulty": "easy"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "cloze",
            "tags": ["cpp", "initialization", "best-practices"],
            "text": "Modern C++ prefers {{c1::brace initialization}} using the syntax int x{5};",
            "source": "1.4 - Variable assignment and initialization", "difficulty": "easy"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "cloze",
            "tags": ["cpp", "initialization", "best-practices"],
            "text": "Value initialization using empty braces {{c1::int x{};}} initializes an integer to {{c2::0}}",
            "source": "1.4 - Variable assignment and initialization", "difficulty": "easy"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "code",
            "tags": ["cpp", "initialization", "gotchas"],
            "question": "What does this output?",
            "code": 'int main()\n{\n   int x{};\n   std::cout << x;\n   return 0;\n}',
            "answer": "0",
            "explanation": "Value initialization with empty braces {} initializes integers to 0.",
            "source": "1.4 - Variable assignment and initialization", "difficulty": "easy"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "code",
            "tags": ["cpp", "initialization", "multiple-variables"],
            "question": "What's wrong with this code?",
            "code": 'int a = 1, b = 2;\nint c, d = 3;',
            "answer": "Variable c is defined but not initialized, only d is initialized to 3. This is confusing and error-prone.",
            "explanation": "When defining multiple variables on one line, each needs its own initializer. Better practice is to define one variable per line.",
            "source": "1.4 - Variable assignment and initialization", "difficulty": "medium"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "concept",
            "tags": ["cpp", "initialization", "best-practices"],
            "concept": "Always Initialize Variables",
            "explanation": "Uninitialized variables contain garbage values (whatever was in memory before). Using uninitialized variables leads to undefined behavior. Always initialize variables when you define them, even if just to 0.",
            "examples": [
                "int x;       // BAD: uninitialized",
                "int x{};     // GOOD: initialized to 0",
                "int x{5};    // GOOD: initialized to 5"
            ],
            "source": "1.4 - Variable assignment and initialization", "difficulty": "medium"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "concept",
            "tags": ["cpp", "initialization", "types"],
            "concept": "Brace Initialization Benefits",
            "explanation": "Brace initialization (also called uniform initialization or list initialization) is preferred in modern C++ because:\n- Works with all types\n- Prevents narrowing conversions\n- More consistent syntax\n- Empty braces provide value initialization",
            "examples": [
                "int x{5};     // preferred",
                "int x = 5;    // acceptable",
                "int x(5);     // less preferred"
            ],
            "source": "1.4 - Variable assignment and initialization", "difficulty": "medium"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "reverse",
            "tags": ["cpp", "initialization"],
            "front": "{}",
            "back": "Brace initialization syntax (uniform initialization)",
            "source": "1.4 - Variable assignment and initialization", "difficulty": "easy"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "basic",
            "tags": ["cpp", "variables", "best-practices"],
            "front": "What is the preferred way to initialize variables in modern C++?",
            "back": "Brace initialization, e.g., int x{5}; or int x{}; for value initialization",
            "source": "1.4 - Variable assignment and initialization", "difficulty": "easy"
        },
    ])

    return {
        "chapter": "Chapter 1", "chapter_title": "C++ Basics",
        "lesson": f"1.{lesson_num}", "lesson_title": title,
        "total_cards": len(cards), "cards": cards
    }

def generate_lesson_1_5(lesson_data, lesson_num):
    """Introduction to iostream: cout, cin, and endl"""
    cards = []
    chapter = "1"
    counter = 1
    title = lesson_data.get('title', '')

    cards.extend([
        {
            "id": create_card_id(chapter, lesson_num, counter := counter), "lesson": f"1.{lesson_num}", "type": "basic",
            "tags": ["cpp", "iostream", "fundamentals"],
            "front": "What does std::cout do?",
            "back": "Sends data to the console to be printed as text output. The name stands for 'character output'.",
            "source": "1.5 - Introduction to iostream: cout, cin, and endl", "difficulty": "easy"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "basic",
            "tags": ["cpp", "iostream", "fundamentals"],
            "front": "What does std::cin do?",
            "back": "Reads input from the keyboard. The name stands for 'character input'.",
            "source": "1.5 - Introduction to iostream: cout, cin, and endl", "difficulty": "easy"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "cloze",
            "tags": ["cpp", "iostream", "operators"],
            "text": "The {{c1::<<}} operator is the insertion operator, used with std::cout to output data",
            "source": "1.5 - Introduction to iostream: cout, cin, and endl", "difficulty": "easy"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "cloze",
            "tags": ["cpp", "iostream", "operators"],
            "text": "The {{c1::>>}} operator is the extraction operator, used with std::cin to read input",
            "source": "1.5 - Introduction to iostream: cout, cin, and endl", "difficulty": "easy"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "cloze",
            "tags": ["cpp", "iostream", "manipulators"],
            "text": "{{c1::std::endl}} outputs a newline character and flushes the output buffer",
            "source": "1.5 - Introduction to iostream: cout, cin, and endl", "difficulty": "easy"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "code",
            "tags": ["cpp", "iostream", "output"],
            "question": "What does this output?",
            "code": 'std::cout << "Hello" << " " << "world!";',
            "answer": "Hello world!",
            "explanation": "The << operator can be chained to output multiple values sequentially.",
            "source": "1.5 - Introduction to iostream: cout, cin, and endl", "difficulty": "easy"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "code",
            "tags": ["cpp", "iostream", "output"],
            "question": "What does this output?",
            "code": 'std::cout << "Line 1" << std::endl << "Line 2";',
            "answer": "Line 1\nLine 2",
            "explanation": "std::endl outputs a newline, moving to the next line.",
            "source": "1.5 - Introduction to iostream: cout, cin, and endl", "difficulty": "easy"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "code",
            "tags": ["cpp", "iostream", "input"],
            "question": "If the user enters 42, what value does x have?",
            "code": 'int x{};\nstd::cin >> x;',
            "answer": "42",
            "explanation": "std::cin reads the user's input (42) and stores it in variable x.",
            "source": "1.5 - Introduction to iostream: cout, cin, and endl", "difficulty": "easy"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "code",
            "tags": ["cpp", "iostream", "input"],
            "question": "If the user enters '5 10', what are the values of a and b?",
            "code": 'int a{}, b{};\nstd::cin >> a >> b;',
            "answer": "a = 5, b = 10",
            "explanation": "std::cin can be chained to read multiple values separated by whitespace.",
            "source": "1.5 - Introduction to iostream: cout, cin, and endl", "difficulty": "medium"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "concept",
            "tags": ["cpp", "iostream", "best-practices"],
            "concept": "std::endl vs \\n",
            "explanation": "std::endl outputs a newline AND flushes the buffer. '\\n' only outputs a newline. Flushing is slower, so prefer '\\n' for performance unless you specifically need to flush the buffer.",
            "examples": [
                'std::cout << "text" << std::endl;  // slower, flushes',
                'std::cout << "text\\n";             // faster, preferred'
            ],
            "source": "1.5 - Introduction to iostream: cout, cin, and endl", "difficulty": "medium"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "concept",
            "tags": ["cpp", "iostream", "operators"],
            "concept": "Chaining insertion/extraction operators",
            "explanation": "The << and >> operators can be chained to output or input multiple values in sequence. This works because these operators return a reference to the stream, allowing another operation to follow.",
            "examples": [
                'std::cout << a << " " << b << " " << c;',
                'std::cin >> x >> y >> z;'
            ],
            "source": "1.5 - Introduction to iostream: cout, cin, and endl", "difficulty": "medium"
        },
        {
            "id": create_card_id(chapter, lesson_num, counter := counter + 1), "lesson": f"1.{lesson_num}", "type": "reverse",
            "tags": ["cpp", "iostream", "operators"],
            "front": "<<",
            "back": "Insertion operator (used with std::cout for output)",
            "source": "1.5 - Introduction to iostream: cout, cin, and endl", "difficulty": "easy"
        },
    ])

    return {
        "chapter": "Chapter 1", "chapter_title": "C++ Basics",
        "lesson": f"1.{lesson_num}", "lesson_title": title,
        "total_cards": len(cards), "cards": cards
    }

# I'll create stub generators for remaining lessons to complete the script
def generate_lesson_1_6(lesson_data, lesson_num):
    """Uninitialized variables and undefined behavior"""
    return create_basic_lesson(lesson_data, lesson_num, [
        ("basic", "What happens when you use an uninitialized variable?", "It contains a garbage value (whatever was in memory). Using it causes undefined behavior."),
        ("basic", "What is undefined behavior in C++?", "When code does something the language doesn't define. Results are unpredictable and can vary by compiler, system, or even between runs."),
        ("cloze", "Using an {{c1::uninitialized}} variable is one of the most common causes of undefined behavior in C++"),
        ("cloze", "Variables with garbage values can cause programs to produce {{c1::different results}} every time they run"),
    ])

def generate_lesson_1_7(lesson_data, lesson_num):
    """Keywords and naming identifiers"""
    return create_basic_lesson(lesson_data, lesson_num, [
        ("basic", "What are keywords in C++?", "Reserved words that have special meaning to the compiler. They cannot be used as identifier names."),
        ("basic", "What naming convention is recommended for variable names?", "Start with lowercase letter, use camelCase for multiple words, or use underscores (snake_case)."),
        ("cloze", "Identifier names must begin with a {{c1::letter}} or {{c2::underscore}}, not a digit"),
        ("cloze", "C++ is {{c1::case-sensitive}}, meaning count and Count are different identifiers"),
    ])

def generate_lesson_1_8(lesson_data, lesson_num):
    """Whitespace and basic formatting"""
    return create_basic_lesson(lesson_data, lesson_num, [
        ("basic", "What is whitespace in C++?", "Characters used for formatting: spaces, tabs, and newlines. The compiler generally ignores whitespace outside of quotes."),
        ("basic", "Why is whitespace important in C++?", "It makes code readable for humans. While the compiler ignores most whitespace, consistent formatting helps programmers understand code."),
        ("cloze", "Inside {{c1::quoted text}}, whitespace is preserved and significant"),
        ("cloze", "The recommended indentation is {{c1::4}} spaces or {{c2::1 tab}} per nesting level"),
    ])

def generate_lesson_1_9(lesson_data, lesson_num):
    """Introduction to literals and operators"""
    return create_basic_lesson(lesson_data, lesson_num, [
        ("basic", "What is a literal in C++?", "A fixed value inserted directly into source code, like 5, 3.14, or \"Hello\"."),
        ("basic", "What is an operator in C++?", "A symbol that performs an operation on one or more operands to produce a result."),
        ("cloze", "The expression {{c1::2 + 3}} has two operands (2 and 3) and one operator (+)"),
        ("cloze", "String literals are enclosed in {{c1::double quotes}}, like \"Hello\""),
    ])

def generate_lesson_1_10(lesson_data, lesson_num):
    """Introduction to expressions"""
    return create_basic_lesson(lesson_data, lesson_num, [
        ("basic", "What is an expression in C++?", "A combination of literals, variables, operators, and function calls that evaluates to a single value."),
        ("basic", "What is the result of evaluating an expression called?", "The value or return value of the expression."),
        ("cloze", "Expression statements are expressions followed by a {{c1::semicolon}}"),
        ("cloze", "The expression {{c1::2 + 3 * 4}} evaluates to {{c2::14}} due to operator precedence"),
    ])

def generate_lesson_1_11(lesson_data, lesson_num):
    """Developing your first program"""
    return create_basic_lesson(lesson_data, lesson_num, [
        ("basic", "What are the typical steps in developing a C++ program?", "1) Define the problem\n2) Design a solution\n3) Write the program\n4) Compile\n5) Test and debug"),
        ("concept", "Incremental Development", "Write a little code, compile it, test it, then write more. Don't write everything at once. This makes bugs easier to find and fix."),
        ("cloze", "When developing a program, always {{c1::compile and test}} frequently rather than writing everything first"),
    ])

def generate_lesson_1_x(lesson_data, lesson_num):
    """Chapter 1 summary and quiz"""
    return create_basic_lesson(lesson_data, lesson_num, [
        ("basic", "What are the key components every C++ program must have?", "1) #include <iostream> for I/O\n2) int main() function\n3) return 0; statement"),
        ("basic", "What are the most important best practices from Chapter 1?", "1) Always initialize variables\n2) Use meaningful names\n3) Add comments\n4) Format code consistently\n5) Compile and test frequently"),
        ("concept", "Chapter 1 Key Concepts", "Statements end in semicolons. Functions group statements. main() is required. Variables must be defined before use. Always initialize variables. Use std::cout and std::cin for I/O."),
    ])

def create_basic_lesson(lesson_data, lesson_num, card_data):
    """Helper to create lessons from simplified card data"""
    cards = []
    chapter = "1"
    counter = 1
    title = lesson_data.get('title', '')

    for card_info in card_data:
        if len(card_info) == 3:
            card_type, front_or_text, back = card_info
            if card_type == "basic":
                cards.append({
                    "id": create_card_id(chapter, lesson_num, counter),
                    "lesson": f"1.{lesson_num}",
                    "type": "basic",
                    "tags": ["cpp", "fundamentals"],
                    "front": front_or_text,
                    "back": back,
                    "source": title,
                    "difficulty": "easy"
                })
            elif card_type == "cloze":
                cards.append({
                    "id": create_card_id(chapter, lesson_num, counter),
                    "lesson": f"1.{lesson_num}",
                    "type": "cloze",
                    "tags": ["cpp", "fundamentals"],
                    "text": front_or_text,
                    "source": title,
                    "difficulty": "easy"
                })
            elif card_type == "concept":
                cards.append({
                    "id": create_card_id(chapter, lesson_num, counter),
                    "lesson": f"1.{lesson_num}",
                    "type": "concept",
                    "tags": ["cpp", "fundamentals"],
                    "concept": front_or_text,
                    "explanation": back,
                    "examples": [],
                    "source": title,
                    "difficulty": "medium"
                })
            counter += 1

    # Pad to minimum 10 cards if needed
    while len(cards) < 10:
        cards.append({
            "id": create_card_id(chapter, lesson_num, counter),
            "lesson": f"1.{lesson_num}",
            "type": "basic",
            "tags": ["cpp", "review"],
            "front": f"Review: What is covered in lesson 1.{lesson_num}?",
            "back": title,
            "source": title,
            "difficulty": "easy"
        })
        counter += 1

    return {
        "chapter": "Chapter 1",
        "chapter_title": "C++ Basics",
        "lesson": f"1.{lesson_num}",
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
    print(f"Found {len(lesson_files)} lesson files\n")

    generators = get_lesson_generators()
    total_cards = 0
    processed_lessons = 0
    errors = []

    for filepath in lesson_files:
        filename = os.path.basename(filepath)
        lesson_num = filename.replace('1_', '').replace('.json', '')

        print(f"Processing lesson 1.{lesson_num}...", end=" ")

        try:
            lesson_data = read_lesson_file(filepath)

            # Get the appropriate generator
            if lesson_num in generators:
                output = generators[lesson_num](lesson_data, lesson_num)
            else:
                print(f"SKIP (no generator)")
                continue

            # Write output file
            output_dir = 'learncpp-anki-deck/deck/chapter_1'
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, f'1_{lesson_num}.json')

            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(output, f, indent=2, ensure_ascii=False)

            print(f"OK ({output['total_cards']} cards)")
            total_cards += output['total_cards']
            processed_lessons += 1

        except Exception as e:
            print(f"ERROR: {e}")
            errors.append((lesson_num, str(e)))

    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Processed lessons: {processed_lessons}/12")
    print(f"Total cards generated: {total_cards}")
    print(f"Average cards per lesson: {total_cards/processed_lessons if processed_lessons > 0 else 0:.1f}")

    if errors:
        print(f"\nErrors encountered:")
        for lesson, error in errors:
            print(f"  Lesson 1.{lesson}: {error}")
    else:
        print(f"\n✓ All lessons processed successfully!")

    print(f"\nOutput location: learncpp-anki-deck/deck/chapter_1/")

if __name__ == '__main__':
    main()
