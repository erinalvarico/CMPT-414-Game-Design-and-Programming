# [Name] Erin Alvarico
# [Class] CMPT 414N - Game & Programming I
# [Lab 02] Number Guessing Game - 9/6/2020

import random

# Create a random number for Player to guess
secret_number = random.randrange(1, 129)

# Variables
guess = 0               # Player guess
guesses = []            # Player's previous guesses
terminate = ""          # Player quit input
stop = False            # Flag to stop game

# [GAME START]
# While loop to keep game playing
while guess != secret_number:        # Two conditions: secret num not found

    # Declare what number guess Player is at
    print("[ Guess #" + str(len(guesses)) + " ]: ")

    # Player's input stored in guess variable
    guess = int(input("Guess a number 1 to 128: "))     # Number between 1 - 128
    guesses.append(guess)                               # Add guess to list

    # Check if list length is less than 7
    if len(guesses) < 8:
        # [CONDITIONS] Provides hints to Player
        # If guess is lower than secret_number
        if guess < secret_number:
            print("Too low! Try guessing a higher number.")

        # If guess is high than secret_number
        elif guess > secret_number:
            print("Too high! Try guessing a lower number.")

        # If guess matches secret_number, Player wins the game!
        else:
            print("Congratulations, your guess is correct!")
            print("The secret number was: " + str(guess))

            pressEnter()        # To have a break in between text

            print("Would you like to see your previous guesses?")
            terminate = input("Press < q > to Skip, or < Any Key > to Continue")    # Player input for skip/no skip

            # Checks if terminate is equal to < q >, if so flip stop bool
            if terminate == "q":
                stop = True

            # Checks stop flag:
            # If true, prints previous guesses via guesses list
            if stop is not True:
                previousGuesses()   # Prints all previous guesses the Player has made

            # If false, skips printing previous guesses and ends game
            else:
                print("")
                print("You have chosen not to see your past guesses.")

    # List length is 8, Player loses the game
    else:
        print("")
        print("You have reached the maximum amount of guesses! (Max = 7)")
        print("")
        print("You have not guessed the right number.")
        print("That's too bad! Try again next time.")

        pressEnter()        # To have a break in between text

        print("Would you like to see your previous guesses?")
        terminate = input("Press < q > to Skip, or < Any Key > to Continue")    # Player input for skip/no skip

        # Checks if terminate is equal to < q >, if so flip stop bool
        if terminate == "q":
            stop = True

        # Checks stop flag:
        # If true, prints previous guesses via guesses list
        if stop is not True:
            previousGuesses()   # Prints all previous guesses the Player has made
            break

        # If false, skips printing previous guesses and ends game
        else:
            print("")
            print("You have chosen not to see your past guesses.")
            break

    # [FUNCTIONS]
    # Player presses < Enter > to proceed
    def pressEnter():
        print("")
        input("press < Enter > To Proceed")
        print("")

    # Prints out Player's previous guesses by guesses list
    def previousGuesses():
        print("")
        print("[ Previous Guesses ]")
        print(*guesses, end = " ")      # guesses are separated by spaces

print("")
print("Thank You For Playing!")
# [END OF GAME]