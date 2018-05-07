import json
import ProblemThirtyThree

exampleDict = ProblemThirtyThree.readFile('C:/Users/Home/Desktop/VSCodeProjects/PracticePython.org/textFile/grid.txt')
path = "C:/Users/Home/Desktop/VSCodeProjects/PracticePython.org/textFile/file.json"
def createFile():
    with open(path, 'w') as jsonFile:
        json.dump(exampleDict, jsonFile)

def addElemet():
    choice = "yes"
    while choice == "yes" or choice == "yes":
        choice = input("Would you like to add a person?\n")
        exampleDict[input("Name: ")] = input("Birthday: ")
        appendFile(path,exampleDict)

def appendFile(path, dictionary):
    with open(path,'w') as newFile:
        json.dump(dictionary,newFile)
     
def main():
    createFile()
    addElemet()

if __name__ == '__main__':
    main()

