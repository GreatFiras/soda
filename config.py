import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Ensure absolute path
DATA_DIR = os.path.join(BASE_DIR, "data")  # Store all JSON files here

QUESTIONS_FILE = os.path.join(DATA_DIR, "questions.json")
TRANSLATIONS_FILE = os.path.join(DATA_DIR, "translations.json")
USER_TRANSLATIONS_FILE = os.path.join(DATA_DIR, "user_translations.json")
ANSWERS_FILE = os.path.join(DATA_DIR, "answers.json")
