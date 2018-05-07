"""
    Practice Python Problem 1:
    - Read name and age
    - Print the year they will turn 100
"""

def displayInformation():
    name = input("Enter you name:")
    age = calcAgeHundred((int)(input("Enter your age:")))
    printInfo(name,age)

def calcAgeHundred(age):
    return (100-age) + 2018

def printInfo(name,age):
    print("Hi",name,end='\n')
    print("You will be a centurian in year ",age,end='\n')

displayInformation()
