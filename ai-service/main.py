import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from teacher_bot import get_teacher_response
from tester_bot import generate_questions, evaluate_answer
from overall_evaluator import get_overall_feedback

load_dotenv()

app = FastAPI(
    title       = "Eternal Sunshine AI Service",
    description = "AI-powered teacher and tester bots for Pakistani students",
    version     = "2.0.0"
)

# ── input length constants ────────────────────────────────────────────────────
MAX_QUESTION_LEN  = 1000
MAX_ANSWER_LEN    = 3000
MAX_HISTORY_ITEMS = 20

# ── request models with validation ───────────────────────────────────────────
class ChatRequest(BaseModel):
    question:         str  = Field(..., max_length=MAX_QUESTION_LEN)
    board:            str
    class_level:      str
    subject:          str
    language:         str  = "en"
    chat_history:     list = Field(default_factory=list, max_length=MAX_HISTORY_ITEMS)
    existing_summary: str  = Field(default="", max_length=2000)

class QuizRequest(BaseModel):
    topic:         str  = Field(..., max_length=500)
    board:         str
    class_level:   str
    subject:       str
    question_type: str  = "mcq"
    num_questions: int  = Field(default=5, ge=1, le=20)

class EvalRequest(BaseModel):
    question:       str = Field(..., max_length=MAX_QUESTION_LEN)
    student_answer: str = Field(..., max_length=MAX_ANSWER_LEN)
    board:          str
    class_level:    str
    subject:        str
    question_type: str

class QuestionResult(BaseModel):
    question:       str   = Field(..., max_length=MAX_QUESTION_LEN)
    student_answer: str   = Field(..., max_length=MAX_ANSWER_LEN)
    score:          float = Field(..., ge=0, le=10)
    feedback:       str   = Field(default="", max_length=1000)

class OverallFeedbackRequest(BaseModel):
    board:         str
    class_level:   str
    subject:       str
    question_type: str
    results:       list[QuestionResult] = Field(..., max_length=50)

# ── response models ───────────────────────────────────────────────────────────
class ChatResponse(BaseModel):
    answer:          str
    updated_summary: str  = ""
    success:         bool = True

class QuizResponse(BaseModel):
    questions: str
    success:   bool = True

class EvalResponse(BaseModel):
    feedback: str
    score: int
    success:  bool = True

class OverallFeedbackResponse(BaseModel):
    total_score:      str
    percentage:       float
    grade:            str
    strong_areas:     list[str]
    weak_areas:       list[str]
    overall_feedback: str
    study_tip:        str
    success:          bool = True

# ── health ────────────────────────────────────────────────────────────────────
@app.get("/")
def root():
    return {"status": "Eternal Sunshine AI Service is running", "version": "2.0.0"}

@app.get("/health")
def health():
    return {"status": "ok"}

# ── endpoints ─────────────────────────────────────────────────────────────────
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    try:
        result = get_teacher_response(
            question         = req.question,
            board            = req.board,
            class_level      = req.class_level,
            subject          = req.subject,
            language         = req.language,
            chat_history     = req.chat_history,
            existing_summary = req.existing_summary,
        )
        return ChatResponse(
            answer          = result["answer"],
            updated_summary = result["updated_summary"],
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/quiz/generate", response_model=QuizResponse)
def quiz_generate(req: QuizRequest):
    try:
        questions = generate_questions(
            topic         = req.topic,
            board         = req.board,
            class_level   = req.class_level,
            subject       = req.subject,
            question_type = req.question_type,
            num_questions = req.num_questions,
        )
        return QuizResponse(questions=questions)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/quiz/evaluate", response_model=EvalResponse)
def quiz_evaluate(req: EvalRequest):
    try:
        result = evaluate_answer(
            question       = req.question,
            student_answer = req.student_answer,
            board          = req.board,
            class_level    = req.class_level,
            subject        = req.subject,
            question_type = req.question_type,
        )
        return EvalResponse(
            feedback = result["feedback"],
            score    = result["score"],
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/quiz/overall", response_model=OverallFeedbackResponse)
def quiz_overall(req: OverallFeedbackRequest):
    try:
        results = [
            {
                "question":       r.question,
                "student_answer": r.student_answer,
                "score":          r.score,
                "feedback":       r.feedback,
            }
            for r in req.results
        ]
        feedback = get_overall_feedback(
            board         = req.board,
            class_level   = req.class_level,
            subject       = req.subject,
            question_type = req.question_type,
            results       = results,
        )
        return OverallFeedbackResponse(**feedback)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))