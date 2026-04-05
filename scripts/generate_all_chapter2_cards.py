#!/usr/bin/env python3
"""
Generate pragmatic, practical Anki flashcards for ALL Chapter 2 lessons.
Follows the CARD_GENERATION_PROMPT.md guidelines.
"""

import json
import pathlib
import sys


def create_cards_2_1(lesson):
    """Lesson 2.1 - Introduction to functions"""
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
    """Lesson 2.2 - Function return values"""
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


def create_cards_2_3(lesson):
    """Lesson 2.3 - Void functions"""
    cards = []

    cards.append({
        "id": "ch2_3_001",
        "lesson": "2.3",
        "type": "basic",
        "tags": ["cpp", "functions", "void"],
        "front": "What is a void function?",
        "back": "A function that does not return a value to the caller. Its return type is void.",
        "source": "2.3 - Void functions",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_3_002",
        "lesson": "2.3",
        "type": "cloze",
        "tags": ["cpp", "functions", "syntax"],
        "text": "A function that doesn't return a value uses the return type {{c1::void}}.",
        "source": "2.3 - Void functions",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_3_003",
        "lesson": "2.3",
        "type": "basic",
        "tags": ["cpp", "functions", "void"],
        "front": "Do void functions need a return statement?",
        "back": "No, void functions don't require a return statement (though you can use \"return;\" to exit early).",
        "source": "2.3 - Void functions",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_3_004",
        "lesson": "2.3",
        "type": "code",
        "tags": ["cpp", "functions", "void"],
        "question": "What does this program output?",
        "code": "#include <iostream>\n\nvoid printHi()\n{\n    std::cout << \"Hi\" << '\\n';\n}\n\nint main()\n{\n    printHi();\n    return 0;\n}",
        "answer": "Hi",
        "explanation": "The void function printHi() is called and prints \"Hi\" with a newline, then returns to main().",
        "source": "2.3 - Void functions",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_3_005",
        "lesson": "2.3",
        "type": "code",
        "tags": ["cpp", "functions", "common-mistakes"],
        "question": "What's wrong with this code?",
        "code": "void printValue()\n{\n    std::cout << \"Value\";\n    return 5;\n}",
        "answer": "A void function cannot return a value. Remove the '5' or change the return type.",
        "explanation": "Void functions don't return values. Use \"return;\" to exit early, or just let the function end naturally.",
        "source": "2.3 - Void functions",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_3_006",
        "lesson": "2.3",
        "type": "concept",
        "tags": ["cpp", "functions", "void"],
        "concept": "Early return from void functions",
        "explanation": "You can use a return statement with no value to exit a void function early.",
        "examples": [
            "void doSomething() {",
            "    if (error)",
            "        return;  // exit early",
            "    // normal processing",
            "}"
        ],
        "source": "2.3 - Void functions",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_3_007",
        "lesson": "2.3",
        "type": "basic",
        "tags": ["cpp", "functions", "void"],
        "front": "Can you use the return value of a void function?",
        "back": "No, void functions don't return a value, so there's nothing to use.",
        "source": "2.3 - Void functions",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_3_008",
        "lesson": "2.3",
        "type": "cloze",
        "tags": ["cpp", "functions", "terminology"],
        "text": "Functions that don't return a value are sometimes called {{c1::non-value returning functions}} or {{c2::void functions}}.",
        "source": "2.3 - Void functions",
        "difficulty": "easy"
    })

    return cards


def create_cards_2_4(lesson):
    """Lesson 2.4 - Introduction to function parameters and arguments"""
    cards = []

    cards.append({
        "id": "ch2_4_001",
        "lesson": "2.4",
        "type": "basic",
        "tags": ["cpp", "functions", "parameters"],
        "front": "What is a function parameter?",
        "back": "A variable declared in the function header that will receive a value from the caller.",
        "source": "2.4 - Introduction to function parameters and arguments",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_4_002",
        "lesson": "2.4",
        "type": "basic",
        "tags": ["cpp", "functions", "arguments"],
        "front": "What is an argument?",
        "back": "The actual value or expression passed to a function when it is called.",
        "source": "2.4 - Introduction to function parameters and arguments",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_4_003",
        "lesson": "2.4",
        "type": "reverse",
        "tags": ["cpp", "functions", "terminology"],
        "front": "parameter",
        "back": "A variable declared in the function header",
        "source": "2.4 - Introduction to function parameters and arguments",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_4_004",
        "lesson": "2.4",
        "type": "reverse",
        "tags": ["cpp", "functions", "terminology"],
        "front": "argument",
        "back": "The value passed to a function when calling it",
        "source": "2.4 - Introduction to function parameters and arguments",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_4_005",
        "lesson": "2.4",
        "type": "cloze",
        "tags": ["cpp", "functions", "syntax"],
        "text": "To define a function with parameters, write: {{c1::returnType functionName(type paramName)}}",
        "source": "2.4 - Introduction to function parameters and arguments",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_4_006",
        "lesson": "2.4",
        "type": "code",
        "tags": ["cpp", "functions", "parameters"],
        "question": "What does this program output?",
        "code": "#include <iostream>\n\nvoid printValue(int x)\n{\n    std::cout << x << '\\n';\n}\n\nint main()\n{\n    printValue(5);\n    printValue(10);\n    return 0;\n}",
        "answer": "5\n10",
        "explanation": "printValue() is called twice with different arguments. First with 5, then with 10. Each time it prints the argument value.",
        "source": "2.4 - Introduction to function parameters and arguments",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_4_007",
        "lesson": "2.4",
        "type": "cloze",
        "tags": ["cpp", "functions", "syntax"],
        "text": "When defining multiple parameters, separate them with {{c1::commas}}, e.g., void func(int x, int y)",
        "source": "2.4 - Introduction to function parameters and arguments",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_4_008",
        "lesson": "2.4",
        "type": "concept",
        "tags": ["cpp", "functions", "parameters"],
        "concept": "Multiple parameters",
        "explanation": "Functions can have multiple parameters. When calling the function, provide arguments in the same order as the parameters.",
        "examples": [
            "void add(int x, int y) {",
            "    std::cout << x + y;",
            "}",
            "add(3, 4);  // x=3, y=4, outputs 7"
        ],
        "source": "2.4 - Introduction to function parameters and arguments",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_4_009",
        "lesson": "2.4",
        "type": "code",
        "tags": ["cpp", "functions", "common-mistakes"],
        "question": "What's wrong with this code?",
        "code": "void printSum(int x, int y)\n{\n    std::cout << x + y;\n}\n\nint main()\n{\n    printSum(5);  // missing argument\n    return 0;\n}",
        "answer": "Missing argument. The function expects 2 arguments but only 1 is provided.",
        "explanation": "When calling a function, you must provide the correct number of arguments matching the parameter list.",
        "source": "2.4 - Introduction to function parameters and arguments",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_4_010",
        "lesson": "2.4",
        "type": "basic",
        "tags": ["cpp", "functions", "parameters"],
        "front": "How are arguments passed to parameters?",
        "back": "Arguments are copied into the parameters when the function is called (pass by value).",
        "source": "2.4 - Introduction to function parameters and arguments",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_4_011",
        "lesson": "2.4",
        "type": "basic",
        "tags": ["cpp", "functions", "best-practices"],
        "front": "What happens to parameters when a function returns?",
        "back": "Parameters are destroyed when the function returns (they are local to the function).",
        "source": "2.4 - Introduction to function parameters and arguments",
        "difficulty": "medium"
    })

    return cards


def create_cards_2_5(lesson):
    """Lesson 2.5 - Introduction to local scope"""
    cards = []

    cards.append({
        "id": "ch2_5_001",
        "lesson": "2.5",
        "type": "basic",
        "tags": ["cpp", "scope", "local-variables"],
        "front": "What is a local variable?",
        "back": "A variable defined inside a function (including parameters). It can only be accessed within that function.",
        "source": "2.5 - Introduction to local scope",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_5_002",
        "lesson": "2.5",
        "type": "basic",
        "tags": ["cpp", "scope", "fundamentals"],
        "front": "What is scope?",
        "back": "The region of code where a variable can be accessed. Determines where an identifier can be used.",
        "source": "2.5 - Introduction to local scope",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_5_003",
        "lesson": "2.5",
        "type": "basic",
        "tags": ["cpp", "scope", "local-variables"],
        "front": "What is local scope?",
        "back": "The scope of a variable defined inside a function. The variable is only accessible within that function.",
        "source": "2.5 - Introduction to local scope",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_5_004",
        "lesson": "2.5",
        "type": "code",
        "tags": ["cpp", "scope", "common-mistakes"],
        "question": "What's wrong with this code?",
        "code": "void doSomething()\n{\n    int x = 5;\n}\n\nint main()\n{\n    std::cout << x;  // error\n    return 0;\n}",
        "answer": "Variable x is not in scope. It's local to doSomething() and can't be accessed in main().",
        "explanation": "Local variables are only accessible within the function where they're defined. x is destroyed when doSomething() returns.",
        "source": "2.5 - Introduction to local scope",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_5_005",
        "lesson": "2.5",
        "type": "basic",
        "tags": ["cpp", "scope", "local-variables"],
        "front": "When is a local variable created and destroyed?",
        "back": "Created when the function is called, destroyed when the function returns.",
        "source": "2.5 - Introduction to local scope",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_5_006",
        "lesson": "2.5",
        "type": "reverse",
        "tags": ["cpp", "scope", "terminology"],
        "front": "lifetime",
        "back": "The period of time from when a variable is created until it is destroyed",
        "source": "2.5 - Introduction to local scope",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_5_007",
        "lesson": "2.5",
        "type": "basic",
        "tags": ["cpp", "scope", "local-variables"],
        "front": "Can two different functions have local variables with the same name?",
        "back": "Yes. Local variables in different functions are independent, even if they have the same name.",
        "source": "2.5 - Introduction to local scope",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_5_008",
        "lesson": "2.5",
        "type": "concept",
        "tags": ["cpp", "scope", "best-practices"],
        "concept": "Local scope encapsulation",
        "explanation": "Local variables provide encapsulation - each function has its own variables that don't interfere with other functions.",
        "examples": [
            "void foo() { int x = 1; }",
            "void bar() { int x = 2; }  // different x",
            "// These are independent variables"
        ],
        "source": "2.5 - Introduction to local scope",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_5_009",
        "lesson": "2.5",
        "type": "cloze",
        "tags": ["cpp", "scope", "terminology"],
        "text": "Variables defined inside a function are said to have {{c1::local scope}} or {{c2::block scope}}.",
        "source": "2.5 - Introduction to local scope",
        "difficulty": "easy"
    })

    return cards


def create_cards_2_6(lesson):
    """Lesson 2.6 - Why functions are useful"""
    cards = []

    cards.append({
        "id": "ch2_6_001",
        "lesson": "2.6",
        "type": "basic",
        "tags": ["cpp", "functions", "best-practices"],
        "front": "What is the primary reason to use functions?",
        "back": "To avoid code duplication and make programs more modular, easier to read, maintain, and test.",
        "source": "2.6 - Why functions are useful",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_6_002",
        "lesson": "2.6",
        "type": "concept",
        "tags": ["cpp", "functions", "best-practices"],
        "concept": "DRY Principle",
        "explanation": "Don't Repeat Yourself (DRY) - If you need to do the same thing multiple times, put it in a function rather than copying code.",
        "examples": [
            "// Bad: repeated code",
            "std::cout << \"------\\n\";",
            "std::cout << \"------\\n\";",
            "",
            "// Good: use a function",
            "void printLine() { std::cout << \"------\\n\"; }",
            "printLine(); printLine();"
        ],
        "source": "2.6 - Why functions are useful",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_6_003",
        "lesson": "2.6",
        "type": "basic",
        "tags": ["cpp", "functions", "best-practices"],
        "front": "What are the benefits of using functions?",
        "back": "- Minimizes duplicate code\n- Makes programs easier to read and understand\n- Easier to maintain and update\n- Allows code reuse\n- Easier to test",
        "source": "2.6 - Why functions are useful",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_6_004",
        "lesson": "2.6",
        "type": "basic",
        "tags": ["cpp", "functions", "best-practices"],
        "front": "How do functions help with code updates?",
        "back": "When you need to change functionality, you only update the function once instead of finding and changing every copy of duplicated code.",
        "source": "2.6 - Why functions are useful",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_6_005",
        "lesson": "2.6",
        "type": "basic",
        "tags": ["cpp", "functions", "best-practices"],
        "front": "How do functions improve code readability?",
        "back": "Well-named functions make code self-documenting. The function name describes what it does, making the code easier to understand.",
        "source": "2.6 - Why functions are useful",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_6_006",
        "lesson": "2.6",
        "type": "concept",
        "tags": ["cpp", "functions", "best-practices"],
        "concept": "Function length guidelines",
        "explanation": "Functions should be relatively short and focused on a single task. If a function gets too long, consider breaking it into smaller functions.",
        "examples": [
            "// Good: focused function",
            "int add(int x, int y) { return x + y; }",
            "",
            "// If main() gets too long,",
            "// break it into helper functions"
        ],
        "source": "2.6 - Why functions are useful",
        "difficulty": "medium"
    })

    return cards


def create_cards_2_7(lesson):
    """Lesson 2.7 - Forward declarations"""
    cards = []

    cards.append({
        "id": "ch2_7_001",
        "lesson": "2.7",
        "type": "basic",
        "tags": ["cpp", "functions", "forward-declarations"],
        "front": "What is a forward declaration?",
        "back": "A declaration that tells the compiler about the existence of a function before it's defined, allowing it to be called before its definition.",
        "source": "2.7 - Forward declarations",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_7_002",
        "lesson": "2.7",
        "type": "reverse",
        "tags": ["cpp", "functions", "terminology"],
        "front": "function prototype",
        "back": "Another name for a forward declaration (a function declaration without a body)",
        "source": "2.7 - Forward declarations",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_7_003",
        "lesson": "2.7",
        "type": "cloze",
        "tags": ["cpp", "functions", "syntax"],
        "text": "A forward declaration consists of the function {{c1::signature}} (return type, name, and parameters) followed by a {{c2::semicolon}}.",
        "source": "2.7 - Forward declarations",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_7_004",
        "lesson": "2.7",
        "type": "code",
        "tags": ["cpp", "functions", "forward-declarations"],
        "question": "Which part is the forward declaration?",
        "code": "#include <iostream>\n\nint add(int x, int y);  // ?\n\nint main()\n{\n    std::cout << add(3, 4);\n    return 0;\n}\n\nint add(int x, int y)\n{\n    return x + y;\n}",
        "answer": "int add(int x, int y); is the forward declaration",
        "explanation": "The forward declaration tells the compiler that add() exists, allowing main() to call it before its full definition appears.",
        "source": "2.7 - Forward declarations",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_7_005",
        "lesson": "2.7",
        "type": "basic",
        "tags": ["cpp", "functions", "forward-declarations"],
        "front": "Why use forward declarations?",
        "back": "To allow functions to be defined in any order and to enable functions to call each other (mutual recursion).",
        "source": "2.7 - Forward declarations",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_7_006",
        "lesson": "2.7",
        "type": "concept",
        "tags": ["cpp", "functions", "forward-declarations"],
        "concept": "Declaration vs Definition",
        "explanation": "A declaration tells the compiler about a function's existence. A definition provides the actual implementation.",
        "examples": [
            "int add(int x, int y);         // declaration only",
            "int add(int x, int y) { ... }  // definition (includes declaration)"
        ],
        "source": "2.7 - Forward declarations",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_7_007",
        "lesson": "2.7",
        "type": "code",
        "tags": ["cpp", "functions", "common-mistakes"],
        "question": "What's wrong with this code?",
        "code": "#include <iostream>\n\nint main()\n{\n    std::cout << add(3, 4);  // error\n    return 0;\n}\n\nint add(int x, int y)\n{\n    return x + y;\n}",
        "answer": "Function add() is called before being declared. Add a forward declaration before main().",
        "explanation": "Without a forward declaration, the compiler doesn't know about add() when it's called in main().",
        "source": "2.7 - Forward declarations",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_7_008",
        "lesson": "2.7",
        "type": "basic",
        "tags": ["cpp", "functions", "forward-declarations"],
        "front": "Do parameter names in forward declarations need to match the definition?",
        "back": "No. Parameter names can differ or be omitted in forward declarations. Only types must match.",
        "source": "2.7 - Forward declarations",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_7_009",
        "lesson": "2.7",
        "type": "cloze",
        "tags": ["cpp", "functions", "syntax"],
        "text": "In forward declarations, parameter names are {{c1::optional}}. Only the types are required.",
        "source": "2.7 - Forward declarations",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_7_010",
        "lesson": "2.7",
        "type": "basic",
        "tags": ["cpp", "functions", "best-practices"],
        "front": "What must match between a forward declaration and definition?",
        "back": "- Return type\n- Function name\n- Number of parameters\n- Type of each parameter\n(Parameter names don't need to match)",
        "source": "2.7 - Forward declarations",
        "difficulty": "hard"
    })

    return cards


def create_cards_2_8(lesson):
    """Lesson 2.8 - Programs with multiple code files"""
    cards = []

    cards.append({
        "id": "ch2_8_001",
        "lesson": "2.8",
        "type": "basic",
        "tags": ["cpp", "multi-file", "project-organization"],
        "front": "Why split a program into multiple files?",
        "back": "To organize code better, make it more maintainable, enable code reuse, and allow separate compilation.",
        "source": "2.8 - Programs with multiple code files",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_8_002",
        "lesson": "2.8",
        "type": "basic",
        "tags": ["cpp", "multi-file", "fundamentals"],
        "front": "How many main() functions can a program have?",
        "back": "Exactly one. Every program must have exactly one main() function.",
        "source": "2.8 - Programs with multiple code files",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_8_003",
        "lesson": "2.8",
        "type": "concept",
        "tags": ["cpp", "multi-file", "best-practices"],
        "concept": "Multi-file programs",
        "explanation": "Functions can be defined in different files. Use forward declarations to let one file call functions from another.",
        "examples": [
            "// add.cpp",
            "int add(int x, int y) { return x + y; }",
            "",
            "// main.cpp",
            "int add(int, int);  // forward declaration",
            "int main() { return add(3,4); }"
        ],
        "source": "2.8 - Programs with multiple code files",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_8_004",
        "lesson": "2.8",
        "type": "basic",
        "tags": ["cpp", "multi-file", "compilation"],
        "front": "How do you compile a multi-file program?",
        "back": "Compile all .cpp files together in a single compile command, or compile them separately and link the object files.",
        "source": "2.8 - Programs with multiple code files",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_8_005",
        "lesson": "2.8",
        "type": "cloze",
        "tags": ["cpp", "multi-file", "syntax"],
        "text": "When using functions from another file, you need to add a {{c1::forward declaration}} in the file where you call them.",
        "source": "2.8 - Programs with multiple code files",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_8_006",
        "lesson": "2.8",
        "type": "code",
        "tags": ["cpp", "multi-file", "common-mistakes"],
        "question": "What's missing in main.cpp?",
        "code": "// add.cpp\nint add(int x, int y) { return x + y; }\n\n// main.cpp\nint main()\n{\n    int sum = add(3, 4);  // error\n    return 0;\n}",
        "answer": "Missing forward declaration for add() in main.cpp",
        "explanation": "main.cpp needs a forward declaration: int add(int, int); before main() to tell the compiler about add().",
        "source": "2.8 - Programs with multiple code files",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_8_007",
        "lesson": "2.8",
        "type": "basic",
        "tags": ["cpp", "multi-file", "best-practices"],
        "front": "What's a common naming convention for multi-file programs?",
        "back": "Put related functions in a .cpp file named after their purpose (e.g., math.cpp for math functions).",
        "source": "2.8 - Programs with multiple code files",
        "difficulty": "medium"
    })

    return cards


def create_cards_2_9(lesson):
    """Lesson 2.9 - Naming collisions and intro to namespaces"""
    cards = []

    cards.append({
        "id": "ch2_9_001",
        "lesson": "2.9",
        "type": "basic",
        "tags": ["cpp", "namespaces", "fundamentals"],
        "front": "What is a naming collision?",
        "back": "When two or more identifiers with the same name are introduced into the same scope, causing a conflict.",
        "source": "2.9 - Naming collisions and namespaces",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_9_002",
        "lesson": "2.9",
        "type": "basic",
        "tags": ["cpp", "namespaces", "fundamentals"],
        "front": "What is a namespace?",
        "back": "A region that allows you to declare names inside it for the purpose of preventing naming collisions.",
        "source": "2.9 - Naming collisions and namespaces",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_9_003",
        "lesson": "2.9",
        "type": "reverse",
        "tags": ["cpp", "namespaces", "operators"],
        "front": "::",
        "back": "Scope resolution operator - used to access identifiers in a namespace",
        "source": "2.9 - Naming collisions and namespaces",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_9_004",
        "lesson": "2.9",
        "type": "cloze",
        "tags": ["cpp", "namespaces", "syntax"],
        "text": "To access a name in a namespace, use {{c1::namespaceName::identifier}}",
        "source": "2.9 - Naming collisions and namespaces",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_9_005",
        "lesson": "2.9",
        "type": "code",
        "tags": ["cpp", "namespaces", "syntax"],
        "question": "What does this code demonstrate?",
        "code": "#include <iostream>\n\nint main()\n{\n    std::cout << \"Hello\";\n    return 0;\n}",
        "answer": "Using the scope resolution operator to access cout from the std namespace",
        "explanation": "std::cout means 'cout from the std namespace'. The :: operator qualifies which namespace we're using.",
        "source": "2.9 - Naming collisions and namespaces",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_9_006",
        "lesson": "2.9",
        "type": "basic",
        "tags": ["cpp", "namespaces", "std"],
        "front": "What does std stand for in C++?",
        "back": "Standard - the namespace containing all standard library functionality.",
        "source": "2.9 - Naming collisions and namespaces",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_9_007",
        "lesson": "2.9",
        "type": "code",
        "tags": ["cpp", "namespaces", "common-mistakes"],
        "question": "What's wrong with this code?",
        "code": "#include <iostream>\n\nint main()\n{\n    cout << \"Hello\";  // error\n    return 0;\n}",
        "answer": "cout is not qualified with std::. Use std::cout instead.",
        "explanation": "cout is in the std namespace, so you must write std::cout to access it (unless using 'using' directives).",
        "source": "2.9 - Naming collisions and namespaces",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_9_008",
        "lesson": "2.9",
        "type": "concept",
        "tags": ["cpp", "namespaces", "best-practices"],
        "concept": "Why use namespaces",
        "explanation": "Namespaces prevent naming collisions by grouping related identifiers. Different namespaces can have identifiers with the same name without conflict.",
        "examples": [
            "namespace foo { void print() {} }",
            "namespace bar { void print() {} }",
            "foo::print();  // calls foo's version",
            "bar::print();  // calls bar's version"
        ],
        "source": "2.9 - Naming collisions and namespaces",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_9_009",
        "lesson": "2.9",
        "type": "basic",
        "tags": ["cpp", "namespaces", "fundamentals"],
        "front": "Can identifiers in different namespaces have the same name?",
        "back": "Yes. Namespaces prevent collisions, so different namespaces can contain identifiers with identical names.",
        "source": "2.9 - Naming collisions and namespaces",
        "difficulty": "medium"
    })

    return cards


def create_cards_2_10(lesson):
    """Lesson 2.10 - Introduction to the preprocessor"""
    cards = []

    cards.append({
        "id": "ch2_10_001",
        "lesson": "2.10",
        "type": "basic",
        "tags": ["cpp", "preprocessor", "fundamentals"],
        "front": "What is the preprocessor?",
        "back": "A program that processes your code before compilation, handling directives that begin with #.",
        "source": "2.10 - Introduction to the preprocessor",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_10_002",
        "lesson": "2.10",
        "type": "basic",
        "tags": ["cpp", "preprocessor", "directives"],
        "front": "What is a preprocessor directive?",
        "back": "An instruction to the preprocessor that begins with # and doesn't end with a semicolon.",
        "source": "2.10 - Introduction to the preprocessor",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_10_003",
        "lesson": "2.10",
        "type": "cloze",
        "tags": ["cpp", "preprocessor", "syntax"],
        "text": "Preprocessor directives start with {{c1::#}} and do not end with a {{c2::semicolon}}.",
        "source": "2.10 - Introduction to the preprocessor",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_10_004",
        "lesson": "2.10",
        "type": "basic",
        "tags": ["cpp", "preprocessor", "include"],
        "front": "What does #include do?",
        "back": "Replaces the #include directive with the contents of the specified file.",
        "source": "2.10 - Introduction to the preprocessor",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_10_005",
        "lesson": "2.10",
        "type": "cloze",
        "tags": ["cpp", "preprocessor", "syntax"],
        "text": "Use {{c1::#include <filename>}} for standard library headers and {{c2::#include \"filename\"}} for user-defined headers.",
        "source": "2.10 - Introduction to the preprocessor",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_10_006",
        "lesson": "2.10",
        "type": "reverse",
        "tags": ["cpp", "preprocessor", "terminology"],
        "front": "macro",
        "back": "A rule that defines how to transform input text into replacement output text",
        "source": "2.10 - Introduction to the preprocessor",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_10_007",
        "lesson": "2.10",
        "type": "cloze",
        "tags": ["cpp", "preprocessor", "macros"],
        "text": "To define a macro, use {{c1::#define}} followed by the macro name and replacement text.",
        "source": "2.10 - Introduction to the preprocessor",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_10_008",
        "lesson": "2.10",
        "type": "concept",
        "tags": ["cpp", "preprocessor", "macros"],
        "concept": "Object-like macros",
        "explanation": "Simple macros that replace a name with text. They don't use parentheses.",
        "examples": [
            "#define MAX_VALUE 100",
            "int x = MAX_VALUE;  // becomes: int x = 100;"
        ],
        "source": "2.10 - Introduction to the preprocessor",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_10_009",
        "lesson": "2.10",
        "type": "basic",
        "tags": ["cpp", "preprocessor", "conditional"],
        "front": "What do conditional compilation directives do?",
        "back": "Allow you to conditionally include or exclude code based on preprocessor conditions (#ifdef, #ifndef, #if, etc.).",
        "source": "2.10 - Introduction to the preprocessor",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_10_010",
        "lesson": "2.10",
        "type": "basic",
        "tags": ["cpp", "preprocessor", "best-practices"],
        "front": "When does the preprocessor run?",
        "back": "Before compilation - it processes directives and produces the modified source that the compiler then compiles.",
        "source": "2.10 - Introduction to the preprocessor",
        "difficulty": "medium"
    })

    return cards


def create_cards_2_11(lesson):
    """Lesson 2.11 - Header files"""
    cards = []

    cards.append({
        "id": "ch2_11_001",
        "lesson": "2.11",
        "type": "basic",
        "tags": ["cpp", "header-files", "fundamentals"],
        "front": "What is a header file?",
        "back": "A file (usually .h or .hpp) that contains forward declarations and is included in other files using #include.",
        "source": "2.11 - Header files",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_11_002",
        "lesson": "2.11",
        "type": "basic",
        "tags": ["cpp", "header-files", "best-practices"],
        "front": "What should you put in header files?",
        "back": "- Forward declarations\n- Function prototypes\n- Type definitions\n- Inline functions\n(NOT function definitions or variables)",
        "source": "2.11 - Header files",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_11_003",
        "lesson": "2.11",
        "type": "cloze",
        "tags": ["cpp", "header-files", "syntax"],
        "text": "User-defined header files use {{c1::#include \"filename.h\"}} with quotes, while standard library headers use {{c2::#include <filename>}} with angle brackets.",
        "source": "2.11 - Header files",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_11_004",
        "lesson": "2.11",
        "type": "concept",
        "tags": ["cpp", "header-files", "project-organization"],
        "concept": "Header file purpose",
        "explanation": "Header files allow you to share declarations across multiple files without duplicating code.",
        "examples": [
            "// add.h",
            "#ifndef ADD_H",
            "#define ADD_H",
            "int add(int x, int y);",
            "#endif",
            "",
            "// Now multiple .cpp files can #include \"add.h\""
        ],
        "source": "2.11 - Header files",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_11_005",
        "lesson": "2.11",
        "type": "basic",
        "tags": ["cpp", "header-files", "header-guards"],
        "front": "What are header guards?",
        "back": "Preprocessor directives (#ifndef, #define, #endif) that prevent a header file from being included multiple times in the same file.",
        "source": "2.11 - Header files",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_11_006",
        "lesson": "2.11",
        "type": "code",
        "tags": ["cpp", "header-files", "header-guards"],
        "question": "What is the purpose of this pattern?",
        "code": "#ifndef MYHEADER_H\n#define MYHEADER_H\n\n// declarations here\n\n#endif",
        "answer": "Header guard - prevents the header from being included multiple times",
        "explanation": "The first time this is included, MYHEADER_H isn't defined, so the content is included. Subsequent inclusions skip the content since MYHEADER_H is now defined.",
        "source": "2.11 - Header files",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_11_007",
        "lesson": "2.11",
        "type": "cloze",
        "tags": ["cpp", "header-files", "header-guards"],
        "text": "A header guard consists of {{c1::#ifndef}}, {{c2::#define}}, and {{c3::#endif}} directives.",
        "source": "2.11 - Header files",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_11_008",
        "lesson": "2.11",
        "type": "basic",
        "tags": ["cpp", "header-files", "best-practices"],
        "front": "What naming convention should header guards use?",
        "back": "Typically the header filename in uppercase with underscores, ending in _H (e.g., MY_HEADER_H).",
        "source": "2.11 - Header files",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_11_009",
        "lesson": "2.11",
        "type": "code",
        "tags": ["cpp", "header-files", "common-mistakes"],
        "question": "What's wrong with this header file?",
        "code": "// math.h\nint add(int x, int y)\n{\n    return x + y;\n}",
        "answer": "Header files should contain declarations, not definitions. Move the function body to a .cpp file.",
        "explanation": "Putting function definitions in headers can lead to multiple definition errors when the header is included in multiple .cpp files.",
        "source": "2.11 - Header files",
        "difficulty": "hard"
    })

    cards.append({
        "id": "ch2_11_010",
        "lesson": "2.11",
        "type": "basic",
        "tags": ["cpp", "header-files", "best-practices"],
        "front": "Why shouldn't you put function definitions in header files?",
        "back": "If multiple .cpp files include the header, each gets a copy of the definition, causing multiple definition linker errors.",
        "source": "2.11 - Header files",
        "difficulty": "hard"
    })

    cards.append({
        "id": "ch2_11_011",
        "lesson": "2.11",
        "type": "basic",
        "tags": ["cpp", "header-files", "best-practices"],
        "front": "What's the typical file extension for C++ header files?",
        "back": ".h or .hpp (both are common, .h is more traditional)",
        "source": "2.11 - Header files",
        "difficulty": "easy"
    })

    return cards


def create_cards_2_12(lesson):
    """Lesson 2.12 - Header guards"""
    cards = []

    cards.append({
        "id": "ch2_12_001",
        "lesson": "2.12",
        "type": "basic",
        "tags": ["cpp", "header-guards", "preprocessor"],
        "front": "What problem do header guards solve?",
        "back": "They prevent a header file from being included multiple times in the same translation unit, which would cause redefinition errors.",
        "source": "2.12 - Header guards",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_12_002",
        "lesson": "2.12",
        "type": "concept",
        "tags": ["cpp", "header-guards", "best-practices"],
        "concept": "Header guard structure",
        "explanation": "Header guards use conditional compilation to include header contents only once per translation unit.",
        "examples": [
            "#ifndef UNIQUE_NAME_H  // if not defined",
            "#define UNIQUE_NAME_H  // define it",
            "// header contents",
            "#endif  // end of guard"
        ],
        "source": "2.12 - Header guards",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_12_003",
        "lesson": "2.12",
        "type": "code",
        "tags": ["cpp", "header-guards", "syntax"],
        "question": "Complete the header guard:",
        "code": "// square.h\n#ifndef SQUARE_H\n#define SQUARE_H\n\nint getSquare(int x);\n\n???",
        "answer": "#endif",
        "explanation": "Every header guard must end with #endif to close the conditional compilation block.",
        "source": "2.12 - Header guards",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_12_004",
        "lesson": "2.12",
        "type": "basic",
        "tags": ["cpp", "header-guards", "best-practices"],
        "front": "What happens if you forget header guards?",
        "back": "If a header is included multiple times in the same file, you'll get redefinition compile errors.",
        "source": "2.12 - Header guards",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_12_005",
        "lesson": "2.12",
        "type": "cloze",
        "tags": ["cpp", "header-guards", "best-practices"],
        "text": "Every header file should have a {{c1::header guard}} to prevent multiple inclusion problems.",
        "source": "2.12 - Header guards",
        "difficulty": "easy"
    })

    cards.append({
        "id": "ch2_12_006",
        "lesson": "2.12",
        "type": "basic",
        "tags": ["cpp", "header-guards", "pragma"],
        "front": "What is #pragma once?",
        "back": "A non-standard but widely supported alternative to header guards that prevents multiple inclusion.",
        "source": "2.12 - Header guards",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_12_007",
        "lesson": "2.12",
        "type": "concept",
        "tags": ["cpp", "header-guards", "pragma"],
        "concept": "#pragma once vs traditional header guards",
        "explanation": "#pragma once is simpler but not part of the C++ standard. Traditional header guards are standard-compliant.",
        "examples": [
            "// Option 1: #pragma once",
            "#pragma once",
            "// declarations",
            "",
            "// Option 2: traditional",
            "#ifndef HEADER_H",
            "#define HEADER_H",
            "// declarations",
            "#endif"
        ],
        "source": "2.12 - Header guards",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_12_008",
        "lesson": "2.12",
        "type": "basic",
        "tags": ["cpp", "header-guards", "best-practices"],
        "front": "What makes a good header guard macro name?",
        "back": "Unique, based on the file name, typically uppercase with underscores, avoiding reserved names (don't start with underscore + capital).",
        "source": "2.12 - Header guards",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_12_009",
        "lesson": "2.12",
        "type": "code",
        "tags": ["cpp", "header-guards", "common-mistakes"],
        "question": "What's wrong with this header guard?",
        "code": "// myfile.h\n#ifndef _MYFILE_H\n#define _MYFILE_H\n// ...\n#endif",
        "answer": "Names starting with underscore followed by capital letter are reserved. Use MYFILE_H instead.",
        "explanation": "Identifiers starting with underscore and capital letter are reserved for the implementation. Avoid them in your code.",
        "source": "2.12 - Header guards",
        "difficulty": "hard"
    })

    return cards


def create_cards_2_13(lesson):
    """Lesson 2.13 - How to design your first programs"""
    cards = []

    cards.append({
        "id": "ch2_13_001",
        "lesson": "2.13",
        "type": "concept",
        "tags": ["cpp", "design", "best-practices"],
        "concept": "Program design steps",
        "explanation": "Before coding, plan your program:\n1. Define the problem\n2. Design the solution\n3. Write the program\n4. Compile and test\n5. Debug",
        "examples": [
            "Don't jump straight to coding",
            "Think about structure first",
            "Break down the problem",
            "Plan your functions"
        ],
        "source": "2.13 - How to design your first programs",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_13_002",
        "lesson": "2.13",
        "type": "basic",
        "tags": ["cpp", "design", "best-practices"],
        "front": "What should you do before writing code?",
        "back": "Plan and design your solution:\n- Understand the problem\n- Break it into steps\n- Identify needed functions\n- Consider data flow",
        "source": "2.13 - How to design your first programs",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_13_003",
        "lesson": "2.13",
        "type": "basic",
        "tags": ["cpp", "design", "best-practices"],
        "front": "How should you approach a complex problem?",
        "back": "Break it down into smaller sub-problems. Solve each sub-problem with a separate function.",
        "source": "2.13 - How to design your first programs",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_13_004",
        "lesson": "2.13",
        "type": "concept",
        "tags": ["cpp", "design", "best-practices"],
        "concept": "Top-down design",
        "explanation": "Start with the high-level structure (main function), then break down into smaller functions for specific tasks.",
        "examples": [
            "// Start with main",
            "int main() {",
            "    getUserInput();",
            "    processData();",
            "    displayResults();",
            "}",
            "// Then implement each function"
        ],
        "source": "2.13 - How to design your first programs",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_13_005",
        "lesson": "2.13",
        "type": "basic",
        "tags": ["cpp", "design", "best-practices"],
        "front": "What is the benefit of breaking a program into functions?",
        "back": "- Easier to understand\n- Easier to test each part\n- Easier to reuse code\n- Easier to maintain and update",
        "source": "2.13 - How to design your first programs",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_13_006",
        "lesson": "2.13",
        "type": "basic",
        "tags": ["cpp", "design", "testing"],
        "front": "When should you test your program?",
        "back": "Test early and often. Test each function as you write it, not just at the end.",
        "source": "2.13 - How to design your first programs",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_13_007",
        "lesson": "2.13",
        "type": "basic",
        "tags": ["cpp", "design", "best-practices"],
        "front": "What makes a good function?",
        "back": "- Does one thing well\n- Has a clear purpose\n- Has a descriptive name\n- Is relatively short\n- Is reusable",
        "source": "2.13 - How to design your first programs",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_13_008",
        "lesson": "2.13",
        "type": "concept",
        "tags": ["cpp", "design", "best-practices"],
        "concept": "Iterative development",
        "explanation": "Build your program incrementally. Write a little, test a little. Don't try to write everything at once.",
        "examples": [
            "1. Write main() skeleton",
            "2. Add one function",
            "3. Test it",
            "4. Add next function",
            "5. Test again",
            "Repeat until complete"
        ],
        "source": "2.13 - How to design your first programs",
        "difficulty": "medium"
    })

    return cards


def create_cards_2_x(lesson):
    """Lesson 2.x - Chapter 2 summary and quiz"""
    cards = []

    cards.append({
        "id": "ch2_x_001",
        "lesson": "2.x",
        "type": "concept",
        "tags": ["cpp", "functions", "summary"],
        "concept": "Chapter 2 Key Concepts",
        "explanation": "Functions are the fundamental building blocks of C++ programs. They enable code reuse, organization, and modularity.",
        "examples": [
            "- Functions execute reusable sequences of statements",
            "- Parameters pass data into functions",
            "- Return values pass data back to callers",
            "- Local scope isolates variables",
            "- Forward declarations allow flexible ordering"
        ],
        "source": "2.x - Chapter 2 summary",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_x_002",
        "lesson": "2.x",
        "type": "basic",
        "tags": ["cpp", "functions", "summary"],
        "front": "What are the key components of a function?",
        "back": "- Return type\n- Function name\n- Parameter list (can be empty)\n- Function body\n- Return statement (for non-void)",
        "source": "2.x - Chapter 2 summary",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_x_003",
        "lesson": "2.x",
        "type": "basic",
        "tags": ["cpp", "header-files", "summary"],
        "front": "What's the standard multi-file organization pattern?",
        "back": "- .h files: forward declarations and prototypes\n- .cpp files: function definitions\n- Header guards in all .h files\n- #include headers where needed",
        "source": "2.x - Chapter 2 summary",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_x_004",
        "lesson": "2.x",
        "type": "basic",
        "tags": ["cpp", "preprocessor", "summary"],
        "front": "What are the main preprocessor directives covered in Chapter 2?",
        "back": "#include - include files\n#define - define macros\n#ifndef/#define/#endif - header guards\n#pragma once - alternative header guard",
        "source": "2.x - Chapter 2 summary",
        "difficulty": "medium"
    })

    cards.append({
        "id": "ch2_x_005",
        "lesson": "2.x",
        "type": "concept",
        "tags": ["cpp", "best-practices", "summary"],
        "concept": "Chapter 2 Best Practices",
        "explanation": "Follow these practices for better C++ code organization and maintainability.",
        "examples": [
            "- Always use header guards",
            "- Put declarations in .h, definitions in .cpp",
            "- One function, one purpose",
            "- Use descriptive function names",
            "- Prefix std:: for standard library",
            "- Test incrementally as you build"
        ],
        "source": "2.x - Chapter 2 summary",
        "difficulty": "hard"
    })

    return cards


def process_lesson(lesson_file, output_dir, lesson_num, create_cards_func):
    """Process a single lesson file"""
    try:
        with open(lesson_file, 'r', encoding='utf-8') as f:
            lesson = json.load(f)

        cards = create_cards_func(lesson)

        output = {
            "chapter": "Chapter 2",
            "chapter_title": "Functions and Files",
            "lesson": lesson_num,
            "lesson_title": lesson.get('title', f'Lesson {lesson_num}'),
            "total_cards": len(cards),
            "cards": cards
        }

        output_file = output_dir / f'{lesson_num}.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        return len(cards), None
    except Exception as e:
        return 0, str(e)


def main():
    # Find Chapter 2 directory (handles non-breaking space)
    lessons_dir = pathlib.Path('/Users/stefan/Desktop/learnCPP/learncpp-anki-deck/content/lessons')
    chapter2_dir = None
    for d in lessons_dir.iterdir():
        if d.is_dir() and d.name.startswith('Chapter') and d.name.split()[-1] == '2':
            chapter2_dir = d
            break

    if not chapter2_dir:
        print("ERROR: Could not find Chapter 2 directory")
        return

    output_dir = pathlib.Path('/Users/stefan/Desktop/learnCPP/learncpp-anki-deck/deck/chapter_2')
    output_dir.mkdir(parents=True, exist_ok=True)

    # Map of lesson numbers to card creation functions
    lessons = {
        '2_1': create_cards_2_1,
        '2_2': create_cards_2_2,
        '2_3': create_cards_2_3,
        '2_4': create_cards_2_4,
        '2_5': create_cards_2_5,
        '2_6': create_cards_2_6,
        '2_7': create_cards_2_7,
        '2_8': create_cards_2_8,
        '2_9': create_cards_2_9,
        '2_10': create_cards_2_10,
        '2_11': create_cards_2_11,
        '2_12': create_cards_2_12,
        '2_13': create_cards_2_13,
        '2_x': create_cards_2_x,
    }

    total_cards = 0
    total_lessons = 0
    errors = []

    print("=" * 60)
    print("GENERATING ANKI FLASHCARDS FOR CHAPTER 2")
    print("=" * 60)

    for lesson_file, create_func in lessons.items():
        lesson_path = chapter2_dir / f'{lesson_file}.json'
        if lesson_path.exists():
            card_count, error = process_lesson(lesson_path, output_dir, lesson_file.replace('_', '.'), create_func)
            if error:
                errors.append(f"{lesson_file}: {error}")
                print(f"✗ {lesson_file}: ERROR - {error}")
            else:
                total_cards += card_count
                total_lessons += 1
                print(f"✓ {lesson_file}: Created {card_count} cards")
        else:
            print(f"✗ {lesson_file}: File not found")

    print("=" * 60)
    print(f"SUMMARY:")
    print(f"  Lessons processed: {total_lessons}/14")
    print(f"  Total cards created: {total_cards}")
    if errors:
        print(f"  Errors: {len(errors)}")
        for error in errors:
            print(f"    - {error}")
    else:
        print(f"  Errors: 0")
    print("=" * 60)

if __name__ == "__main__":
    main()
