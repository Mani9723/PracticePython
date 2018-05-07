def readFile(filePath):
    nameList = set()
    with open(filePath,'r') as file:
        for line in file:
            tempLine = line.split("/")
            nameList.add(tempLine[2])
    print(file.closed)
    return nameList

def main():
    numberOfCategories = readFile('C:/Users/Home/Desktop/nameList.txt')
    print("There were ", len(numberOfCategories), " categories on the list.")

if __name__ == '__main__':
    main()


