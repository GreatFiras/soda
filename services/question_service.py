import random
from data.questions_data import QUESTIONS  # ✅ Import static questions
from utils.json_handler import load_json, save_json
from config import ANSWERS_FILE
from models.schemas import AnswerRequest
from state import used_questions

question_limit = 6  # Limit for available questions

def get_random_question():
    """Fetches a unique random question from the Python file."""
    if len(used_questions) >= question_limit:
        return {"question": "Done"}

    available_questions = [q for q in QUESTIONS if q["id"] not in used_questions]

    if not available_questions:
        return {"question": "Done"}

    question = random.choice(available_questions)
    used_questions.add(question["id"])

    return {"question_id": question["id"], "question": question["question"]}

def submit_answer(request: AnswerRequest):
    """Stores user-submitted answers in JSON."""
    submitted_answers = load_json(ANSWERS_FILE)
    submitted_answers.append({"question_id": request.question_id, "answer": request.answer})
    save_json(ANSWERS_FILE, submitted_answers)

    return {"status": "success", "message": "Answer recorded!"}

def reset_questions():
    """Resets used questions."""
    used_questions.clear()
    return {"message": "Questions have been reset."}
