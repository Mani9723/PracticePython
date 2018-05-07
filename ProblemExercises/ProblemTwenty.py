"""
Binary Search
"""
import random
def binarySearch(target, array):
    print(array)
    low = 0
    high = len(array)-1

    if(target>array[high] or target<array[low]):
        return False
    while(low<=high):
        mid = (low+high)>>1
        midValue = array[mid]
        if(target > midValue):
            low = mid+1
        elif(target < midValue):
            high = mid -1
        else:
            return True
    return False

def main():
    array = [random.randint(1,1000) for x in range(10,random.randint(11,1000))]
    array.sort()
    print(binarySearch(11,array))

if __name__ == '__main__':
    main()