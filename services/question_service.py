import random
from utils.json_handler import load_json, save_json
from config import QUESTIONS_FILE, ANSWERS_FILE
from models.schemas import AnswerRequest
from state import used_questions

question_limit = 6  # Limit on questions before returning "Done"

def get_random_question():
    """Fetches a unique random question."""
    questions = load_json(QUESTIONS_FILE, "QUESTIONS_DATA")  # ✅ Load from Render ENV if available

    if not questions:
        return {"question": "No questions available."}

    if len(used_questions) >= question_limit:
        return {"question": "Done"}

    available_questions = [q for q in questions if q["id"] not in used_questions]

    if not available_questions:
        return {"question": "Done"}

    question = random.choice(available_questions)
    used_questions.add(question["id"])

    return {"question_id": question["id"], "question": question["question"]}

def submit_answer(request: AnswerRequest):
    """Stores user-submitted answers."""
    questions = load_json(QUESTIONS_FILE, "QUESTIONS_DATA")

    if not any(q["id"] == request.question_id for q in questions):
        return {"error": "Invalid question ID"}

    submitted_answers = load_json(ANSWERS_FILE)
    submitted_answers.append({"question_id": request.question_id, "answer": request.answer})
    save_json(ANSWERS_FILE, submitted_answers)

    return {"status": "success", "message": "Answer saved!"}

def reset_questions():
    """Resets used questions."""
    used_questions.clear()
    return {"message": "Questions have been reset."}
