#!/usr/bin/env python3
import json
import os
import subprocess

# Get all Chapter 1 lesson files
result = subprocess.run(
    ['find', 'learncpp-anki-deck/content/lessons', '-name', '1_*.json', '-type', 'f'],
    capture_output=True,
    text=True
)

lesson_files = sorted(result.stdout.strip().split('\n'))

# Print the files for processing
for f in lesson_files:
    print(f)
