import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Ensure `data/` directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Define JSON file paths
ANSWERS_FILE = os.path.join(DATA_DIR, "answers.json")
USER_TRANSLATIONS_FILE = os.path.join(DATA_DIR, "user_translations.json")
