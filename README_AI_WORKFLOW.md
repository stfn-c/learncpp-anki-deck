# LearnCPP AI-Generated Anki Cards Workflow

## Overview
This project uses AI agents to intelligently read LearnCPP.com content and generate high-quality Anki cards. The workflow consists of three phases:

1. **Content Scraping**: Already completed - 356 lessons from 35 chapters scraped
2. **AI Card Generation**: AI agents read individual lessons and generate JSON cards per lesson
3. **Anki Deck Creation**: Python script converts JSON to Anki deck with hierarchical subdecks for each lesson

## Directory Structure
```
learncpp-anki-deck/
├── deck/                    # Current working deck (organize by chapter)
│   ├── chapter_0/
│   ├── chapter_1/
│   │   ├── 1_1.json
│   │   ├── 1_2.json
│   │   └── ...
│   └── ...
├── build/                   # Built Anki decks (versioned)
│   ├── version_1.apkg
│   ├── version_2.apkg
│   └── ...
├── content/
│   ├── index.json          # Complete index of all lessons
│   └── lessons/            # Scraped lesson content (356 files)
├── src/
│   ├── build_deck.py       # Build versioned .apkg from deck/
│   ├── lesson_scraper.py   # Single-threaded scraper
│   ├── lesson_scraper_parallel.py  # Parallel scraper
│   └── json_to_anki.py     # JSON to Anki converter
└── docs/
    └── card_schema.md      # JSON schema for AI-generated cards
```

## AI Card Generation Guidelines

### Core Principles
1. **One atomic concept per card** - Each card tests exactly one thing
2. **No memorization-based cards** - Focus on understanding, not rote learning
3. **Include code context** - Keep code examples with their explanations
4. **Progressive difficulty** - Mix easy, medium, and hard cards
5. **Practical focus** - Include common mistakes, best practices, gotchas

### Card Types

#### 1. Basic (Q&A)
```json
{
  "type": "basic",
  "front": "Question text",
  "back": "Answer text"
}
```

#### 2. Cloze (Fill-in-the-blank)
```json
{
  "type": "cloze",
  "text": "In C++, {{c1::int x = 5;}} is {{c2::copy initialization}}"
}
```

#### 3. Code (Code comprehension)
```json
{
  "type": "code",
  "question": "What does this output?",
  "code": "std::cout << \"Hello\";",
  "answer": "Hello",
  "explanation": "Why it works this way..."
}
```

#### 4. Reverse (Bidirectional)
```json
{
  "type": "reverse",
  "front": "<<",
  "back": "Insertion operator for std::cout"
}
```

#### 5. Concept (Understanding)
```json
{
  "type": "concept",
  "concept": "RAII",
  "explanation": "Resource Acquisition Is Initialization...",
  "examples": ["unique_ptr example", "lock_guard example"]
}
```

## Workflow Steps

### Step 1: AI Card Generation
For each lesson, an AI agent should:

1. Read a single lesson file from `content/lessons/Chapter_X/X_Y.json`
2. Analyze content to identify key concepts
3. Generate cards following the schema
4. Output JSON to `deck/chapter_X/X_Y.json`

Example:
```bash
# AI reads lesson and generates cards
# Input:  content/lessons/Chapter_1/1_1.json
# Output: deck/chapter_1/1_1.json
```

### Step 2: Build Anki Deck

```bash
# Build deck with auto-incremented version
python src/build_deck.py

# Output: build/version_X.apkg (X auto-increments)

# Or specify version
python src/build_deck.py --version 5
```

## JSON Schema Requirements

Each lesson JSON file must follow this structure:
```json
{
  "chapter": "Chapter 1",
  "chapter_title": "C++ Basics",
  "lesson": "1.1",
  "lesson_title": "Introduction to variables",
  "total_cards": 15,
  "cards": [
    {
      "id": "ch1_001",
      "lesson": "1.1",
      "type": "basic|cloze|code|reverse|concept",
      "tags": ["cpp", "basics", "topic"],
      "source": "1.1 - Lesson Title",
      "difficulty": "easy|medium|hard",
      // Type-specific fields...
    }
  ]
}
```

## Quality Guidelines for AI Agents

### What Makes a Good Card
- Tests understanding, not memorization
- Has one clear answer
- Provides sufficient context
- Uses practical examples
- Includes common edge cases

### What to Avoid
- Trivial facts (e.g., "Who created C++?")
- Overly complex multi-concept questions
- Ambiguous questions with multiple valid answers
- Pure syntax memorization without context
- Cards that become outdated with language changes

### Special Considerations
1. **Code Writing Questions**: Include these even though Anki can't verify code
2. **Quiz Questions**: Convert all quiz questions from lessons
3. **Best Practices**: Create cards for recommended patterns
4. **Common Mistakes**: Create cards for typical errors
5. **Comparisons**: Create cards comparing similar concepts

## Current Status

✅ **Completed:**
- Scraped all 356 lessons from LearnCPP.com
- Created parallel scraper (5x speed improvement)
- Defined JSON schema for cards
- Built JSON to Anki converter with subdeck support
- Tested converter with sample data

📝 **Next Steps:**
1. Use AI agents to read each lesson individually
2. Generate JSON cards for each lesson (356 JSON files total)
3. Review and refine generated cards
4. Create final Anki deck with full subdeck hierarchy

## Usage Example

```bash
# 1. AI generates cards for a lesson
# Input:  content/lessons/Chapter_1/1_1.json (scraped content)
# Output: deck/chapter_1/1_1.json (AI-generated cards)

# 2. Build the deck
python src/build_deck.py
# Creates: build/version_1.apkg

# 3. Make edits to cards in deck/ folder

# 4. Rebuild with new version
python src/build_deck.py
# Creates: build/version_2.apkg

# 5. Import version_X.apkg into Anki and test
```

## Statistics
- **Total Lessons**: 356
- **Total Chapters**: 35 (Chapter 0 through Chapter 28 + Appendices)
- **Expected Cards**: ~3000-5000 high-quality cards
- **Subdeck Structure**:
  - Main deck: LearnCPP
  - Chapter decks: 35 (e.g., LearnCPP::Chapter 1 - C++ Basics)
  - Lesson subdecks: 356 (e.g., LearnCPP::Chapter 1 - C++ Basics::1.1 - Introduction to variables)

## Notes
- The converter creates hierarchical decks (LearnCPP::Chapter 1 - C++ Basics)
- All cards use minimalist styling (no gradients, no rounded corners)
- Night mode is supported
- Cards preserve code formatting and syntax