#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import json
import time
import os
from typing import Dict, List, Tuple
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

print("Starting parallel lesson scraper...", flush=True)

class ParallelLessonScraper:
    def __init__(self, max_workers=5):
        self.max_workers = max_workers
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        self.lock = threading.Lock()
        self.processed_count = 0
        self.total_count = 0

    def fetch_lesson(self, lesson_info: Tuple[str, str, str, str]) -> Tuple[str, str, Dict]:
        """Fetch and parse a single lesson from LearnCPP"""
        chapter_dir, lesson_num, lesson_title, lesson_url = lesson_info

        try:
            response = self.session.get(lesson_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Get the main content area
            content = soup.find('div', class_='entry-content')
            if not content:
                return chapter_dir, lesson_num, None

            # Get lesson title
            title = soup.find('h1', class_='entry-title')
            title_text = title.get_text(strip=True) if title else ""

            # Extract sections with their content (keeping order)
            sections = []
            current_section = {'heading': None, 'content': []}

            for element in content.find_all(['h2', 'h3', 'p', 'pre', 'ul', 'ol', 'blockquote', 'div']):
                # Skip navigation elements
                if element.get('class') and any(c in str(element.get('class')) for c in ['lessonnav', 'prevnext']):
                    continue

                if element.name in ['h2', 'h3']:
                    # Save current section if it has content
                    if current_section['content']:
                        sections.append(current_section)

                    # Start new section
                    current_section = {
                        'heading': element.get_text(strip=True),
                        'content': []
                    }

                elif element.name == 'pre':
                    # Code block - keep inline with content
                    code_text = element.get_text()
                    current_section['content'].append({'code': code_text})

                elif element.name == 'p':
                    # Regular paragraph
                    text = element.get_text(strip=True)
                    if text and len(text) > 10:  # Filter out very short/empty paragraphs
                        current_section['content'].append({'text': text})

                elif element.name in ['ul', 'ol']:
                    # Lists
                    items = []
                    for li in element.find_all('li'):
                        item_text = li.get_text(strip=True)
                        if item_text:
                            items.append(item_text)
                    if items:
                        current_section['content'].append({'list': items})

                elif element.name == 'blockquote':
                    # Special notes/warnings
                    quote_text = element.get_text(strip=True)
                    if quote_text:
                        current_section['content'].append({'note': quote_text})

            # Don't forget the last section
            if current_section['content']:
                sections.append(current_section)

            # Extract quiz questions if present
            quiz_questions = self._extract_quiz(content)

            lesson_data = {
                'url': lesson_url,
                'title': title_text,
                'sections': sections,
                'quiz': quiz_questions
            }

            with self.lock:
                self.processed_count += 1
                print(f"  [{self.processed_count}/{self.total_count}] {lesson_num} - {lesson_title[:50]}... -> Saved", flush=True)

            return chapter_dir, lesson_num, lesson_data

        except Exception as e:
            with self.lock:
                self.processed_count += 1
                print(f"  [{self.processed_count}/{self.total_count}] {lesson_num} - Error: {e}", flush=True)
            return chapter_dir, lesson_num, None

    def _extract_quiz(self, content) -> List[Dict]:
        """Extract quiz questions from lesson content"""
        quiz_questions = []

        # Look for quiz section
        quiz_header = content.find(string=re.compile(r'Quiz\s*time', re.I))
        if not quiz_header:
            return quiz_questions

        # Get the parent element and find questions after it
        quiz_element = quiz_header.parent

        # Find all elements after quiz header
        current = quiz_element.find_next_sibling()
        current_question = None

        while current:
            text = current.get_text(strip=True)

            # Check if this is a question (usually starts with a number or "Question")
            if re.match(r'^(Question\s+)?\d+[).]', text) or re.match(r'^\d+[).]', text):
                if current_question:
                    quiz_questions.append(current_question)

                current_question = {
                    'question': text,
                    'code': None,
                    'answer_hint': None
                }

            elif current_question:
                # Check if this is code related to the question
                if current.name == 'pre':
                    current_question['code'] = current.get_text()

                # Check if this contains answer/hint keywords
                elif any(keyword in text.lower() for keyword in ['answer', 'solution', 'hint']):
                    current_question['answer_hint'] = text

            current = current.find_next_sibling()

        # Add last question
        if current_question:
            quiz_questions.append(current_question)

        return quiz_questions

    def scrape_all_lessons(self, index_path: str, output_dir: str):
        """Scrape all lessons from the index using parallel threads"""
        print(f"Loading index from {index_path}...", flush=True)

        # Load index
        with open(index_path, 'r') as f:
            chapters = json.load(f)

        os.makedirs(output_dir, exist_ok=True)

        # Prepare all lesson tasks
        lesson_tasks = []
        for chapter_name in sorted(chapters.keys()):
            chapter_dir = os.path.join(output_dir, chapter_name.replace(' ', '_'))
            os.makedirs(chapter_dir, exist_ok=True)

            for lesson in chapters[chapter_name]:
                lesson_num = lesson['number']
                lesson_title = lesson['title']
                lesson_url = lesson['url']

                # Check if already scraped
                output_file = os.path.join(chapter_dir, f"{lesson_num.replace('.', '_')}.json")
                if not os.path.exists(output_file):
                    lesson_tasks.append((chapter_dir, lesson_num, lesson_title, lesson_url))

        self.total_count = len(lesson_tasks)
        print(f"Found {len(chapters)} chapters with {self.total_count} lessons to scrape", flush=True)
        print(f"Using {self.max_workers} parallel threads", flush=True)

        if not lesson_tasks:
            print("All lessons already scraped!")
            return

        # Process lessons in parallel
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all tasks
            futures = {executor.submit(self.fetch_lesson, task): task for task in lesson_tasks}

            # Process completed tasks
            for future in as_completed(futures):
                chapter_dir, lesson_num, lesson_data = future.result()

                if lesson_data:
                    # Save to file
                    output_file = os.path.join(chapter_dir, f"{lesson_num.replace('.', '_')}.json")
                    with open(output_file, 'w') as f:
                        json.dump(lesson_data, f, indent=2)

                # Small delay to be respectful (reduced because we're parallel)
                time.sleep(0.2)

        print(f"\nDone! Processed {self.processed_count} lessons")

if __name__ == "__main__":
    # You can adjust max_workers for more or fewer parallel threads
    # Be respectful to the server - don't use too many!
    scraper = ParallelLessonScraper(max_workers=5)
    scraper.scrape_all_lessons(
        'learncpp-anki-deck/content/index.json',
        'learncpp-anki-deck/content/lessons'
    )