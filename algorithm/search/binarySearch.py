def binarySearch(myList,item):
    first = 0
    last = len(myList)-1
    foundFlag = False
    while( first<=last and not foundFlag):
        mid = (first + last)//2
        if myList[mid] == item :
            foundFlag = True
            result_index = mid
        else:
            if item < myList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if foundFlag == True:
        return result_index
    return foundFlag



MyList = [20,30,40,50]
print(binarySearch(MyList,100))