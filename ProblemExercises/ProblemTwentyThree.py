""" 
File Overlap
Two .txt file contain primes and happy numbers respectively
find the overlapping numbers
"""
def readPrimeFile(filePath):
    sets = []
    with open(filePath,'r') as file:
        [sets.append((int)(numbers)) for numbers in file]
    return set(sets)

def setIntersect(fileOne, fileTwo ):
    return sorted(readPrimeFile(fileOne) & readPrimeFile(fileTwo))

def main():
    primePath = 'C:/Users/Home/Desktop/primes.txt' 
    happyPath = 'C:/Users/Home/Desktop/happyNumbers.txt'
    print(setIntersect(primePath,happyPath))

if __name__ == '__main__':
    main()