import random

def play_game():
    print("Welcome to Rock-Paper-Scissors!\n")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'quit' to end the game.\n")

    user_score, computer_score = 0, 0

    while True:
        user_choice = input("Your choice: ").lower()
        if user_choice == "quit":
            print(f"\nFinal Scores - You: {user_score}, Computer: {computer_score}")
            print("Thanks for playing!")
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Try again.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print(f"Scores - You: {user_score}, Computer: {computer_score}\n")

if __name__ == "__main__":
    play_game()
