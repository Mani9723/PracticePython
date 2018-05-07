"""
        Problem 2:
Ask the user for a number.
Depending on whether the number is even or odd, 
print out an appropriate message to the user.

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. 
If not, print a different appropriate message.
"""

def readNumber():
    number = (int)(input("Enter a number: "))
    printParity(number)

def printParity(number):
    if (number%2==0):
        print(number, "is even")
        if (number%4==0):
            print(number, "is multiple of 4")
    else:
        print(number, "is odd")

def divisibilityCheck(first,second):
    if(first%second==0):
        print(first,"and ",second," are divisible")
    else:
        print("They are not divisible", end='\n')

def main():
    readNumber()
    divisibilityCheck((int)(input("Enter dividend: ")), (int)(input("Enter divisor: ")))

main()