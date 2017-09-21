# guessing game written in Python
# Author: Dillon Ward (Dillonward2017@gmail.com)
# Date: 20/09/2017
# import 'randint' from the 'random' module
from random import randint

# generate the number the user has to guess
answer = randint(0, 10)
guesses = 0 # number of guesses
temp = 0 

print("Guess a number between 0 and 10!", answer)


while True:
    userInput = input("Your guess:")
    guess = int(userInput) # converts userInput into an int 'guess'

    if guess != temp:
        temp = guess 
        guesses += 1
        # temporarily store the previously entered number
        # increment the number of guesses

    if guess > answer:
        print("Too High!")

    
    elif guess < answer:
        print("Too Low!")

    else:
        print("Correct!")
        print("Number of guesses: ", guesses)
        break # exit the while loop