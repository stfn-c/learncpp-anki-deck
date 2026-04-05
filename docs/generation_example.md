# Card Generation Example

This document shows how to use the AI prompt to generate cards from lesson content.

## Quick Start

1. **Read the generation prompt**: `docs/ai_card_generation_prompt.md`
2. **Get lesson content**: From `content/lessons/Chapter_X/X_Y.json`
3. **Feed to AI**: Use prompt + lesson content
4. **Get output**: AI generates `deck/chapter_X/X_Y.json`
5. **Build**: Run `python src/build_deck.py`

## Example Workflow

### Step 1: Get Lesson Content

```bash
# View a lesson's content
cat content/lessons/Chapter\ 1/1_1.json
```

This gives you the scraped content with sections, code, and quiz questions.

### Step 2: Prompt the AI

**System prompt** (from `ai_card_generation_prompt.md`):
```
You are an AI specialized in creating high-quality Anki flashcards
from C++ educational content...
[full prompt from the file]
```

**User message**:
```
Generate Anki cards for this lesson:

[paste the lesson JSON content here]

Output the complete JSON following the schema, ready to save as
deck/chapter_1/1_1.json
```

### Step 3: AI Generates Cards

The AI will output something like:

```json
{
  "chapter": "Chapter 1",
  "chapter_title": "C++ Basics",
  "lesson": "1.1",
  "lesson_title": "Statements and the structure of a program",
  "total_cards": 12,
  "cards": [
    {
      "id": "ch1_1_001",
      "lesson": "1.1",
      "type": "basic",
      "tags": ["cpp", "basics", "statements"],
      "front": "What is a statement in C++?",
      "back": "A statement is an instruction that tells the computer to perform an action. Every statement ends with a semicolon.",
      "source": "1.1 - Statements and the structure of a program",
      "difficulty": "easy"
    },
    // ... more cards
  ]
}
```

### Step 4: Save and Build

```bash
# Save the output
# AI output -> deck/chapter_1/1_1.json

# Build the deck
python src/build_deck.py

# Output: build/version_1.apkg
```

### Step 5: Test in Anki

Import `build/version_1.apkg` into Anki and review the cards.

## Using with Claude

If using Claude (or similar AI):

```
System: [paste ai_card_generation_prompt.md content]

User: Generate Anki cards from this LearnCPP lesson:

[paste content from content/lessons/Chapter_1/1_1.json]

Please output complete, valid JSON following the schema.
```

## Using with OpenAI API

```python
import openai
import json

# Read the prompt
with open('docs/ai_card_generation_prompt.md') as f:
    system_prompt = f.read()

# Read lesson content
with open('content/lessons/Chapter 1/1_1.json') as f:
    lesson = json.load(f)

# Generate cards
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Generate Anki cards from this lesson:\n\n{json.dumps(lesson, indent=2)}"}
    ]
)

# Parse and save
cards_json = response.choices[0].message.content
with open('deck/chapter_1/1_1.json', 'w') as f:
    f.write(cards_json)
```

## Batch Processing

To generate cards for multiple lessons:

```bash
# Pseudo-code workflow
for lesson in content/lessons/Chapter_1/*.json; do
  lesson_num=$(basename "$lesson" .json)

  # 1. Read lesson content
  content=$(cat "$lesson")

  # 2. Send to AI with prompt
  # (using your preferred AI tool/API)

  # 3. Save output to deck/chapter_1/${lesson_num}.json

  # 4. Validate JSON
  python -m json.tool "deck/chapter_1/${lesson_num}.json" > /dev/null

done

# 5. Build final deck
python src/build_deck.py
```

## Quality Review

After generation, review cards for:

1. **Correctness**: Technical accuracy
2. **Clarity**: Question makes sense
3. **Atomicity**: One concept per card
4. **Difficulty**: Appropriate level
5. **Value**: Actually useful to learn from

## Tips

- Start with 1-2 lessons to test the prompt
- Iterate on the prompt if cards aren't good quality
- Review and manually edit generated cards
- Build and test in Anki frequently
- Commit good versions to git

## Automation Ideas

1. **Full automation**: Script that processes all 356 lessons
2. **Semi-automation**: Generate cards, manual review, commit
3. **Continuous**: Generate cards as lessons are updated
4. **Parallel**: Use multiple AI instances for faster generation

## Common Issues

**JSON syntax errors:**
```bash
# Validate JSON
python -m json.tool deck/chapter_1/1_1.json
```

**Missing fields:**
- Check against schema in `docs/card_schema.md`

**Poor quality cards:**
- Adjust the system prompt
- Add examples of bad vs good cards
- Be more specific about what to avoid

**Too many/few cards:**
- Adjust target card count in prompt
- Focus on key concepts only
