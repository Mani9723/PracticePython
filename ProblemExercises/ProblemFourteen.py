#Remove any duplicates in a list or a set

def useSet(set):
    print(set)

def useList(list):
    newList = []
    [newList.append(x) for x in list if(x not in newList)]
    print(newList)

def main():
    a = [1,1,2,3,4,23,5,34,5,4,6,7,4,2]
    useSet((set)(a))
    useList(a)

main()