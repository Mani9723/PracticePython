"""
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
import random

def play():
    printWinner()
    while playAgain()!="no":
        printWinner()
    print("Game Over!")

def getWinnerPlayer():
    playerOne = input("Player One: ")
    playerTwo = getChoices()
    print("Player Two: ", playerTwo)
    return compareInput(playerOne,playerTwo)

def getChoices():
    choices = ["rock","paper","scissors"]
    return choices[random.randint(0,2)]

def compareInput(playerOne,playerTwo):
    if(playerOne == "rock" and playerTwo == "scissors"):
        return "playerOne"
    elif (playerOne == "scissors" and playerTwo == "paper") or (playerOne == "rock" and playerTwo == "paper"): 
        return "playerOne"
    elif (playerOne == "paper" and playerTwo == "rock"):
        return "playerOne"
    elif(playerOne==playerTwo):
        return "Tie"

def printWinner():
    choice = getWinnerPlayer()
    if(choice == "playerOne"):
        print("Player One wins")
    else:
        if (choice=="Tie"):
            print("Tie")
        else:
            print("Player Two", "wins")

def playAgain():
    return input("Play Again: ")
    
play()