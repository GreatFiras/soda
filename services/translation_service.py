import random
from utils.json_handler import load_json, save_json
from config import TRANSLATIONS_FILE, USER_TRANSLATIONS_FILE
from models.schemas import TranslationRequest
from state import used_translation_questions  # Tracks used translation texts

translation_limit = 2  # Max number of unique translations before returning "Done"

def get_balanced_text():
    """Returns a unique translation text just like the question service."""
    texts = load_json(TRANSLATIONS_FILE)

    # Stop if limit is reached
    if len(used_translation_questions) >= translation_limit:
        return {"message": "Done"}

    # Filter available texts
    available_texts = [t for t in texts if t["id"] not in used_translation_questions]

    if not available_texts:
        return {"message": "Done"}

    # Select a random text
    text = random.choice(available_texts)
    used_translation_questions.add(text["id"])

    return {"text_id": text["id"], "text": text["text"], "sentiment": text["sentiment"]}

def reset_translation_questions():
    """Resets used translation texts without deleting stored translations."""
    used_translation_questions.clear()
    return {"message": "Translation questions have been reset successfully."}


def submit_translation(request: TranslationRequest):
    """Stores user-submitted translations in a separate JSON file."""
    texts = load_json(TRANSLATIONS_FILE)

    text_obj = next((t for t in texts if t["id"] == request.text_id), None)

    if not text_obj:
        return {"error": "Invalid text ID"}

    submitted_translations = load_json(USER_TRANSLATIONS_FILE)
    submitted_translations.append({
        "text_id": request.text_id,
        "original_text": text_obj["text"],
        "sentiment": text_obj["sentiment"],
        "translated_text": request.translation
    })

    save_json(USER_TRANSLATIONS_FILE, submitted_translations)

    return {"status": "success", "message": "Translation saved!", "data": submitted_translations}

def get_all_translations():
    """Fetch all submitted translations from JSON."""
    return {"status": "success", "translations": load_json(USER_TRANSLATIONS_FILE)}
