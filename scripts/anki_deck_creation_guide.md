# Complete Guide to Creating Prolific Anki Decks (2024)

## Table of Contents
1. [Import Formats](#import-formats)
2. [Card Types](#card-types)
3. [Programmatic Generation with Python](#programmatic-generation-with-python)
4. [Bulk Generation Tools](#bulk-generation-tools)
5. [Media and Advanced Formatting](#media-and-advanced-formatting)
6. [Best Practices](#best-practices)

## Import Formats

### Supported File Types
- **Text files** (CSV/TSV) - Most flexible for bulk import
- **APKG files** - Native Anki package format
- **Mnemosyne 2.0 .db files**
- **SuperMemo .xml files**

### CSV/TSV Import Features

#### Basic Format
```csv
Front,Back,Tags
"What is Python?","A programming language","programming python"
"Define recursion","A function calling itself","algorithms recursion"
```

#### Advanced Headers (Anki 2.1.54+)
Place at the top of your file:
```
#separator:comma
#html:true
#deck column:3
#notetype column:4
#tags column:5
#guid column:6
```

#### Key Features:
- **Deck routing**: Use `#deck column:2` to automatically create/organize into different decks
- **GUID support**: Include GUIDs for updating existing notes without duplicates
- **Note type mapping**: Different note types in same import file
- **HTML content**: Embed formatted content directly

### Field Handling
- Escape quotes by doubling: `"He said ""Hello"" to me"`
- Use HTML tags for formatting: `<b>Bold</b>`, `<i>Italic</i>`
- Include tags at line end, space-separated

## Card Types

### 1. Basic Cards
Simple front/back flashcards with customizable fields.

### 2. Cloze Cards
Fill-in-the-blank style with `{{c1::text}}` syntax:
```
The capital of France is {{c1::Paris}} and was founded in {{c2::3rd century BC}}.
```

### 3. Type-in Cards
Require typed answers with `{{type:FieldName}}` in template.

### Advanced Styling

#### Custom CSS Example
```css
.card {
    font-family: 'Open Sans', arial;
    font-size: 20px;
    text-align: center;
    color: #333;
    background-color: white;
}

.cloze {
    font-weight: bold;
    color: #09c;
}

.nightMode .cloze {
    color: #8df;
}

/* Code blocks */
pre {
    font-family: 'Fira Code', monospace;
    background-color: #f4f4f4;
    padding: 10px;
    border-radius: 5px;
}

/* Media controls */
.replay-button svg {
    width: 20px;
    height: 20px;
}
```

## Programmatic Generation with Python

### Using genanki Library

#### Installation
```bash
pip install genanki
```

#### Basic Example
```python
import genanki
import random

# Create a model (note type)
my_model = genanki.Model(
    random.randint(1000000, 9999999),
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'Extra'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}<br><br>{{Extra}}',
        },
    ],
    css='''
    .card {
        font-family: arial;
        font-size: 20px;
        text-align: center;
        color: black;
        background-color: white;
    }
    '''
)

# Create a deck
my_deck = genanki.Deck(
    random.randint(1000000, 9999999),
    'My Programming Deck'
)

# Add notes
my_note = genanki.Note(
    model=my_model,
    fields=['What is a variable?', 'A named storage location in memory', 'Variables can hold different data types']
)
my_deck.add_note(my_note)

# Generate package with media
my_package = genanki.Package(my_deck)
my_package.media_files = ['diagram1.png', 'audio1.mp3']
my_package.write_to_file('output.apkg')
```

#### Cloze Card Example
```python
cloze_model = genanki.Model(
    random.randint(1000000, 9999999),
    'Cloze Model',
    fields=[
        {'name': 'Text'},
        {'name': 'Extra'},
    ],
    templates=[
        {
            'name': 'Cloze Card',
            'qfmt': '{{cloze:Text}}',
            'afmt': '{{cloze:Text}}<br>{{Extra}}',
        },
    ],
    model_type=genanki.Model.CLOZE,
)

cloze_note = genanki.Note(
    model=cloze_model,
    fields=[
        'Python was created by {{c1::Guido van Rossum}} in {{c2::1991}}',
        'Additional info about Python history'
    ]
)
```

#### Reverse Cards (Two-way)
```python
reverse_model = genanki.Model(
    random.randint(1000000, 9999999),
    'Reverse Model',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
    ],
    templates=[
        {
            'name': 'Forward',
            'qfmt': '{{Front}}',
            'afmt': '{{Back}}',
        },
        {
            'name': 'Reverse',
            'qfmt': '{{Back}}',
            'afmt': '{{Front}}',
        },
    ]
)
```

### Bulk Generation from Data Sources

#### From CSV
```python
import csv
import genanki

def csv_to_anki(csv_file, output_file):
    deck = genanki.Deck(2059400110, 'CSV Import Deck')

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            note = genanki.Note(
                model=my_model,
                fields=[row['Question'], row['Answer'], row.get('Extra', '')]
            )
            deck.add_note(note)

    genanki.Package(deck).write_to_file(output_file)
```

#### From JSON/API
```python
import json
import requests

def api_to_anki(api_url, output_file):
    response = requests.get(api_url)
    data = response.json()

    deck = genanki.Deck(2059400110, 'API Import Deck')

    for item in data['flashcards']:
        note = genanki.Note(
            model=my_model,
            fields=[item['front'], item['back'], item.get('tags', '')]
        )
        deck.add_note(note)

    genanki.Package(deck).write_to_file(output_file)
```

## Bulk Generation Tools

### AI-Powered Tools

#### 1. AnkiGPT
- Generates comprehensive decks from topics
- Converts YouTube transcripts to flashcards
- Requires OpenAI API key

#### 2. ChatGPT Integration
**Prompt Template:**
```
Create 20 Anki flashcards about [TOPIC] in CSV format.
Format: "Question";"Answer";"Tags"
Include a mix of:
- Definition cards
- Concept explanations
- Application examples
- Common misconceptions
Make them suitable for spaced repetition learning.
```

#### 3. PDF to Anki Converters
- Extract key concepts from PDFs
- Generate questions automatically
- Support for diagrams via OCR

### Automation Scripts

#### Markdown to Anki
```python
import markdown2anki  # hypothetical library

def markdown_to_flashcards(md_file):
    """
    Convert markdown headers to questions,
    content to answers
    """
    with open(md_file, 'r') as f:
        content = f.read()

    # Parse headers as questions
    # Parse content under headers as answers
    # Handle code blocks, images, links

    return flashcards
```

## Media and Advanced Formatting

### Image Embedding
```html
<img src="myimage.jpg">
```

In fields:
```python
note = genanki.Note(
    model=my_model,
    fields=['What is this diagram?', '<img src="diagram.png">', '']
)
```

### Audio Files
```html
[sound:pronunciation.mp3]
```

### Video Support
```html
<video width="320" height="240" controls>
  <source src="myvideo.mp4" type="video/mp4">
</video>
```

### LaTeX/MathJax

#### Inline Math
```
When $a \ne 0$, there are two solutions to $(ax^2 + bx + c = 0)$
```

#### Block Math
```
$$\begin{aligned}
x &= \frac{-b \pm \sqrt{b^2-4ac}}{2a} \\
\end{aligned}$$
```

### SVG Diagrams
- Embed directly as `<img src="diagram.svg">`
- Smaller file size than raster images
- Scalable without quality loss

### Code Syntax Highlighting
```html
<pre><code class="language-python">
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
</code></pre>
```

## Best Practices

### Deck Organization
```
Main Subject/
├── Chapter 1/
│   ├── Concepts
│   ├── Examples
│   └── Problems
├── Chapter 2/
└── Review/
    └── Mixed Practice
```

### Card Creation Guidelines

1. **One concept per card** - Avoid combining multiple ideas
2. **Context independence** - Cards should make sense standalone
3. **Active recall** - Phrase as questions, not statements
4. **Concise answers** - Keep responses under 3 lines when possible
5. **Visual aids** - Use diagrams for complex concepts
6. **Mnemonics** - Include memory aids in Extra field

### Performance Optimization

1. **Media files**:
   - Compress images (JPEG for photos, PNG for diagrams)
   - Keep audio under 10 seconds
   - Use web-optimized formats

2. **Deck size**:
   - Limit to 5000 cards per deck for mobile performance
   - Split large subjects into sub-decks

3. **Import efficiency**:
   - Use GUID for updating existing cards
   - Batch imports rather than one-by-one

### Quality Control

```python
def validate_flashcard(front, back):
    """Basic validation for flashcard quality"""

    # Check for empty fields
    if not front.strip() or not back.strip():
        return False, "Empty fields"

    # Check for overly long content
    if len(front) > 200 or len(back) > 500:
        return False, "Content too long"

    # Check for question format
    question_words = ['what', 'why', 'how', 'when', 'where', 'which']
    if not any(word in front.lower() for word in question_words):
        if not front.endswith('?'):
            return False, "Not phrased as question"

    return True, "Valid"
```

## Advanced Techniques

### Dynamic Content Generation
```python
def generate_programming_cards(language, topics):
    """Generate cards based on programming language and topics"""

    templates = {
        'syntax': 'What is the syntax for {topic} in {language}?',
        'purpose': 'What is the purpose of {topic} in {language}?',
        'example': 'Provide an example of {topic} in {language}',
        'error': 'What error occurs when {topic} is misused in {language}?'
    }

    cards = []
    for topic in topics:
        for template_type, template in templates.items():
            question = template.format(topic=topic, language=language)
            # Generate answer using AI or database
            answer = generate_answer(question)
            cards.append((question, answer))

    return cards
```

### Spaced Repetition Optimization
- Start with 20-30 new cards per day
- Review cards before adding new ones
- Use tags for targeted study sessions
- Suspend cards that are too easy/hard

### Integration with Learning Resources
1. **Web scraping** for automatic card generation
2. **API integration** with educational platforms
3. **Browser extensions** for quick card creation
4. **Mobile apps** for on-the-go additions

## Conclusion

Creating prolific Anki decks requires:
1. Understanding import formats and card types
2. Leveraging programmatic generation for scale
3. Using AI tools for content creation
4. Implementing media and formatting effectively
5. Following best practices for maintainability

The key is balancing automation with quality control to create decks that are both comprehensive and effective for long-term retention.