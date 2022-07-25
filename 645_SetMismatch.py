#645. Set Mismatch

def findErrorNums(nums):
    L = [0 for i in range(len(nums))]
    for i in nums:
        L[i-1]+=1
    x,y=-1,-1
    for i in range(len(nums)):
        if L[i]==0:
            y = i+1
        elif L[i]==2:
            x = i+1
    return [x,y]