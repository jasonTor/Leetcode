#645. Set Mismatch

def findErrorNums(nums):
    return [[i for i in nums if nums.count(i) == 2][0],int(abs((len(nums)*(len(nums)+1))/2 - sum(list(set(nums)))))]