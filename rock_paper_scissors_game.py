import random

def get_user_choice():
    user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid input. Please enter Rock, Paper, or Scissors: ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return f"You win! {user_choice.capitalize()} beats {computer_choice}", 1
    else:
        return f"Computer wins! {computer_choice.capitalize()} beats {user_choice}", -1

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("You chose:", user_choice.capitalize())
        print("Computer chose:", computer_choice.capitalize())

        result, score = determine_winner(user_choice, computer_choice)
        print(result)

        user_score += score
        print(f"Your Score: {user_score}, Computer Score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
