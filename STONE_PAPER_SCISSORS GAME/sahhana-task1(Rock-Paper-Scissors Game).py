# ----------------------------------------
# Rock Paper Scissors Game
# Internship Project
# ----------------------------------------

import random

# List of valid choices
choices = ["rock", "paper", "scissors"]

# Score variables
user_score = 0
computer_score = 0

print("===================================")
print("     ROCK PAPER SCISSORS GAME")
print("===================================")

# Repeat the game until the user chooses to stop
while True:

    # Get user's choice
    user_choice = input("\nEnter Rock, Paper, or Scissors: ").lower()

    # Check if the input is valid
    if user_choice not in choices:
        print("Invalid choice! Please enter Rock, Paper, or Scissors.")
        continue

    # Computer selects a random choice
    computer_choice = random.choice(choices)

    # Display both choices
    print("\nYour Choice      :", user_choice.capitalize())
    print("Computer Choice  :", computer_choice.capitalize())

    # Determine the winner
    if user_choice == computer_choice:
        print("\nResult : It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("\nResult : Congratulations! You Win!")
        user_score += 1

    else:
        print("\nResult : Computer Wins!")
        computer_score += 1

    # Display current scores
    print("\nCurrent Score")
    print("User      :", user_score)
    print("Computer  :", computer_score)

    # Ask the user if they want to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

# Display final scores
print("\n===================================")
print("          GAME OVER")
print("===================================")

print("Final Score")
print("User      :", user_score)
print("Computer  :", computer_score)

# Display overall winner
if user_score > computer_score:
    print("\nOverall Winner : You! 🎉")

elif computer_score > user_score:
    print("\nOverall Winner : Computer!")

else:
    print("\nOverall Result : It's a Tie!")

print("\nThank you for playing!")