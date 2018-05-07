"""
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order. 
"""

def readString():
    return input("Enter a sentence: ")

def reverseSentnce():
    strList = readString().split()
    return strList[::-1]

def printNewString():
    finalStr = " ".join(reverseSentnce())
    return finalStr
    
def main():
    print(printNewString())

main()