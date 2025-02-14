from pydantic import BaseModel

class AnswerRequest(BaseModel):
    question_id: int
    answer: str

class TranslationRequest(BaseModel):
    text_id: int
    translation: str
