"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""
def readString():
    return input("Enter a string: ")

def checkIfPalindrome():
    string = readString()
    return (string.lower() == string[::-1].lower())

def main():
    if(checkIfPalindrome()):
        print("Its Palindrome")
    else:
        print("Not a palindrome")

main()