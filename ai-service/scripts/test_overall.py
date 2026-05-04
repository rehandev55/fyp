import requests

payload = {
    "board":         "federal",
    "class_level":   "class_11",
    "subject":       "biology",
    "question_type": "mcq",
    "results": [
        {
            "question":       "What is cell theory?",
            "student_answer": "All living things are made of cells",
            "score":          7.0,
            "feedback":       "Correct but missing two other tenets"
        },
        {
            "question":       "Who proposed cell theory?",
            "student_answer": "Robert Hooke",
            "score":          3.0,
            "feedback":       "Incorrect. Schleiden and Schwann proposed it"
        },
        {
            "question":       "What is the basic unit of life?",
            "student_answer": "Cell",
            "score":          10.0,
            "feedback":       "Perfect answer"
        }
    ]
}

response = requests.post("http://localhost:8001/quiz/overall", json=payload)
result = response.json()

print("Total Score:     ", result["total_score"])
print("Percentage:      ", result["percentage"])
print("Grade:           ", result["grade"])
print("Strong Areas:    ", result["strong_areas"])
print("Weak Areas:      ", result["weak_areas"])
print("Overall Feedback:", result["overall_feedback"])
print("Study Tip:       ", result["study_tip"])