import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the absolute path of the project root
DATA_DIR = os.path.join(BASE_DIR, "data")  # Define the data folder

# JSON files for storing user responses
ANSWERS_FILE = os.path.join(DATA_DIR, "answers.json")
USER_TRANSLATIONS_FILE = os.path.join(DATA_DIR, "user_translations.json")
