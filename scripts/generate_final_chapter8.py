#!/usr/bin/env python3
"""
Generate Anki flashcards for final Chapter 8 lessons (8.8-8.x)
Focuses on loops, control flow, and random numbers
"""

import os
import json

def find_chapter_dir(base_path, marker='8_8.json'):
    """Find the Chapter 8 directory"""
    for item in os.listdir(base_path):
        full_path = os.path.join(base_path, item)
        if os.path.isdir(full_path):
            try:
                if marker in os.listdir(full_path):
                    return full_path
            except:
                pass
    return None

def generate_cards_8_8(lesson):
    """Generate cards for lesson 8.8 - Introduction to loops and while statements"""
    cards = []
    card_num = 1

    cards.append({
        "id": f"ch8_8_{card_num:03d}",
        "lesson": "8.8",
        "type": "basic",
        "tags": ["cpp", "loops", "while"],
        "front": "What is a loop in programming?",
        "back": "A control flow construct that repeatedly executes a sequence of statements until a condition is no longer true.",
        "source": "8.8 - Introduction to loops and while statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_8_{card_num:03d}",
        "lesson": "8.8",
        "type": "cloze",
        "tags": ["cpp", "while", "syntax"],
        "text": "The syntax for a while loop is: while ({{c1::condition}}) {{c2::statement;}}",
        "source": "8.8 - Introduction to loops and while statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_8_{card_num:03d}",
        "lesson": "8.8",
        "type": "basic",
        "tags": ["cpp", "while", "execution"],
        "front": "When does a while loop check its condition?",
        "back": "Before each iteration, including before the first iteration.",
        "source": "8.8 - Introduction to loops and while statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_8_{card_num:03d}",
        "lesson": "8.8",
        "type": "code",
        "tags": ["cpp", "while", "execution"],
        "question": "How many times does this loop execute?",
        "code": "int count{0};\nwhile (count < 3)\n{\n    std::cout << count << '\\n';\n    ++count;\n}",
        "answer": "3 times (count = 0, 1, 2)",
        "explanation": "The loop starts with count=0 and executes while count < 3, so it runs for count values 0, 1, and 2 (3 iterations).",
        "source": "8.8 - Introduction to loops and while statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_8_{card_num:03d}",
        "lesson": "8.8",
        "type": "basic",
        "tags": ["cpp", "loops", "infinite-loop"],
        "front": "What is an infinite loop?",
        "back": "A loop whose condition never becomes false, causing it to execute forever (or until forcibly terminated).",
        "source": "8.8 - Introduction to loops and while statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_8_{card_num:03d}",
        "lesson": "8.8",
        "type": "code",
        "tags": ["cpp", "while", "infinite-loop", "common-mistakes"],
        "question": "Why is this an infinite loop?",
        "code": "int count{0};\nwhile (count < 5)\n{\n    std::cout << count;\n    // forgot to increment count!\n}",
        "answer": "The condition is never updated. count stays 0, which is always less than 5.",
        "explanation": "count is never incremented, so it remains 0 forever, making the condition count < 5 always true.",
        "source": "8.8 - Introduction to loops and while statements",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_8_{card_num:03d}",
        "lesson": "8.8",
        "type": "basic",
        "tags": ["cpp", "loops", "terminology"],
        "front": "What is a loop variable (or counter)?",
        "back": "A variable used to control the number of loop iterations, typically incremented or decremented each iteration.",
        "source": "8.8 - Introduction to loops and while statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_8_{card_num:03d}",
        "lesson": "8.8",
        "type": "cloze",
        "tags": ["cpp", "loops", "terminology"],
        "text": "Each execution of a loop's body is called an {{c1::iteration}}.",
        "source": "8.8 - Introduction to loops and while statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_8_{card_num:03d}",
        "lesson": "8.8",
        "type": "code",
        "tags": ["cpp", "while", "execution"],
        "question": "How many times does this loop execute?",
        "code": "int x{5};\nwhile (x < 3)\n{\n    std::cout << \"Hello\\n\";\n    ++x;\n}",
        "answer": "0 times (never executes)",
        "explanation": "x is 5, which is not less than 3, so the condition is false from the start and the loop body never executes.",
        "source": "8.8 - Introduction to loops and while statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_8_{card_num:03d}",
        "lesson": "8.8",
        "type": "concept",
        "tags": ["cpp", "loops", "best-practices"],
        "concept": "Loop Variable Initialization",
        "explanation": "Always initialize loop variables before the loop and update them inside the loop body.",
        "examples": [
            "// Good: proper initialization and update",
            "int count{0};  // initialized before loop",
            "while (count < 5)",
            "{",
            "    std::cout << count;",
            "    ++count;  // updated in loop",
            "}",
            "",
            "// Bad: uninitialized variable",
            "int count;  // garbage value!",
            "while (count < 5)  // undefined behavior",
            "    ++count;"
        ],
        "source": "8.8 - Introduction to loops and while statements",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_8_{card_num:03d}",
        "lesson": "8.8",
        "type": "basic",
        "tags": ["cpp", "while", "best-practices"],
        "front": "Should you use blocks {} with while loops even for single statements?",
        "back": "Yes, always use blocks with while loops to prevent errors when adding more statements and improve readability.",
        "source": "8.8 - Introduction to loops and while statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_8_{card_num:03d}",
        "lesson": "8.8",
        "type": "code",
        "tags": ["cpp", "while", "common-mistakes"],
        "question": "What's wrong with this code?",
        "code": "while (x < 10);\n{\n    std::cout << x;\n    ++x;\n}",
        "answer": "Semicolon after while creates a null statement, causing an infinite loop.",
        "explanation": "The semicolon ends the while with an empty statement that loops forever. The block is not part of the loop.",
        "source": "8.8 - Introduction to loops and while statements",
        "difficulty": "medium"
    })

    return cards

def generate_cards_8_9(lesson):
    """Generate cards for lesson 8.9 - Do while statements"""
    cards = []
    card_num = 1

    cards.append({
        "id": f"ch8_9_{card_num:03d}",
        "lesson": "8.9",
        "type": "basic",
        "tags": ["cpp", "do-while", "loops"],
        "front": "What is the key difference between while and do-while loops?",
        "back": "do-while loops check the condition after the loop body executes, guaranteeing at least one iteration. while loops check before.",
        "source": "8.9 - Do while statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_9_{card_num:03d}",
        "lesson": "8.9",
        "type": "cloze",
        "tags": ["cpp", "do-while", "syntax"],
        "text": "The syntax for a do-while loop is: do {{c1::statement;}} while ({{c2::condition}});",
        "source": "8.9 - Do while statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_9_{card_num:03d}",
        "lesson": "8.9",
        "type": "basic",
        "tags": ["cpp", "do-while", "execution"],
        "front": "How many times will a do-while loop execute at minimum?",
        "back": "At least once, because the condition is checked after the first iteration.",
        "source": "8.9 - Do while statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_9_{card_num:03d}",
        "lesson": "8.9",
        "type": "code",
        "tags": ["cpp", "do-while", "execution"],
        "question": "How many times does this do-while loop execute?",
        "code": "int x{10};\ndo\n{\n    std::cout << x;\n    ++x;\n} while (x < 5);",
        "answer": "1 time",
        "explanation": "do-while executes the body first (x=10), then checks the condition (10 < 5 is false), so it runs exactly once.",
        "source": "8.9 - Do while statements",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_9_{card_num:03d}",
        "lesson": "8.9",
        "type": "basic",
        "tags": ["cpp", "do-while", "syntax"],
        "front": "What punctuation comes after the condition in a do-while loop?",
        "back": "A semicolon (;) - do-while is the only loop that requires a semicolon after the condition.",
        "source": "8.9 - Do while statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_9_{card_num:03d}",
        "lesson": "8.9",
        "type": "concept",
        "tags": ["cpp", "do-while", "use-cases"],
        "concept": "When to Use Do-While Loops",
        "explanation": "Use do-while when you want the loop body to execute at least once before checking the condition.",
        "examples": [
            "// Good use case: menu that must show at least once",
            "int selection;",
            "do",
            "{",
            "    std::cout << \"1) Option 1\\n2) Option 2\\n\";",
            "    std::cin >> selection;",
            "} while (selection != 1 && selection != 2);",
            "",
            "// User must see menu at least once"
        ],
        "source": "8.9 - Do while statements",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_9_{card_num:03d}",
        "lesson": "8.9",
        "type": "code",
        "tags": ["cpp", "do-while", "common-mistakes"],
        "question": "What's missing from this code?",
        "code": "int x{0};\ndo\n{\n    std::cout << x;\n    ++x;\n} while (x < 5)  // Missing something!",
        "answer": "Missing semicolon after the while condition.",
        "explanation": "do-while requires a semicolon after the condition: while (x < 5);",
        "source": "8.9 - Do while statements",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_9_{card_num:03d}",
        "lesson": "8.9",
        "type": "basic",
        "tags": ["cpp", "do-while", "best-practices"],
        "front": "Are do-while loops used frequently in practice?",
        "back": "No, do-while loops are less common than while and for loops. Most situations are better served by other loop types.",
        "source": "8.9 - Do while statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_9_{card_num:03d}",
        "lesson": "8.9",
        "type": "concept",
        "tags": ["cpp", "loops", "comparison"],
        "concept": "While vs Do-While Loop Comparison",
        "explanation": "Choose while when the loop may not execute at all. Choose do-while when it must execute at least once.",
        "examples": [
            "// while: may not execute",
            "while (x < 5)  // checks first",
            "    doSomething();",
            "",
            "// do-while: always executes once",
            "do",
            "    doSomething();  // executes first",
            "while (x < 5);  // then checks"
        ],
        "source": "8.9 - Do while statements",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_9_{card_num:03d}",
        "lesson": "8.9",
        "type": "cloze",
        "tags": ["cpp", "do-while", "execution"],
        "text": "A do-while loop checks its condition {{c1::after}} each iteration, while a while loop checks {{c2::before}}.",
        "source": "8.9 - Do while statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_9_{card_num:03d}",
        "lesson": "8.9",
        "type": "basic",
        "tags": ["cpp", "do-while", "scope"],
        "front": "Can variables declared inside the do-while body be used in the while condition?",
        "back": "No, variables declared in the loop body go out of scope before the condition is evaluated.",
        "source": "8.9 - Do while statements",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_9_{card_num:03d}",
        "lesson": "8.9",
        "type": "code",
        "tags": ["cpp", "do-while", "input-validation"],
        "question": "Why is do-while good for this input validation?",
        "code": "int num;\ndo\n{\n    std::cout << \"Enter 1-10: \";\n    std::cin >> num;\n} while (num < 1 || num > 10);",
        "answer": "The user must be prompted at least once, and will keep being prompted until valid input is entered.",
        "explanation": "do-while guarantees the prompt shows at least once, and repeats if the input is invalid.",
        "source": "8.9 - Do while statements",
        "difficulty": "easy"
    })

    return cards

def generate_cards_8_10(lesson):
    """Generate cards for lesson 8.10 - For statements"""
    cards = []
    card_num = 1

    cards.append({
        "id": f"ch8_10_{card_num:03d}",
        "lesson": "8.10",
        "type": "cloze",
        "tags": ["cpp", "for", "syntax"],
        "text": "The syntax for a for loop is: for ({{c1::init-statement}}; {{c2::condition}}; {{c3::end-expression}}) {{c4::statement;}}",
        "source": "8.10 - For statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_10_{card_num:03d}",
        "lesson": "8.10",
        "type": "basic",
        "tags": ["cpp", "for", "execution"],
        "front": "What is the execution order of a for loop's components?",
        "back": "1) init-statement (once)\n2) condition check\n3) loop body\n4) end-expression\n5) repeat from step 2",
        "source": "8.10 - For statements",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_10_{card_num:03d}",
        "lesson": "8.10",
        "type": "code",
        "tags": ["cpp", "for", "execution"],
        "question": "What does this for loop print?",
        "code": "for (int i{0}; i < 3; ++i)\n{\n    std::cout << i << ' ';\n}",
        "answer": "0 1 2",
        "explanation": "Loop starts at i=0, runs while i<3, printing 0, 1, and 2, then increments i each time.",
        "source": "8.10 - For statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_10_{card_num:03d}",
        "lesson": "8.10",
        "type": "basic",
        "tags": ["cpp", "for", "scope"],
        "front": "What is the scope of a variable declared in a for loop's init-statement?",
        "back": "The variable is scoped to the for loop only and cannot be accessed outside the loop.",
        "source": "8.10 - For statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_10_{card_num:03d}",
        "lesson": "8.10",
        "type": "basic",
        "tags": ["cpp", "for", "best-practices"],
        "front": "When should you prefer for loops over while loops?",
        "back": "Use for loops when you know in advance how many iterations you need, especially when iterating with a counter.",
        "source": "8.10 - For statements",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_10_{card_num:03d}",
        "lesson": "8.10",
        "type": "concept",
        "tags": ["cpp", "for", "best-practices"],
        "concept": "For Loop vs While Loop",
        "explanation": "For loops are preferred when iterating a specific number of times. All loop control is visible in one line.",
        "examples": [
            "// For loop: clear iteration count",
            "for (int i{0}; i < 10; ++i)",
            "    doSomething();",
            "",
            "// While loop: same logic, more verbose",
            "int i{0};",
            "while (i < 10)",
            "{",
            "    doSomething();",
            "    ++i;",
            "}"
        ],
        "source": "8.10 - For statements",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_10_{card_num:03d}",
        "lesson": "8.10",
        "type": "cloze",
        "tags": ["cpp", "for", "components"],
        "text": "The init-statement in a for loop runs {{c1::once}} at the start, while the end-expression runs {{c2::after each iteration}}.",
        "source": "8.10 - For statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_10_{card_num:03d}",
        "lesson": "8.10",
        "type": "code",
        "tags": ["cpp", "for", "common-mistakes"],
        "question": "What's wrong with this for loop?",
        "code": "for (int i{0}; i < 10; ++i);\n{\n    std::cout << i;\n}",
        "answer": "Semicolon after for creates a null statement. The block is not part of the loop, and i is out of scope.",
        "explanation": "The semicolon ends the for loop with an empty statement. The block executes once after the loop completes, but i is out of scope there.",
        "source": "8.10 - For statements",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_10_{card_num:03d}",
        "lesson": "8.10",
        "type": "basic",
        "tags": ["cpp", "for", "empty-components"],
        "front": "Can you omit any components of a for loop (init, condition, end-expression)?",
        "back": "Yes, any or all components can be omitted, but the semicolons must remain: for (;;) creates an infinite loop.",
        "source": "8.10 - For statements",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_10_{card_num:03d}",
        "lesson": "8.10",
        "type": "code",
        "tags": ["cpp", "for", "execution"],
        "question": "How many times does this loop execute?",
        "code": "for (int i{5}; i > 0; --i)\n{\n    std::cout << i;\n}",
        "answer": "5 times (i = 5, 4, 3, 2, 1)",
        "explanation": "Loop starts at 5, decrements each iteration, and stops when i becomes 0 (no longer > 0).",
        "source": "8.10 - For statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_10_{card_num:03d}",
        "lesson": "8.10",
        "type": "basic",
        "tags": ["cpp", "for", "naming"],
        "front": "What are common variable names for for loop counters?",
        "back": "i, j, k (for nested loops) or more descriptive names like count, index when clarity is needed.",
        "source": "8.10 - For statements",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_10_{card_num:03d}",
        "lesson": "8.10",
        "type": "code",
        "tags": ["cpp", "for", "off-by-one"],
        "question": "What's the common mistake in this loop that should print 1 to 10?",
        "code": "for (int i{1}; i <= 10; ++i)\n    std::cout << i;  // Is this correct?",
        "answer": "This is actually correct! It prints 1 through 10 inclusive.",
        "explanation": "Using <= 10 includes 10 in the output. A common mistake would be using < 10, which would stop at 9.",
        "source": "8.10 - For statements",
        "difficulty": "medium"
    })

    return cards

def generate_cards_8_11(lesson):
    """Generate cards for lesson 8.11 - Break and continue"""
    cards = []
    card_num = 1

    cards.append({
        "id": f"ch8_11_{card_num:03d}",
        "lesson": "8.11",
        "type": "basic",
        "tags": ["cpp", "break", "control-flow"],
        "front": "What does the break statement do in a loop?",
        "back": "Break immediately exits the innermost loop or switch statement, skipping any remaining iterations.",
        "source": "8.11 - Break and continue",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_11_{card_num:03d}",
        "lesson": "8.11",
        "type": "basic",
        "tags": ["cpp", "continue", "control-flow"],
        "front": "What does the continue statement do in a loop?",
        "back": "Continue skips the rest of the current iteration and jumps to the next iteration of the loop.",
        "source": "8.11 - Break and continue",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_11_{card_num:03d}",
        "lesson": "8.11",
        "type": "code",
        "tags": ["cpp", "break", "execution"],
        "question": "What does this code output?",
        "code": "for (int i{0}; i < 10; ++i)\n{\n    if (i == 5)\n        break;\n    std::cout << i << ' ';\n}",
        "answer": "0 1 2 3 4",
        "explanation": "Loop prints 0-4, then when i equals 5, break exits the loop entirely.",
        "source": "8.11 - Break and continue",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_11_{card_num:03d}",
        "lesson": "8.11",
        "type": "code",
        "tags": ["cpp", "continue", "execution"],
        "question": "What does this code output?",
        "code": "for (int i{0}; i < 5; ++i)\n{\n    if (i == 2)\n        continue;\n    std::cout << i << ' ';\n}",
        "answer": "0 1 3 4",
        "explanation": "When i equals 2, continue skips the cout for that iteration only. The loop continues with i=3.",
        "source": "8.11 - Break and continue",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_11_{card_num:03d}",
        "lesson": "8.11",
        "type": "concept",
        "tags": ["cpp", "break", "continue", "differences"],
        "concept": "Break vs Continue",
        "explanation": "Break exits the loop completely. Continue skips to the next iteration.",
        "examples": [
            "// break: exits loop",
            "for (int i{0}; i < 5; ++i)",
            "{",
            "    if (i == 2) break;  // stops at 2",
            "    std::cout << i;  // prints: 0 1",
            "}",
            "",
            "// continue: skips iteration",
            "for (int i{0}; i < 5; ++i)",
            "{",
            "    if (i == 2) continue;  // skips 2",
            "    std::cout << i;  // prints: 0 1 3 4",
            "}"
        ],
        "source": "8.11 - Break and continue",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_11_{card_num:03d}",
        "lesson": "8.11",
        "type": "basic",
        "tags": ["cpp", "break", "nested-loops"],
        "front": "If break is used in a nested loop, which loop does it exit?",
        "back": "Break only exits the innermost loop that contains it. Outer loops continue executing.",
        "source": "8.11 - Break and continue",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_11_{card_num:03d}",
        "lesson": "8.11",
        "type": "basic",
        "tags": ["cpp", "continue", "for-loops"],
        "front": "In a for loop, what happens after a continue statement?",
        "back": "The end-expression executes (e.g., ++i), then the condition is checked for the next iteration.",
        "source": "8.11 - Break and continue",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_11_{card_num:03d}",
        "lesson": "8.11",
        "type": "code",
        "tags": ["cpp", "continue", "common-mistakes"],
        "question": "Why might this while loop behave unexpectedly?",
        "code": "int i{0};\nwhile (i < 5)\n{\n    if (i == 2)\n        continue;\n    std::cout << i;\n    ++i;\n}",
        "answer": "When i==2, continue skips the increment, creating an infinite loop.",
        "explanation": "continue jumps back to the condition check, skipping ++i. Since i stays 2, the loop never progresses.",
        "source": "8.11 - Break and continue",
        "difficulty": "hard"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_11_{card_num:03d}",
        "lesson": "8.11",
        "type": "basic",
        "tags": ["cpp", "break", "continue", "best-practices"],
        "front": "Should break and continue be used frequently?",
        "back": "Use sparingly. They can make code harder to follow. Often better loop structure or early return can be clearer.",
        "source": "8.11 - Break and continue",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_11_{card_num:03d}",
        "lesson": "8.11",
        "type": "concept",
        "tags": ["cpp", "break", "use-cases"],
        "concept": "Common Use Cases for Break",
        "explanation": "Break is useful for early exit when a condition is met, especially in search operations.",
        "examples": [
            "// Find first negative number",
            "for (int num : numbers)",
            "{",
            "    if (num < 0)",
            "    {",
            "        std::cout << \"Found: \" << num;",
            "        break;  // stop searching",
            "    }",
            "}"
        ],
        "source": "8.11 - Break and continue",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_11_{card_num:03d}",
        "lesson": "8.11",
        "type": "concept",
        "tags": ["cpp", "continue", "use-cases"],
        "concept": "Common Use Cases for Continue",
        "explanation": "Continue is useful for skipping invalid or unwanted items during iteration.",
        "examples": [
            "// Process only positive numbers",
            "for (int num : numbers)",
            "{",
            "    if (num <= 0)",
            "        continue;  // skip non-positive",
            "    ",
            "    process(num);  // only process positive",
            "}"
        ],
        "source": "8.11 - Break and continue",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_11_{card_num:03d}",
        "lesson": "8.11",
        "type": "cloze",
        "tags": ["cpp", "break", "continue", "scope"],
        "text": "Break and continue only affect the {{c1::innermost}} loop they appear in.",
        "source": "8.11 - Break and continue",
        "difficulty": "easy"
    })

    return cards

def generate_cards_8_12(lesson):
    """Generate cards for lesson 8.12 - Halts (exiting your program early)"""
    cards = []
    card_num = 1

    cards.append({
        "id": f"ch8_12_{card_num:03d}",
        "lesson": "8.12",
        "type": "basic",
        "tags": ["cpp", "program-termination", "exit"],
        "front": "What does std::exit() do?",
        "back": "std::exit() terminates the program immediately with a specified exit code.",
        "source": "8.12 - Halts (exiting your program early)",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_12_{card_num:03d}",
        "lesson": "8.12",
        "type": "basic",
        "tags": ["cpp", "program-termination", "abort"],
        "front": "What does std::abort() do?",
        "back": "std::abort() terminates the program abnormally, typically without cleanup, indicating an error condition.",
        "source": "8.12 - Halts (exiting your program early)",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_12_{card_num:03d}",
        "lesson": "8.12",
        "type": "cloze",
        "tags": ["cpp", "exit", "header"],
        "text": "std::exit() and std::abort() are defined in the {{c1::<cstdlib>}} header.",
        "source": "8.12 - Halts (exiting your program early)",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_12_{card_num:03d}",
        "lesson": "8.12",
        "type": "basic",
        "tags": ["cpp", "exit", "exit-codes"],
        "front": "What exit code conventionally indicates successful program termination?",
        "back": "0 indicates success. Non-zero values indicate errors or abnormal termination.",
        "source": "8.12 - Halts (exiting your program early)",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_12_{card_num:03d}",
        "lesson": "8.12",
        "type": "cloze",
        "tags": ["cpp", "exit", "syntax"],
        "text": "To exit a program with success status, use {{c1::std::exit(0)}} or {{c1::std::exit(EXIT_SUCCESS)}}.",
        "source": "8.12 - Halts (exiting your program early)",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_12_{card_num:03d}",
        "lesson": "8.12",
        "type": "concept",
        "tags": ["cpp", "exit", "abort", "differences"],
        "concept": "std::exit() vs std::abort()",
        "explanation": "std::exit() performs normal cleanup (destructors, etc.). std::abort() terminates immediately without cleanup.",
        "examples": [
            "// std::exit(): normal termination",
            "if (criticalError)",
            "    std::exit(1);  // cleanup happens",
            "",
            "// std::abort(): abnormal termination",
            "if (fatalError)",
            "    std::abort();  // immediate termination, no cleanup"
        ],
        "source": "8.12 - Halts (exiting your program early)",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_12_{card_num:03d}",
        "lesson": "8.12",
        "type": "basic",
        "tags": ["cpp", "exit", "cleanup"],
        "front": "What cleanup does std::exit() perform before terminating?",
        "back": "std::exit() calls destructors for static and global objects, flushes buffers, and closes files.",
        "source": "8.12 - Halts (exiting your program early)",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_12_{card_num:03d}",
        "lesson": "8.12",
        "type": "basic",
        "tags": ["cpp", "exit", "destructors"],
        "front": "Does std::exit() call destructors for local (automatic) variables?",
        "back": "No, std::exit() does not call destructors for local variables, only for global and static objects.",
        "source": "8.12 - Halts (exiting your program early)",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_12_{card_num:03d}",
        "lesson": "8.12",
        "type": "basic",
        "tags": ["cpp", "program-termination", "best-practices"],
        "front": "What is the preferred way to terminate a program normally?",
        "back": "Return from main() rather than calling std::exit(), as return properly cleans up local variables.",
        "source": "8.12 - Halts (exiting your program early)",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_12_{card_num:03d}",
        "lesson": "8.12",
        "type": "basic",
        "tags": ["cpp", "exit", "constants"],
        "front": "What are EXIT_SUCCESS and EXIT_FAILURE?",
        "back": "Constants defined in <cstdlib> representing successful (0) and unsuccessful (non-zero) program termination.",
        "source": "8.12 - Halts (exiting your program early)",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_12_{card_num:03d}",
        "lesson": "8.12",
        "type": "code",
        "tags": ["cpp", "exit", "usage"],
        "question": "What does this code do?",
        "code": "#include <cstdlib>\n\nvoid checkFile()\n{\n    if (!fileExists)\n        std::exit(EXIT_FAILURE);\n}",
        "answer": "Terminates the program with a failure exit code if the file doesn't exist.",
        "explanation": "std::exit(EXIT_FAILURE) immediately terminates the program with a non-zero exit code indicating an error.",
        "source": "8.12 - Halts (exiting your program early)",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_12_{card_num:03d}",
        "lesson": "8.12",
        "type": "basic",
        "tags": ["cpp", "abort", "use-cases"],
        "front": "When should you use std::abort() instead of std::exit()?",
        "back": "Use std::abort() for fatal errors where cleanup might be dangerous or when you want to generate a core dump for debugging.",
        "source": "8.12 - Halts (exiting your program early)",
        "difficulty": "hard"
    })

    return cards

def generate_cards_8_13(lesson):
    """Generate cards for lesson 8.13 - Introduction to random number generation"""
    cards = []
    card_num = 1

    cards.append({
        "id": f"ch8_13_{card_num:03d}",
        "lesson": "8.13",
        "type": "basic",
        "tags": ["cpp", "random", "prng"],
        "front": "What is a PRNG?",
        "back": "A Pseudo-Random Number Generator - an algorithm that generates a sequence of numbers that appear random but are actually deterministic.",
        "source": "8.13 - Introduction to random number generation",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_13_{card_num:03d}",
        "lesson": "8.13",
        "type": "basic",
        "tags": ["cpp", "random", "seed"],
        "front": "What is a seed in the context of random number generation?",
        "back": "An initial value used to initialize the PRNG. The same seed produces the same sequence of random numbers.",
        "source": "8.13 - Introduction to random number generation",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_13_{card_num:03d}",
        "lesson": "8.13",
        "type": "basic",
        "tags": ["cpp", "random", "rand"],
        "front": "Why should you avoid using std::rand()?",
        "back": "std::rand() is old, has poor randomness quality, limited range, and is not recommended for modern C++.",
        "source": "8.13 - Introduction to random number generation",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_13_{card_num:03d}",
        "lesson": "8.13",
        "type": "cloze",
        "tags": ["cpp", "random", "header"],
        "text": "Modern C++ random number facilities are in the {{c1::<random>}} header.",
        "source": "8.13 - Introduction to random number generation",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_13_{card_num:03d}",
        "lesson": "8.13",
        "type": "basic",
        "tags": ["cpp", "random", "components"],
        "front": "What are the two main components needed for random number generation in modern C++?",
        "back": "1) A random number engine (generates random numbers)\n2) A distribution (shapes the output to desired range/pattern)",
        "source": "8.13 - Introduction to random number generation",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_13_{card_num:03d}",
        "lesson": "8.13",
        "type": "basic",
        "tags": ["cpp", "random", "seeding"],
        "front": "What happens if you don't seed a PRNG?",
        "back": "It uses a default seed and produces the same sequence of numbers every time the program runs.",
        "source": "8.13 - Introduction to random number generation",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_13_{card_num:03d}",
        "lesson": "8.13",
        "type": "basic",
        "tags": ["cpp", "random", "std-random-device"],
        "front": "What is std::random_device used for?",
        "back": "std::random_device generates non-deterministic random numbers, typically used as a seed for PRNGs.",
        "source": "8.13 - Introduction to random number generation",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_13_{card_num:03d}",
        "lesson": "8.13",
        "type": "concept",
        "tags": ["cpp", "random", "best-practices"],
        "concept": "Modern Random Number Generation Pattern",
        "explanation": "Use std::random_device for seeding, a PRNG engine for generation, and a distribution for shaping output.",
        "examples": [
            "#include <random>",
            "",
            "std::random_device rd;  // seed source",
            "std::mt19937 gen(rd()); // Mersenne Twister engine",
            "std::uniform_int_distribution<> dist(1, 6);  // 1-6 range",
            "",
            "int roll = dist(gen);  // generate random number"
        ],
        "source": "8.13 - Introduction to random number generation",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_13_{card_num:03d}",
        "lesson": "8.13",
        "type": "basic",
        "tags": ["cpp", "random", "distributions"],
        "front": "What is the purpose of a distribution in C++ random number generation?",
        "back": "A distribution transforms the engine's output into a desired range and pattern (e.g., uniform, normal).",
        "source": "8.13 - Introduction to random number generation",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_13_{card_num:03d}",
        "lesson": "8.13",
        "type": "basic",
        "tags": ["cpp", "random", "uniform-distribution"],
        "front": "What does std::uniform_int_distribution do?",
        "back": "Produces integers in a specified range where each value has equal probability of being selected.",
        "source": "8.13 - Introduction to random number generation",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_13_{card_num:03d}",
        "lesson": "8.13",
        "type": "basic",
        "tags": ["cpp", "random", "pseudo-random"],
        "front": "Why are PRNG numbers called pseudo-random instead of truly random?",
        "back": "They are generated by a deterministic algorithm. Given the same seed, they produce the same sequence.",
        "source": "8.13 - Introduction to random number generation",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_13_{card_num:03d}",
        "lesson": "8.13",
        "type": "basic",
        "tags": ["cpp", "random", "time-seeding"],
        "front": "Is using current time as a seed a good practice?",
        "back": "It's better than a fixed seed, but std::random_device is preferred as it provides better entropy.",
        "source": "8.13 - Introduction to random number generation",
        "difficulty": "medium"
    })

    return cards

def generate_cards_8_14(lesson):
    """Generate cards for lesson 8.14 - Generating random numbers using Mersenne Twister"""
    cards = []
    card_num = 1

    cards.append({
        "id": f"ch8_14_{card_num:03d}",
        "lesson": "8.14",
        "type": "basic",
        "tags": ["cpp", "random", "mersenne-twister"],
        "front": "What is Mersenne Twister?",
        "back": "A high-quality PRNG algorithm that produces excellent random numbers, available in C++ as std::mt19937.",
        "source": "8.14 - Generating random numbers using Mersenne Twister",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_14_{card_num:03d}",
        "lesson": "8.14",
        "type": "cloze",
        "tags": ["cpp", "random", "mersenne-twister"],
        "text": "The Mersenne Twister implementation in C++ is {{c1::std::mt19937}} (32-bit) or {{c1::std::mt19937_64}} (64-bit).",
        "source": "8.14 - Generating random numbers using Mersenne Twister",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_14_{card_num:03d}",
        "lesson": "8.14",
        "type": "basic",
        "tags": ["cpp", "random", "mt19937"],
        "front": "What does the 19937 in mt19937 represent?",
        "back": "The period of the generator: 2^19937-1, an extremely long sequence before repeating.",
        "source": "8.14 - Generating random numbers using Mersenne Twister",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_14_{card_num:03d}",
        "lesson": "8.14",
        "type": "concept",
        "tags": ["cpp", "random", "mersenne-twister", "usage"],
        "concept": "Using Mersenne Twister for Random Numbers",
        "explanation": "Create the engine once, seed it, and reuse it with different distributions.",
        "examples": [
            "#include <random>",
            "",
            "// Create and seed once",
            "std::random_device rd;",
            "std::mt19937 gen(rd());",
            "",
            "// Use with distribution",
            "std::uniform_int_distribution<> dist(1, 100);",
            "int random_num = dist(gen);"
        ],
        "source": "8.14 - Generating random numbers using Mersenne Twister",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_14_{card_num:03d}",
        "lesson": "8.14",
        "type": "basic",
        "tags": ["cpp", "random", "best-practices"],
        "front": "Should you create a new std::mt19937 object every time you need a random number?",
        "back": "No, create it once and reuse it. Creating it repeatedly (especially with the same seed) produces poor randomness.",
        "source": "8.14 - Generating random numbers using Mersenne Twister",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_14_{card_num:03d}",
        "lesson": "8.14",
        "type": "basic",
        "tags": ["cpp", "random", "distributions"],
        "front": "What is std::uniform_real_distribution used for?",
        "back": "Generating random floating-point numbers in a specified range with equal probability.",
        "source": "8.14 - Generating random numbers using Mersenne Twister",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_14_{card_num:03d}",
        "lesson": "8.14",
        "type": "code",
        "tags": ["cpp", "random", "mersenne-twister"],
        "question": "What range of values can this code generate?",
        "code": "std::mt19937 gen(std::random_device{}());\nstd::uniform_int_distribution dist(1, 6);\nint roll = dist(gen);",
        "answer": "1 to 6 inclusive (like a six-sided die)",
        "explanation": "std::uniform_int_distribution(1, 6) generates integers from 1 to 6 with equal probability.",
        "source": "8.14 - Generating random numbers using Mersenne Twister",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_14_{card_num:03d}",
        "lesson": "8.14",
        "type": "basic",
        "tags": ["cpp", "random", "static"],
        "front": "Why might you declare a random number generator as static in a function?",
        "back": "To initialize it only once (with seed) and maintain state between function calls, improving randomness.",
        "source": "8.14 - Generating random numbers using Mersenne Twister",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_14_{card_num:03d}",
        "lesson": "8.14",
        "type": "concept",
        "tags": ["cpp", "random", "static-generator"],
        "concept": "Static Random Generator in Functions",
        "explanation": "Use static to preserve generator state across function calls.",
        "examples": [
            "int rollDice()",
            "{",
            "    static std::mt19937 gen(std::random_device{}());",
            "    static std::uniform_int_distribution dist(1, 6);",
            "    ",
            "    return dist(gen);  // maintains state between calls",
            "}"
        ],
        "source": "8.14 - Generating random numbers using Mersenne Twister",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_14_{card_num:03d}",
        "lesson": "8.14",
        "type": "basic",
        "tags": ["cpp", "random", "seeding"],
        "front": "Should you seed a random number generator more than once?",
        "back": "No, seed it once at creation. Re-seeding can reduce randomness quality and is usually unnecessary.",
        "source": "8.14 - Generating random numbers using Mersenne Twister",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_14_{card_num:03d}",
        "lesson": "8.14",
        "type": "basic",
        "tags": ["cpp", "random", "distributions"],
        "front": "Can you use the same mt19937 generator with different distributions?",
        "back": "Yes, one generator can be used with multiple distributions (e.g., both int and real distributions).",
        "source": "8.14 - Generating random numbers using Mersenne Twister",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_14_{card_num:03d}",
        "lesson": "8.14",
        "type": "basic",
        "tags": ["cpp", "random", "mersenne-twister"],
        "front": "Is Mersenne Twister cryptographically secure?",
        "back": "No, Mersenne Twister is not cryptographically secure. For security applications, use specialized cryptographic RNGs.",
        "source": "8.14 - Generating random numbers using Mersenne Twister",
        "difficulty": "hard"
    })

    return cards

def generate_cards_8_15(lesson):
    """Generate cards for lesson 8.15 - Global random numbers (Random.h)"""
    cards = []
    card_num = 1

    cards.append({
        "id": f"ch8_15_{card_num:03d}",
        "lesson": "8.15",
        "type": "basic",
        "tags": ["cpp", "random", "global"],
        "front": "Why might you want a global random number generator?",
        "back": "To avoid re-creating and re-seeding generators, ensuring better randomness and consistency across the program.",
        "source": "8.15 - Global random numbers (Random.h)",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_15_{card_num:03d}",
        "lesson": "8.15",
        "type": "concept",
        "tags": ["cpp", "random", "namespace"],
        "concept": "Namespace for Global Random Functions",
        "explanation": "Put random number utilities in a namespace to avoid naming conflicts and organize code.",
        "examples": [
            "// Random.h",
            "namespace Random",
            "{",
            "    int get(int min, int max);",
            "    double get(double min, double max);",
            "}",
            "",
            "// Usage",
            "int dice = Random::get(1, 6);"
        ],
        "source": "8.15 - Global random numbers (Random.h)",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_15_{card_num:03d}",
        "lesson": "8.15",
        "type": "basic",
        "tags": ["cpp", "random", "header-file"],
        "front": "What should you put in a Random.h header file?",
        "back": "Function declarations for random number generation utilities, typically within a Random namespace.",
        "source": "8.15 - Global random numbers (Random.h)",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_15_{card_num:03d}",
        "lesson": "8.15",
        "type": "basic",
        "tags": ["cpp", "random", "implementation"],
        "front": "Where should the global mt19937 generator be defined?",
        "back": "In a .cpp file (Random.cpp), typically as a static variable or in an anonymous namespace to limit scope.",
        "source": "8.15 - Global random numbers (Random.h)",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_15_{card_num:03d}",
        "lesson": "8.15",
        "type": "concept",
        "tags": ["cpp", "random", "helper-functions"],
        "concept": "Random Number Helper Functions",
        "explanation": "Create simple helper functions to abstract away the complexity of random number generation.",
        "examples": [
            "// Random.h",
            "namespace Random",
            "{",
            "    int get(int min, int max);",
            "}",
            "",
            "// Random.cpp",
            "int Random::get(int min, int max)",
            "{",
            "    static std::mt19937 gen{std::random_device{}()};",
            "    return std::uniform_int_distribution{min, max}(gen);",
            "}"
        ],
        "source": "8.15 - Global random numbers (Random.h)",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_15_{card_num:03d}",
        "lesson": "8.15",
        "type": "basic",
        "tags": ["cpp", "random", "best-practices"],
        "front": "Why use helper functions for random number generation?",
        "back": "They simplify usage, ensure consistent seeding, prevent common mistakes, and make code more readable.",
        "source": "8.15 - Global random numbers (Random.h)",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_15_{card_num:03d}",
        "lesson": "8.15",
        "type": "basic",
        "tags": ["cpp", "random", "anonymous-namespace"],
        "front": "Why might you put a global mt19937 in an anonymous namespace in the .cpp file?",
        "back": "To give it internal linkage, limiting its scope to that translation unit and preventing naming conflicts.",
        "source": "8.15 - Global random numbers (Random.h)",
        "difficulty": "hard"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_15_{card_num:03d}",
        "lesson": "8.15",
        "type": "code",
        "tags": ["cpp", "random", "usage"],
        "question": "What does this code demonstrate?",
        "code": "#include \"Random.h\"\n\nint main()\n{\n    int dice = Random::get(1, 6);\n    double temp = Random::get(20.0, 30.0);\n}",
        "answer": "Using overloaded Random::get() for both int and double ranges.",
        "explanation": "Function overloading allows Random::get() to handle different types (int and double) with the same interface.",
        "source": "8.15 - Global random numbers (Random.h)",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_15_{card_num:03d}",
        "lesson": "8.15",
        "type": "basic",
        "tags": ["cpp", "random", "initialization"],
        "front": "When should the global random number generator be seeded?",
        "back": "Once, typically when it's first created (e.g., using static initialization with std::random_device).",
        "source": "8.15 - Global random numbers (Random.h)",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_15_{card_num:03d}",
        "lesson": "8.15",
        "type": "basic",
        "tags": ["cpp", "random", "advantages"],
        "front": "What are advantages of centralizing random number generation in Random.h?",
        "back": "Single seeding point, consistent interface, easier testing, prevents duplicate generators, and simpler to use.",
        "source": "8.15 - Global random numbers (Random.h)",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_15_{card_num:03d}",
        "lesson": "8.15",
        "type": "concept",
        "tags": ["cpp", "random", "organization"],
        "concept": "Random Number Generation Organization",
        "explanation": "Organize random generation in separate header/source files for reusability.",
        "examples": [
            "// Random.h - declarations",
            "namespace Random { int get(int min, int max); }",
            "",
            "// Random.cpp - implementation",
            "namespace Random {",
            "    int get(int min, int max) { /*...*/ }",
            "}",
            "",
            "// main.cpp - usage",
            "#include \"Random.h\"",
            "int roll = Random::get(1, 6);"
        ],
        "source": "8.15 - Global random numbers (Random.h)",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_15_{card_num:03d}",
        "lesson": "8.15",
        "type": "basic",
        "tags": ["cpp", "random", "testing"],
        "front": "How does centralizing random number generation help with testing?",
        "back": "You can easily add a seed function for testing, allowing deterministic/reproducible test runs.",
        "source": "8.15 - Global random numbers (Random.h)",
        "difficulty": "hard"
    })

    return cards

def generate_cards_8_x(lesson):
    """Generate cards for lesson 8.x - Chapter 8 summary and quiz"""
    cards = []
    card_num = 1

    cards.append({
        "id": f"ch8_x_{card_num:03d}",
        "lesson": "8.x",
        "type": "basic",
        "tags": ["cpp", "control-flow", "summary"],
        "front": "What are the three main categories of loops in C++?",
        "back": "- while loops (condition checked before)\n- do-while loops (condition checked after)\n- for loops (designed for counted iterations)",
        "source": "8.x - Chapter 8 summary and quiz",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_x_{card_num:03d}",
        "lesson": "8.x",
        "type": "basic",
        "tags": ["cpp", "control-flow", "summary"],
        "front": "What are the main conditional statement types in C++?",
        "back": "- if statements (and if-else)\n- switch statements\n- constexpr if statements (C++17)",
        "source": "8.x - Chapter 8 summary and quiz",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_x_{card_num:03d}",
        "lesson": "8.x",
        "type": "basic",
        "tags": ["cpp", "control-flow", "jump-statements"],
        "front": "What are the jump statements available in C++?",
        "back": "- break (exit loop/switch)\n- continue (skip to next iteration)\n- goto (jump to label)\n- return (exit function)",
        "source": "8.x - Chapter 8 summary and quiz",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_x_{card_num:03d}",
        "lesson": "8.x",
        "type": "concept",
        "tags": ["cpp", "loops", "selection"],
        "concept": "Choosing the Right Loop Type",
        "explanation": "Select loop type based on when condition is checked and whether iteration count is known.",
        "examples": [
            "// while: condition checked first, unknown iterations",
            "while (condition) { /*...*/ }",
            "",
            "// do-while: must execute once",
            "do { /*...*/ } while (condition);",
            "",
            "// for: known iteration count",
            "for (int i{0}; i < 10; ++i) { /*...*/ }"
        ],
        "source": "8.x - Chapter 8 summary and quiz",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_x_{card_num:03d}",
        "lesson": "8.x",
        "type": "basic",
        "tags": ["cpp", "blocks", "summary"],
        "front": "What is a block in C++ and why is it important for control flow?",
        "back": "A block {} groups statements together and creates a scope. It allows multiple statements to be controlled by a single if, loop, etc.",
        "source": "8.x - Chapter 8 summary and quiz",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_x_{card_num:03d}",
        "lesson": "8.x",
        "type": "basic",
        "tags": ["cpp", "switch", "summary"],
        "front": "When should you use switch instead of if-else chains?",
        "back": "When testing a single integral value against multiple constant values. Switch is clearer and potentially more efficient.",
        "source": "8.x - Chapter 8 summary and quiz",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_x_{card_num:03d}",
        "lesson": "8.x",
        "type": "concept",
        "tags": ["cpp", "random", "best-practices"],
        "concept": "Best Practices for Random Number Generation",
        "explanation": "Use modern C++ random facilities with proper seeding and reusable generators.",
        "examples": [
            "// Don't use: std::rand() - old, poor quality",
            "",
            "// Do use: Modern random library",
            "std::mt19937 gen(std::random_device{}());",
            "std::uniform_int_distribution dist(1, 6);",
            "int roll = dist(gen);",
            "",
            "// Or use helper functions (Random::get())"
        ],
        "source": "8.x - Chapter 8 summary and quiz",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_x_{card_num:03d}",
        "lesson": "8.x",
        "type": "basic",
        "tags": ["cpp", "control-flow", "best-practices"],
        "front": "What are common mistakes to avoid with control flow statements?",
        "back": "- Null statements (extra semicolons)\n- Missing blocks {}\n- Using = instead of ==\n- Infinite loops (forgetting to update condition)\n- Wrong break/continue placement",
        "source": "8.x - Chapter 8 summary and quiz",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_x_{card_num:03d}",
        "lesson": "8.x",
        "type": "basic",
        "tags": ["cpp", "goto", "summary"],
        "front": "Should you use goto in modern C++?",
        "back": "No, avoid goto. Use loops, break, continue, return, or restructure code into functions instead.",
        "source": "8.x - Chapter 8 summary and quiz",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_x_{card_num:03d}",
        "lesson": "8.x",
        "type": "basic",
        "tags": ["cpp", "halts", "summary"],
        "front": "What's the difference between returning from main() and calling std::exit()?",
        "back": "Returning from main() properly cleans up local variables. std::exit() skips local variable cleanup but cleans up static/global objects.",
        "source": "8.x - Chapter 8 summary and quiz",
        "difficulty": "medium"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_x_{card_num:03d}",
        "lesson": "8.x",
        "type": "cloze",
        "tags": ["cpp", "control-flow", "summary"],
        "text": "Control flow statements change the normal {{c1::sequential}} execution path, a process called {{c2::branching}}.",
        "source": "8.x - Chapter 8 summary and quiz",
        "difficulty": "easy"
    })
    card_num += 1

    cards.append({
        "id": f"ch8_x_{card_num:03d}",
        "lesson": "8.x",
        "type": "concept",
        "tags": ["cpp", "control-flow", "summary"],
        "concept": "Chapter 8 Key Takeaways",
        "explanation": "Control flow is essential for creating non-trivial programs that can make decisions and repeat operations.",
        "examples": [
            "Key concepts mastered:",
            "- Conditionals (if, switch, constexpr if)",
            "- Loops (while, do-while, for)",
            "- Jump statements (break, continue)",
            "- Random number generation (mt19937)",
            "- Program flow control",
            "",
            "These enable real-world programming beyond straight-line code."
        ],
        "source": "8.x - Chapter 8 summary and quiz",
        "difficulty": "easy"
    })

    return cards

def main():
    """Main function to generate final Chapter 8 flashcards"""

    base_path = '/Users/stefan/Desktop/learnCPP/learncpp-anki-deck/content/lessons'
    output_dir = '/Users/stefan/Desktop/learnCPP/learncpp-anki-deck/deck/chapter_8'

    chapter_dir = find_chapter_dir(base_path)
    if not chapter_dir:
        print("ERROR: Could not find Chapter 8 directory")
        return

    print(f"Found Chapter 8 at: {chapter_dir}")

    total_lessons = 0
    total_cards = 0

    # Define lesson processors
    lesson_processors = [
        ('8_8', generate_cards_8_8),
        ('8_9', generate_cards_8_9),
        ('8_10', generate_cards_8_10),
        ('8_11', generate_cards_8_11),
        ('8_12', generate_cards_8_12),
        ('8_13', generate_cards_8_13),
        ('8_14', generate_cards_8_14),
        ('8_15', generate_cards_8_15),
        ('8_x', generate_cards_8_x),
    ]

    for lesson_num, processor in lesson_processors:
        print(f"\nProcessing lesson {lesson_num}...")
        with open(os.path.join(chapter_dir, f'{lesson_num}.json'), 'r') as f:
            lesson = json.load(f)

        cards = processor(lesson)
        lesson_number = lesson_num.replace('_', '.')

        output = {
            "chapter": "Chapter 8",
            "chapter_title": "Control Flow",
            "lesson": lesson_number,
            "lesson_title": lesson['title'].split('—')[1].strip() if '—' in lesson['title'] else lesson['title'],
            "total_cards": len(cards),
            "cards": cards
        }

        with open(os.path.join(output_dir, f'{lesson_num}.json'), 'w') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        print(f"  Generated {len(cards)} cards for lesson {lesson_number}")
        total_lessons += 1
        total_cards += len(cards)

    print(f"\n{'='*60}")
    print(f"FINAL BATCH SUMMARY (Lessons 8.8-8.x)")
    print(f"{'='*60}")
    print(f"Lessons processed: {total_lessons}")
    print(f"Total cards generated: {total_cards}")
    print(f"Average cards per lesson: {total_cards/total_lessons:.1f}")

if __name__ == "__main__":
    main()
