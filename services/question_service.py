import random
from utils.json_handler import load_json, save_json
from config import QUESTIONS_FILE, ANSWERS_FILE
from models.schemas import AnswerRequest
from state import used_questions

question_limit = 2  # Set same limit as original script

def get_random_question():
    """Returns a unique random question from JSON."""
    questions = load_json(QUESTIONS_FILE)

    if len(used_questions) >= question_limit:
        return {"question": "Done"}

    available_questions = [q for q in questions if q["id"] not in used_questions]

    if not available_questions:
        return {"question": "Done"}

    question = random.choice(available_questions)
    used_questions.add(question["id"])

    return {"question_id": question["id"], "question": question["question"]}

def submit_answer(request: AnswerRequest):
    """Stores a user's answer in JSON and ensures question exists."""
    questions = load_json(QUESTIONS_FILE)

    question_obj = next((q for q in questions if q["id"] == request.question_id), None)

    if not question_obj:
        return {"error": "Invalid question ID"}

    submitted_answers = load_json(ANSWERS_FILE)
    submitted_answers.append({
        "question_id": request.question_id,
        "question": question_obj["question"],
        "answer": request.answer
    })
    
    save_json(ANSWERS_FILE, submitted_answers)

    return {"status": "success", "message": "Answer saved!", "data": submitted_answers}

def get_all_answers():
    """Fetch all answers from JSON."""
    return {"status": "success", "answers": load_json(ANSWERS_FILE)}

def reset_questions():
    """Resets the used questions without clearing saved answers."""
    used_questions.clear()
    return {"message": "Questions have been reset successfully."}
