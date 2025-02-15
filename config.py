import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get absolute path of project root
DATA_DIR = os.path.join(BASE_DIR, "data")  # Set the data folder

# Ensure FastAPI loads JSON files from the correct location
QUESTIONS_FILE = os.path.join(DATA_DIR, "questions.json")
TRANSLATIONS_FILE = os.path.join(DATA_DIR, "translations.json")
USER_TRANSLATIONS_FILE = os.path.join(DATA_DIR, "user_translations.json")
ANSWERS_FILE = os.path.join(DATA_DIR, "answers.json")
