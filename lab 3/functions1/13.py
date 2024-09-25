import random

def guess_the_number():
    # Ask for the player's name
    print("Hello! What is your name?")
    name = input()

    # Greet the player and explain the game
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    # Generate a random number between 1 and 20
    number = random.randint(1, 20)

    # Track the number of guesses taken
    guesses_taken = 0

    # Game loop for guessing
    while True:
        # Prompt the player to guess a number
        print("Take a guess.")
        guess = int(input())  # Convert input to an integer
        guesses_taken += 1

        # Give feedback based on the guess
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            # The player guessed the correct number
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break  # End the game

# Start the game
guess_the_number()
