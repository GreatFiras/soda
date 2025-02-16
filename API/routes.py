from fastapi import APIRouter , Request
from services.question_service import get_random_question, submit_answer , reset_user_progress
from services.translation_service import get_balanced_text, submit_translation, reset_translation_questions
from models.schemas import AnswerRequest, TranslationRequest
from utils.json_handler import load_json
from config import ANSWERS_FILE , USER_TRANSLATIONS_FILE


router = APIRouter()

@router.get("/get-question")
async def get_question(request: Request):
    """Returns a unique random question for the session."""
    session_id = request.headers.get("session_id")

    if not session_id:
        return {"error": "Missing session_id"}

    return get_random_question(session_id)  # ✅ Use the correct function

@router.post("/submit-answer")
async def answer_submission(request: Request, answer: AnswerRequest):
    session_id = request.headers.get("session_id")
    if not session_id:
        return {"error": "Missing session_id"}
    return submit_answer(session_id, answer)

@router.get("/reset-user-progress")
async def reset_user(request: Request):
    session_id = request.headers.get("session_id")
    if not session_id:
        return {"error": "Missing session_id"}
    return reset_user_progress(session_id)

from fastapi import APIRouter, Request
from services.question_service import reset_user_progress

router = APIRouter()

@router.get("/reset-questions")
async def reset_questions(request: Request):
    """Resets user progress for answering questions."""
    session_id = request.headers.get("session_id")

    if not session_id:
        return {"error": "Missing session_id"}

    return reset_user_progress(session_id)

# Translation Routes
@router.get("/get-balanced-sentiments")
async def fetch_translation_text():
    return get_balanced_text()

@router.post("/submit-translation")
async def translation_submission(request: TranslationRequest):
    return submit_translation(request)

@router.get("/reset-translation-questions")
async def reset_translation_questions_endpoint():
    return reset_translation_questions()

@router.get("/get-translations")
async def get_translations():
    """Returns all submitted translations from JSON file."""
    translations = load_json(USER_TRANSLATIONS_FILE)
    return {"status": "success", "translations": translations}