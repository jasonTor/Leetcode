#26. Remove Duplicates from Sorted Array
#Il faut enlever les dupliqués d'une liste

def removeDuplicates(nums):
    i = 1
    while i < len(nums):
        if nums[i] in nums[:i]:
            del nums[i]
        else:
            i+=1