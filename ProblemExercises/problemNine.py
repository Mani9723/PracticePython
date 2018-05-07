"""
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right. 

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random

def playGame():
    count = 0
    guess = 0
    secret = getSecretNumber()
    while(guess!=secret):
        count +=1
        guess = makeGuess()
        compareValues(guess,secret,count)
    
def compareValues(guess,secret,count):
    if(guess < secret):
        print ("Low")
    elif(guess > secret):
        print("High")
    else:
        print("Correct: ", secret, "\nIn ",count," tries")

def makeGuess():
    return (int)(input("Enter a number: "))

def getSecretNumber():
    return random.randint(1,100)

def main():
    answer = ""
    while(answer != "no"):
        playGame()
        answer = input("Play again: ")
main()