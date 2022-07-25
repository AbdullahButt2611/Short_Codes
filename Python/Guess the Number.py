"""
You have to build a "Number Guessing Game," in which a winning number is set to some integer value.
The Program should take input from the user, and if the entered number is less than the winning number,
a message should display that the number is smaller and vice versa.

Instructions:
    1. You are free to use anything we've studied till now.
    2. The number of guesses should be limited, i.e (5 or 9).
    3. Print the number of guesses left.
    4. Print the number of guesses he took to win the game.
    5. “Game Over” message should display if the number of guesses becomes equal to 0.

You are advised to participate in solving this problem. This task helps you to become a good problem solver and helps
you accepting the challenge and acquiring new skills.
"""

numberToGuess = 24            #Change the Number for new Game
noOfRemainingGuesses = 9
userInputtedValue = int(input("Enter A Guess : "))

while True:

    if(noOfRemainingGuesses <= 1):
        print("\n\nWe are Sorry to inform but You Lost\nThe Value was",str(numberToGuess))
        print("Try Again Later!\nBest of Luck🤗")
        break

    if(userInputtedValue == numberToGuess):
        print("Huraay, You Won\n\n You were able to identify the number.\nCongratulations !!")
        break
    else:
        noOfRemainingGuesses -= 1
        print("The number of Remaining Guesses are", str(noOfRemainingGuesses))
        if(userInputtedValue > numberToGuess):
            print("Let's Try some Smaller Value")
        else:
            print("Let's try some Bigger value")

        userInputtedValue = int(input("Enter A Guess : "))