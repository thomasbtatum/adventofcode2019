
def findSum(nums,sum):
    leftIdx = 0
    rightIdx = len(nums)-1

    while(leftIdx != rightIdx):
        sums = nums[leftIdx] + nums[rightIdx]

        if(sums == sum):
            return True
        else:
            if(sums < sum):
                leftIdx=leftIdx+1
            else:
                rightIdx=rightIdx-1
    return False

val = findSum([1,2,4,4,6,7,9],88)
print(val)