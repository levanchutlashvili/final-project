import random

ROCK = 0
PAPER = 1
SCISSORS = 2

User_Win_Count = 0
Computer_Win_Count = 0

def main():
    while True:
        try:
            userInput = user_input(input("Rock, Paper or Scissors?: "))
            computerInput = computer_input()
            match_turns_output(userInput, computerInput)
        except TypeError:
            pass
        else:
            result = match_result(userInput, computerInput)
            print(result)
            print(f"User vs Computer - {User_Win_Count}:{Computer_Win_Count}")
            question = input("Type x to keep playing. (To quit type any other character) ")
            if question.lower() == 'x':
                continue
            else:
                print("Game over!")
                break

def user_input(userInput):
    if userInput.lower() == "rock":
        return ROCK
    elif userInput.lower() == "paper":
        return PAPER
    elif userInput.lower() == "scissors":
        return SCISSORS
    else:
        print("Please write one of the three possible actions")

def computer_input():
    return random.choice(range(3))

def index_to_text(index):
    turns = ["Rock", "Paper", "Scissors"]
    return turns[index]

def match_turns_output(user_input, computer_input):
    print("User played:", index_to_text(user_input))
    print("Computer played:", index_to_text(computer_input))

def match_result(user_input, computer_input):
    winning = {
        ROCK: [SCISSORS],
        PAPER: [ROCK],
        SCISSORS: [PAPER],
    }
    user_win = winning[user_input]
    if user_input == computer_input:
        return "It's a draw"
    elif computer_input in user_win:
        user_win()
        return f"You Won!, {index_to_text(user_input)} Beats {index_to_text(computer_input)}"
    else:
        computer_win()
        return f"You Lost, {index_to_text(computer_input)} Beats {index_to_text(user_input)}"

def user_win():
    global User_Win_Count
    User_Win_Count += 1

def computer_win():
    global Computer_Win_Count
    Computer_Win_Count += 1

if __name__ == "__main__":
    main()
