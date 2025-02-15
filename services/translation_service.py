import random
from data.translations_data import TRANSLATIONS  # ✅ Import static translations
from utils.json_handler import load_json, save_json
from config import USER_TRANSLATIONS_FILE
from models.schemas import TranslationRequest
from state import used_translation_questions

translation_limit = 6  # Limit for available translations

def get_balanced_text():
    """Fetch a translation text from the Python file."""
    if len(used_translation_questions) >= translation_limit:
        return {"message": "Done"}

    available_texts = [t for t in TRANSLATIONS if t["id"] not in used_translation_questions]

    if not available_texts:
        return {"message": "Done"}

    text = random.choice(available_texts)
    used_translation_questions.add(text["id"])

    return {"text_id": text["id"], "text": text["text"], "sentiment": text["sentiment"]}

def submit_translation(request: TranslationRequest):
    """Stores user-submitted translations in JSON."""
    submitted_translations = load_json(USER_TRANSLATIONS_FILE)
    submitted_translations.append({"text_id": request.text_id, "translated_text": request.translation})
    save_json(USER_TRANSLATIONS_FILE, submitted_translations)

    return {"status": "success", "message": "Translation recorded!"}

def reset_translation_questions():
    """Resets used translation questions."""
    used_translation_questions.clear()
    return {"message": "Translation questions have been reset."}
