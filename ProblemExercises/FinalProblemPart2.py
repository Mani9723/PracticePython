"""
In the previous exercise we saved information about famous scientists’ names and birthdays to disk.
In this exercise, load that JSON file from disk, extract the months of all the birthdays, and
count how many scientists have a birthday in each month.

Your program should output something like:

{
	"May": 3,
	"November": 2,
	"December": 1
}
"""

from collections import Counter
import json
from calendar import month_name

def loadFile(filePath):
    with open(filePath, 'r') as bFile:
        return json.load(bFile)

def getNumberOfOccurences():
    dateList = []
    bdayDictionary = loadFile("C:/Users/Home/Desktop/file.json")
    {dateList.append(month_name[(int)(v.split('/')[0])]) for k,v in bdayDictionary.items()}
    return Counter(dateList)

def printValues():
    print("Frequency of Birthdays:\n")
    {print("\t",k,": ",v,"\t") for k, v in getNumberOfOccurences().items()}  

def main():
    printValues()

if __name__ == '__main__':
    main()



