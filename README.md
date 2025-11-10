# LearnCPP.com Anki Deck Generator

Automated system to convert LearnCPP.com tutorials into high-quality Anki flashcards for effective C++ learning.

## Project Structure

```
learncpp-anki-deck/
├── scraper/           # Web scraping scripts
├── content/           # Downloaded chapter content
├── decks/            # Generated Anki decks
└── scripts/          # Card generation and utility scripts
```

## Features

- Scrapes all chapters from LearnCPP.com (1.x through 28.x)
- Converts content into atomic, single-concept flashcards
- Extracts and transforms quiz questions
- Generates properly formatted code cards
- Creates cloze deletions for syntax and definitions
- Follows Anki best practices for optimal learning

## Card Types

1. **Concept cards** - Basic Q&A for definitions and explanations
2. **Syntax cards** - Cloze deletions for C++ syntax
3. **Code analysis** - Understanding code snippets
4. **Error identification** - Common mistakes and fixes
5. **Quiz cards** - Transformed from chapter quizzes

## Usage

```bash
# Scrape all content
python scripts/scrape_learncpp.py

# Generate Anki deck
python scripts/generate_deck.py

# Output: decks/learncpp_complete.apkg
```

## Design Principles

- **One concept per card** - Each card tests exactly one piece of knowledge
- **Atomic information** - Complex topics broken into simple facts
- **Context prefixes** - All cards prefixed with "C++:" for context
- **8-10 second rule** - Cards answerable in under 10 seconds
- **No enumeration** - Lists broken into individual cards
- **Active recall** - Questions, not statements

## Progress Tracking

See [PROGRESS.md](PROGRESS.md) for chapter completion status.# learncpp-anki-deck
