def readFile(filePath):
    nameList = []
    with open(filePath,'r') as file:
        for line in file:
            nameList.append(line)
    print(file.closed)
    return len(nameList)



def main():
    numberOfLines = readFile('C:/Users/Home/Desktop/nameList.txt')
    print("There were ", numberOfLines, " names on the list.")

if __name__ == '__main__':
    main()


