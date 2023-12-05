import random


questions = {
    "What is the capital of France?": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
    "Which planet is known as the Red Planet?": ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"],
    "Who painted the Mona Lisa?": ["A. Pablo Picasso", "B. Leonardo da Vinci", "C. Vincent van Gogh", "D. Michelangelo"],

}


answers = {
    "What is the capital of France?": "A",
    "Which planet is known as the Red Planet?": "A",
    "Who painted the Mona Lisa?": "B",

}

def kbc_game():
    score = 0
    question_list = list(questions.keys())

    
    random.shuffle(question_list)

    for question in question_list:
        print("\n", question)
        for option in questions[question]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D or Q to quit): ").upper()

        if user_answer == 'Q':
            break

        if user_answer == answers[question]:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer!")
            print("Correct answer was:", answers[question])

    print("\nGame Over!")
    print("Total score:", score)


kbc_game()