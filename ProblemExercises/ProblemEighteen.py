""" 
Cows and bull
 Random 4-digit number
 if user guess a correct digit in its correct place = 1 cow
 if user guess a correct digit but in the wrong place = 1 bull
"""
import random
def inputGuess():
    guess(str(random.randint(1000, 9999)),(input("Enter a guess: ")))

def guess(secretNumber,guessNumber):
    while(secretNumber != guessNumber):
        cows, bulls = 0,0
        for index in range(len(secretNumber)):
            if(secretNumber[index] == guessNumber[index]):
                cows += 1
            elif(guessNumber[index] in secretNumber):
                bulls += 1
        print("cows: ", cows, " bulls: ", bulls)
        guessNumber = str(input("Enter a guess or exit: "))
        if(guessNumber == "exit"):
            exit()
            break
    print("Final values: ", secretNumber, guessNumber)

def exit():
    print("Game Over")
def main():
    inputGuess()

if __name__ == '__main__':
    main()
