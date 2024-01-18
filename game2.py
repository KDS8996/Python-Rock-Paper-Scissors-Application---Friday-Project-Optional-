import random

def get_user_choice():
    return input("Enter your choice (rock, paper, scissors) or type 'I quit' to end: ").lower()

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    return "Computer wins!"

while True:
    user_choice = get_user_choice()

    if user_choice == "i quit":
        print("Thank you for playing. Goodbye!")
        break

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter 'rock', 'paper', 'scissors', or 'I quit'.")
        continue

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
