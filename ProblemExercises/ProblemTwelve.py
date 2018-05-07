"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
"""
def printFirstAndLast(list):
    print(list[0]," ",list[len(list)-1])
def main():
    a = [5, 10, 15, 20, 25]
    printFirstAndLast(a)

main()