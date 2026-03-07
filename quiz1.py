# List of quiz questions
questions = [
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "correct_answer": "B"
    },
    {
        "question": "What does RAM stand for?",
        "options": [
            "A. Random Access Memory",
            "B. Read Access Memory",
            "C. Run Access Memory",
            "D. Ready Access Memory"
        ],
        "correct_answer": "A"
    },
    {
        "question": "Which language is mainly used for web pages?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
        "correct_answer": "C"
    }
]

score = 0
total_questions = len(questions)

# Loop through the quiz
for item in questions:
    print("\n" + item["question"])
    
    for option in item["options"]:
        print(option)

    user_answer = input("Choose A, B, C or D: ").upper()

    if user_answer == item["correct_answer"]:
        print("Correct answer!")
        score += 1
    else:
        print("Incorrect answer.")

# Function to calculate percentage
def show_result(score, total):
    percentage = (score / total) * 100
    print("\nFinal Score:", score, "/", total)
    print("Percentage:", percentage, "%")

    if percentage >= 60:
        print("You Passed the Quiz!")
    else:
        print("You Failed the Quiz.")

# Call the function
show_result(score, total_questions)