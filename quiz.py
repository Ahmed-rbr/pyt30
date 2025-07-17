quizz = [
    {'qst': 'What is 4 + 4? ', 'response': 8},
    {'qst': 'What is 4 + 6? ', 'response': 10},
    {'qst': 'What is 5 + 10? ', 'response': 15},
]

play = True
print('Hello to the quiz!')

while play:
    score = 0

    for quiz in quizz:
        while True:
            user_input = input(quiz['qst'])

            if user_input.lower() == 'q' or user_input == '':
                print("Goodbye!")
                play = False
                break
            try:
                answer = int(user_input)
                if answer == quiz['response']:
                    score += 1
                break
            except ValueError:
                print('❌ Please enter a valid number.')

        if not play:
            break
    if play:
        print(f"🎉 Great! You got {score}/{len(quizz)} correct.")
        key = input("Press Enter to play again (or type 'q' to quit): ")
        play = key == ''
