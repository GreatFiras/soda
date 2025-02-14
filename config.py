import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

QUESTIONS_FILE = os.path.join(BASE_DIR, "data", "questions.json")
TRANSLATIONS_FILE = os.path.join(BASE_DIR, "data", "translations.json")
USER_TRANSLATIONS_FILE = os.path.join(BASE_DIR, "data", "user_translations.json")
ANSWERS_FILE = os.path.join(BASE_DIR, "data", "answers.json")
