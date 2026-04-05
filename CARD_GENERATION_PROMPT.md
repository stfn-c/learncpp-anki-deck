# Anki Card Generation Prompt

## Mission

Create pragmatic, practical Anki flashcards from LearnCPP.com lessons. Focus on helping developers actually write C++ code, not just memorize theory.

## CRITICAL: Anki Uses HTML, Not Plain Text

**All card content is HTML.** Use proper HTML formatting:
- Line breaks: `<br>` (NOT `\n`)
- Lists: `<ul><li>item</li></ul>` (NOT `- item`)
- Escape special chars: `&lt;` for `<`, `&gt;` for `>`, `&amp;` for `&`

## Output Format

Create JSON files in `deck/chapter_X/X_Y.json`:

```json
{
  "chapter": "Chapter X",
  "chapter_title": "Chapter Title",
  "lesson": "X.Y",
  "lesson_title": "Lesson Title",
  "total_cards": 12,
  "cards": [...]
}
```

## Card Types (5 types available)

### 1. Basic - Simple Q&A

**Use for:** Specific, clear questions with definite answers

```json
{
  "id": "ch4_1_001",
  "lesson": "4.1",
  "type": "basic",
  "tags": ["cpp", "types", "fundamentals"],
  "front": "What value does an uninitialized int variable contain?",
  "back": "Garbage value (indeterminate). It contains whatever was previously in that memory location.",
  "source": "4.1 - Introduction to fundamental data types",
  "difficulty": "easy"
}
```

**Question style - Be SPECIFIC:**
- ✅ "What value does an uninitialized int contain?"
- ✅ "What happens when you dereference a null pointer?"
- ✅ "What is the minimum guaranteed size of int in bytes?"
- ❌ "Explain variables" (too vague)
- ❌ "What about initialization?" (unclear)
- ❌ "Describe const" (too open-ended)

### 2. Cloze - Fill-in-the-blank

**Use heavily for:** Syntax, code patterns, terminology in context

```json
{
  "id": "ch4_1_002",
  "lesson": "4.1",
  "type": "cloze",
  "tags": ["cpp", "types", "syntax"],
  "text": "To initialize an int to zero using brace initialization, write {{c1::int x{};}} or {{c2::int x{0};}}",
  "source": "4.1 - Introduction to fundamental data types",
  "difficulty": "easy"
}
```

**Good cloze patterns:**
- Syntax: "To declare a const variable: {{c1::const int x = 5;}}"
- Code completion: "std::{{c1::cout}} &lt;&lt; {{c2::\"Hello\"}};"
- Fill-in-blank: "The {{c1::sizeof}} operator returns size in {{c2::bytes}}"

### 3. Code - Code comprehension

```json
{
  "id": "ch4_2_003",
  "lesson": "4.2",
  "type": "code",
  "tags": ["cpp", "void", "common-mistakes"],
  "question": "What's wrong with this code?",
  "code": "void x;\nstd::cout &lt;&lt; x;",
  "answer": "Cannot declare a variable of type void. Void is an incomplete type.",
  "explanation": "void can only be used as a return type or in void pointers (void*), not for regular variables.",
  "source": "4.2 - Void",
  "difficulty": "medium"
}
```

### 4. Reverse - Bidirectional term/definition

```json
{
  "id": "ch4_1_004",
  "lesson": "4.1",
  "type": "reverse",
  "tags": ["cpp", "operators"],
  "front": "sizeof",
  "back": "Operator that returns the size of a type or object in bytes",
  "source": "4.3 - Object sizes and sizeof",
  "difficulty": "easy"
}
```

### 5. Concept - Deep understanding with examples

```json
{
  "id": "ch4_1_005",
  "lesson": "4.1",
  "type": "concept",
  "tags": ["cpp", "best-practices", "initialization"],
  "concept": "Why initialize variables when declaring them",
  "explanation": "Uninitialized variables contain garbage values (whatever was previously in memory), leading to undefined behavior and bugs that are hard to track.",
  "examples": [
    "int x{};      // good: brace init to 0",
    "int y = 5;    // good: copy initialization",
    "int z;        // bad: garbage value"
  ],
  "source": "4.1 - Introduction to fundamental data types",
  "difficulty": "medium"
}
```

## HTML FORMATTING RULES

### Lists - Use HTML Tags

❌ **WRONG (plain text):**
```json
{
  "back": "Fundamental types:\n- int\n- float\n- char"
}
```

✅ **CORRECT (HTML):**
```json
{
  "back": "Fundamental types:<ul><li>int (integers)</li><li>float (floating point)</li><li>char (characters)</li><li>bool (boolean)</li></ul>"
}
```

### Line Breaks - Use `<br>` Tag

❌ **WRONG:**
```json
{
  "back": "First line\nSecond line\nThird line"
}
```

✅ **CORRECT:**
```json
{
  "back": "First line<br>Second line<br>Third line"
}
```

### HTML Escaping - Required for C++ Operators

When writing C++ code with `<`, `>`, `&`:

```json
{
  "code": "std::cout &lt;&lt; x;  // &lt;&lt; is the insertion operator",
  "text": "Compare with {{c1::&lt;}} for less than and {{c2::&gt;}} for greater than"
}
```

**Escape rules:**
- `<` → `&lt;`
- `>` → `&gt;`
- `&` → `&amp;`
- `"` → `&quot;` (if needed)

## QUESTION QUALITY STANDARDS

### Questions Must Be SPECIFIC and CLEAR

❌ **Too vague:**
- "Explain const"
- "What about pointers?"
- "Describe initialization"
- "Global variables"

✅ **Specific and clear:**
- "What is the difference between const int* and int* const?"
- "What happens when you dereference a dangling pointer?"
- "What is the difference between copy initialization and direct initialization?"
- "Why are non-const global variables problematic?"

### Avoid "Explain: X" Format

Instead of generic "Explain:" questions, ask specific, targeted questions:

- ❌ "Explain: const variables"
- ✅ "What are two reasons to use const variables?"

- ❌ "Explain: static_cast"
- ✅ "When should you use static_cast instead of C-style casts?"

- ❌ "Explain: scope"
- ✅ "What is the difference between local scope and global scope?"

### Self-Check Before Creating Each Card

1. **Is the question specific?** Can it be answered in 5-10 seconds with concrete information?
2. **Does the question accidentally contain the answer?**
3. **Would someone who knows the material know exactly what I'm asking?**
4. **Is there ONE clear answer (or a small, well-defined set)?**
5. **Does it test practical understanding, not trivia?**

**If NO to any: revise or skip the card.**

## Card Distribution (Aim for 10-12 cards per lesson)

**INCREASE CLOZE USAGE:**
- **40% Cloze cards** - Syntax patterns, code completion, fill-in-blank
- **25% Code cards** - Code comprehension, "what's wrong", output prediction
- **20% Basic cards** - Specific Q&A (not vague "explain" questions)
- **10% Concept cards** - Best practices, gotchas with examples
- **5% Reverse cards** - Operators, symbols, key terms

## What to Create

### ✅ Always Include

- **Syntax patterns as cloze cards** - "To declare X: {{c1::code}}"
- **Code examples** - From the actual lesson
- **Common mistakes** - "What's wrong with this code?"
- **Specific questions** - Not "Explain X" but "What happens when X?"
- **Best practices** - Why/when to use certain approaches
- **Gotchas** - Subtle bugs and pitfalls
- **Quiz questions** - Convert lesson quizzes

### ❌ Skip These

- Vague "Explain: X" questions
- Historical trivia
- Questions where answer is in the question
- Overly open-ended questions

## Difficulty Levels

- **easy** (40%): Basic syntax, simple patterns, straightforward concepts
- **medium** (40%): Application, common patterns, code analysis
- **hard** (20%): Edge cases, subtle bugs, complex interactions

## Card ID Format

`ch{chapter}_{lesson}_{number}` with zero-padding:
- `ch4_1_001`
- `ch4_1_015`
- `ch12_3_042`

## Tags (2-4 per card)

1. Always: `cpp`
2. Topic: `types`, `functions`, `pointers`, etc.
3. Specific: `initialization`, `memory`, `syntax`, etc.
4. Optional: `best-practices`, `common-mistakes`, `gotchas`

## Examples of Well-Formatted Cards

### Example 1: Cloze with HTML escaping
```json
{
  "type": "cloze",
  "text": "The insertion operator {{c1::&lt;&lt;}} is used with std::cout to output data.",
  "tags": ["cpp", "iostream", "operators"]
}
```

### Example 2: Basic with specific question
```json
{
  "type": "basic",
  "front": "What is the minimum guaranteed range for signed int?",
  "back": "-32,768 to 32,767 (16-bit, 2 bytes minimum)",
  "tags": ["cpp", "types", "int"]
}
```

### Example 3: Code with HTML in answer
```json
{
  "type": "code",
  "question": "What does this code output?",
  "code": "int x{5};\nint y{10};\nstd::cout &lt;&lt; x + y;",
  "answer": "15",
  "explanation": "x + y evaluates to 5 + 10 = 15"
}
```

### Example 4: Concept with HTML list
```json
{
  "type": "concept",
  "concept": "When to avoid unsigned integers",
  "explanation": "Unsigned integers should be avoided in most cases because:<ul><li>Wraparound behavior causes subtle bugs</li><li>Mixing signed/unsigned causes unexpected conversions</li><li>Range checking becomes error-prone</li></ul>",
  "examples": [
    "int count = 0;  // Prefer signed for counters",
    "std::size_t len = vec.size();  // OK: size_t for sizes"
  ]
}
```

## Process

1. Read entire lesson JSON
2. Identify key syntax patterns → create cloze cards
3. Find code examples → create code cards
4. Note specific questions to ask → create basic cards (NOT "explain" cards)
5. Identify best practices/gotchas → create concept cards
6. **Quality check EACH card** - is question specific and clear?
7. **Format with proper HTML** - use `<br>`, `<ul><li>`, escape `<>&`
8. Verify JSON syntax
9. Output valid JSON file

## Final Checklist

- [ ] 40% of cards are cloze (syntax, code patterns)
- [ ] All HTML properly formatted (`<br>`, `<ul><li>`, escaped chars)
- [ ] NO `\n` for newlines (use `<br>`)
- [ ] NO plain text lists (use `<ul><li>`)
- [ ] Questions are SPECIFIC, not "Explain: X"
- [ ] Each card tests one atomic concept
- [ ] Questions don't give away answers
- [ ] Mix of card types and difficulties
- [ ] Card IDs follow format
- [ ] Valid JSON syntax

## Remember

You're creating flashcards for developers to actually write C++ code. Every card should be practical, specific, and useful for real programming work. Use HTML formatting properly so lists and formatting display correctly in Anki.
