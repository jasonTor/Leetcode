#561. Array Partition

def arrayPairSum(self, nums):
    nums.sort()
    l = []
    for i in range(len(nums)//2):
        l.append([nums[2*i],nums[2*i+1]])
    s = 0
    for i in l:
        s += min(i)
    return s