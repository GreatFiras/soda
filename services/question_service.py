import random
from fastapi import Request
from Data.questions_data import QUESTIONS
from utils.json_handler import load_json, save_json
from config import ANSWERS_FILE
from models.schemas import AnswerRequest

USER_PROGRESS = {}  # ✅ Tracks progress for each session

question_limit = 6  # Limit for each user

def get_random_question(session_id: str):
    """Returns a unique random question for the session."""
    if session_id in USER_PROGRESS and len(USER_PROGRESS[session_id]) >= question_limit:
        return {"question": "Done"}

    available_questions = [q for q in QUESTIONS if q["id"] not in USER_PROGRESS.get(session_id, set())]

    if not available_questions:
        return {"question": "Done"}

    question = random.choice(available_questions)
    return {"question_id": question["id"], "question": question["question"]}

def submit_answer(session_id: str, request: AnswerRequest):
    """Stores a user's answer and tracks progress per session."""
    submitted_answers = load_json(ANSWERS_FILE)

    if session_id not in USER_PROGRESS:
        USER_PROGRESS[session_id] = set()

    if len(USER_PROGRESS[session_id]) >= question_limit:
        return {"message": "You have reached the question limit!"}

    USER_PROGRESS[session_id].add(request.question_id)
    submitted_answers.append({"session_id": session_id, "question_id": request.question_id, "answer": request.answer})
    save_json(ANSWERS_FILE, submitted_answers)

    return {"status": "success", "message": "Answer recorded!", "remaining": question_limit - len(USER_PROGRESS[session_id])}

def reset_user_progress(session_id: str):
    """Resets the progress for a specific user session."""
    USER_PROGRESS.pop(session_id, None)
    return {"message": "Your progress has been reset."}
