from fastapi import APIRouter
from services.question_service import get_random_question, submit_answer, reset_questions
from services.translation_service import get_balanced_text, submit_translation, reset_translation_questions
from models.schemas import AnswerRequest, TranslationRequest

router = APIRouter()

# Question Routes
@router.get("/get-question")
async def get_question():
    return get_random_question()

@router.post("/submit-answer")
async def answer_submission(request: AnswerRequest):
    return submit_answer(request)

@router.get("/reset-questions")
async def reset_questions_endpoint():
    return reset_questions()

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
