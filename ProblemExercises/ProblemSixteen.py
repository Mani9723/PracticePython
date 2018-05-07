"""
Password Generator
"""
import random
def createAsciiList():
    asciiList = [random.randint(33,127) for num in range(random.randint(15,20))]
    convertToCharacters(asciiList)

def convertToCharacters(asciiList):
    charList = []
    [charList.append(chr(number)) for number in asciiList]
    print(("".join(charList)))

def main():
    print("Your unique Password: ", end ="")
    createAsciiList()

main()