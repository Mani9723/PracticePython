"""
Guessing game two

This time, we’re going to do exactly the opposite. 
You, the user, will have in your head a number between 0 and 100. 
The program will guess a number, and you, the user, 
will say whether it is too high, too low, or your number.

At the end of this exchange, your program should 
print out how many guesses it took to get your number.
"""
#from ProblemTwenty import binarySearch
#from problemNine import getSecretNumber
import random

def computerGuess():
    computerGuess, secretNumber, count= random.randint(1,100), setSecretNumber(), 0
    while(secretNumber != computerGuess):
        count += 1
        if(secretNumber>computerGuess):
            print("Too Low:\t", computerGuess)
            computerGuess = random.randint(computerGuess,1)
        else:
            print("Too High:\t", computerGuess)
            computerGuess = random.randint(1,computerGuess)
    print("It took ", count, " tries.\nSecret: ", secretNumber, "Guess: ", computerGuess)

def setSecretNumber():
    return random.randint(1,100)
    
def main():
    computerGuess()

if __name__ == '__main__':
    main()