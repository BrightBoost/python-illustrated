import random

# Function to get the winner of the round
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
        (player_choice == 'scissors' and computer_choice == 'paper') or \
        (player_choice == 'paper' and computer_choice == 'rock'):
        return "Player wins!"
    else:
        return "Computer wins!"

# Function to play the game
def play_game():
    choices = ('rock', 'paper', 'scissors')
    player_score = 0
    computer_score = 0

    while player_score < 5 and computer_score < 5:
        # Get player's input and validate it
        while True:
            player_choice = input("Enter rock, paper, or scissors: ").lower()
            if player_choice in choices:
                break
            else:
                print("Invalid choice, please enter rock, paper, or scissors.")

        # Random computer choice
        computer_choice = random.choice(choices)

        # Display choices
        print(f"\nYou chose: {player_choice}")
        print(f"The computer chose: {computer_choice}")

        # Determine the winner of this round
        result = determine_winner(player_choice, computer_choice)
        print(result)

        # Update the score based on the result
        if result == "Player wins!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        # Display current score
        print(f"Score - Player: {player_score} | Computer: {computer_score}\n")

    # Announce the overall winner
    if player_score == 5:
        print("Congratulations! You win the game!")
    else:
        print("Sorry, the computer wins the game!")

    # Ask if the player wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

# Start the game
play_game()
