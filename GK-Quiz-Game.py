import random

questions = [
    {
        "question": "Which planet is known as the Red Planet?",
        "options": {
            "A": "Earth",
            "B": "Mars",
            "C": "Venus",
            "D": "Jupiter"
        },
        "answer": "B"
    },
    {
        "question": "Who is known as the Father of Computers?",
        "options": {
            "A": "Albert Einstein",
            "B": "Isaac Newton",
            "C": "Charles Babbage",
            "D": "Alan Turing"
        },
        "answer": "C"
    },
    {
        "question": "Which is the largest ocean in the world?",
        "options": {
            "A": "Indian Ocean",
            "B": "Atlantic Ocean",
            "C": "Arctic Ocean",
            "D": "Pacific Ocean"
        },
        "answer": "D"
    },
    {
        "question": "Which country hosted the FIFA World Cup 2022?",
        "options": {
            "A": "Brazil",
            "B": "Qatar",
            "C": "Germany",
            "D": "Russia"
        },
        "answer": "B"
    },
    {
        "question": "What is the national language of Japan?",
        "options": {
            "A": "Chinese",
            "B": "Korean",
            "C": "Japanese",
            "D": "Thai"
        },
        "answer": "C"
    }
]

random.shuffle(questions)

score = 0

print("\n===== GENERAL KNOWLEDGE QUIZ =====")

for index, q in enumerate(questions, start=1):

    print(f"\nQuestion {index}: {q['question']}")

    for key, value in q["options"].items():
        print(f"{key}. {value}")

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    while user_answer not in ["A", "B", "C", "D"]:
        user_answer = input("Invalid input. Please enter A, B, C, or D: ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        correct_option = q["options"][q["answer"]]
        print(f"Wrong! Correct answer: {q['answer']}. {correct_option}")

print("\n===== QUIZ COMPLETED =====")
print(f"Your Final Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Score Percentage: {percentage:.0f}%")

if percentage == 100:
    print("Outstanding Performance!")
elif percentage >= 60:
    print("Good Job!")
else:
    print("Keep Practicing and Improving!")