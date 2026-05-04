import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from teacher_bot import get_teacher_response
from tester_bot import generate_questions, evaluate_answer

load_dotenv()

app = FastAPI(
    title       = "Eternal Sunshine AI Service",
    description = "AI-powered teacher and tester bots for Pakistani students",
    version     = "1.0.0"
)

# ── request models ────────────────────────────────────────────────────────────
class ChatRequest(BaseModel):
    question:         str
    board:            str
    class_level:      str
    subject:          str
    language:         str  = "en"
    chat_history:     list = []
    existing_summary: str  = ""    
   

class QuizRequest(BaseModel):
    topic:         str
    board:         str
    class_level:   str
    subject:       str
    question_type: str = "mcq"   # mcq | short | long
    num_questions: int = 5

class EvalRequest(BaseModel):
    question:       str
    student_answer: str
    board:          str
    class_level:    str
    subject:        str

# ── response models ───────────────────────────────────────────────────────────
class ChatResponse(BaseModel):
    answer:           str
    updated_summary:  str  = ""    
    success:          bool = True

class QuizResponse(BaseModel):
    questions: str
    success:   bool = True

class EvalResponse(BaseModel):
    feedback: str
    success:  bool = True

# ── health check ──────────────────────────────────────────────────────────────
@app.get("/")
def root():
    return {"status": "Eternal Sunshine AI Service is running"}

@app.get("/health")
def health():
    return {"status": "ok", "service": "ai-service", "version": "1.0.0"}

# ── teacher bot endpoint ──────────────────────────────────────────────────────
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    try:
        result = get_teacher_response(        # now returns a dict
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

# ── tester bot — generate questions ──────────────────────────────────────────
@app.post("/quiz/generate", response_model=QuizResponse)
def quiz_generate(req: QuizRequest):
    try:
        questions = generate_questions(
            topic         = req.topic,
            board         = req.board,
            class_level   = req.class_level,
            subject       = req.subject,
            question_type = req.question_type,
            num_questions = req.num_questions
        )
        return QuizResponse(questions=questions)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ── tester bot — evaluate answer ──────────────────────────────────────────────
@app.post("/quiz/evaluate", response_model=EvalResponse)
def quiz_evaluate(req: EvalRequest):
    try:
        feedback = evaluate_answer(
            question       = req.question,
            student_answer = req.student_answer,
            board          = req.board,
            class_level    = req.class_level,
            subject        = req.subject
        )
        return EvalResponse(feedback=feedback)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))