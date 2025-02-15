import random
from utils.json_handler import load_json, save_json
from config import TRANSLATIONS_FILE, USER_TRANSLATIONS_FILE , ANSWERS_FILE
from models.schemas import TranslationRequest
from state import used_translation_questions

translation_limit = 6  # Limit for available translations

def get_all_answers():
    """Fetch all answers from the JSON file."""
    return {"status": "success", "answers": load_json(ANSWERS_FILE)}


def get_balanced_text():
    """Fetch a translation text from JSON file."""
    texts = load_json(TRANSLATIONS_FILE)  # ✅ Always loads from file

    if not texts:
        return {"message": "No translations available."}

    if len(used_translation_questions) >= translation_limit:
        return {"message": "Done"}

    available_texts = [t for t in texts if t["id"] not in used_translation_questions]

    if not available_texts:
        return {"message": "Done"}

    text = random.choice(available_texts)
    used_translation_questions.add(text["id"])

    return {"text_id": text["id"], "text": text["text"], "sentiment": text["sentiment"]}

def reset_translation_questions():
    """Resets used translation questions without clearing saved translations."""
    used_translation_questions.clear()
    return {"message": "Translation questions have been reset successfully."}
