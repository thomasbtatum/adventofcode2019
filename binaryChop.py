def chop(target, numList):
    #returns index of target in numList
    leftIdx = 0
    rightIdx = len(numList)-1
    while(leftIdx <= rightIdx):
        mid = (leftIdx+rightIdx)//2
        if (numList[mid] < target):
            leftIdx = mid+1
        elif (numList[mid] > target):
            rightIdx = mid-1
        else:
            return mid
    return -1

print(chop(3,[]))
print(chop(3, [1]))
print(chop(1, [1]))
print(chop(1, [1, 3, 5]))
print(chop(3, [1, 3, 5]))
print(chop(5, [1, 3, 5]))
print(chop(7, [1, 3, 5, 7]))