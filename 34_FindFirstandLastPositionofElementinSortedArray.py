#34. Find First and Last Position of Element in Sorted Array

def searchRange(nums, target):
    if target not in nums:
        return [-1,-1]
    a = [i for i in list(enumerate(nums)) if i[1] == target]
    return [a[0][0],a[-1][0]]