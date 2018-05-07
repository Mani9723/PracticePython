"""  
For this exercise, we will keep track of when our friend’s birthdays are, 
and be able to find that information based on their name. 
Create a dictionary (in your file) of names and birthdays. 
When you run your program it should ask the user to enter a name, 
and return the birthday of that person back to them. 
The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
"""
namesDictionary = {}

def readFile(path):
    print("     We know Birthdays of: ")
    with open(path,'r') as file:
        for line in file:
            #print('\t', end = " ")
            list = line.rstrip().split('-')
            namesDictionary[list[0]] = list[1] +"\n"
        return namesDictionary
           # print("".join(list[0]))
   # askUser()

def askUser():
    getBirthday(str(input("Who's birthday would you like to know?\n-")))

def getBirthday(name):
    print("{}'s birthday is on -".format(name), end = " ")
    print(namesDictionary.get(name,"\nSORRY This person is not on the list"))

def main():
    readFile('C:/Users/Home/Desktop/grid.txt')
    askUser()

if __name__ == '__main__':
    main()