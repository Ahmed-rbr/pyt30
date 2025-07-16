import random

user_history = {
    'rock': 0, 'paper': 0, 'scissors': 0
}
choices = ['rock', 'paper', 'scissors']
play = True
turn = 0
scores = {'user': 0, 'ai': 0}


def determine_winner(user, ai, scores):
    if user == ai:
        return "draw"
    elif (user == "rock" and ai == "scissors") or \
         (user == "paper" and ai == "rock") or \
         (user == "scissors" and ai == "paper"):
        scores['user'] += 1

        return "win"
    else:
        scores['ai'] += 1
        return "lose"


while play:
    if turn > 2:
        most_picked = max(user_history, key=user_history.get)
        match most_picked:
            case 'rock':
                ai_choice = 'paper'
            case 'paper':
                ai_choice = 'scissors'
            case 'scissors':
                ai_choice = 'rock'
    else:
        ai_choice = random.choice(choices)
    user_choice = input('chose rock, paper, or scissors,').lower()
    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue
    turn += 1
    result = determine_winner(user_choice, ai_choice, scores)
    print(f"you: {user_choice}  ai: {ai_choice}")
    print(f"its draw.") if result == 'draw'else print(f"You {result}.")
    print(f"score:\nyou: {scores['user']} - ai: {scores['ai']}")
    ply = input('want another game (y/n)? ')
    if (ply == 'y'):
        play = True
    else:
        play = False
        print("\nFinal Scores:")
        print(f"You: {scores['user']} - AI: {scores['ai']}")
        if scores['user'] > scores['ai']:
            print("🏆 You won the game!")
        elif scores['user'] < scores['ai']:
            print("💻 AI won the game!")
        else:
            print("🤝 It's a tie overall!")
