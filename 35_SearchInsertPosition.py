#35 Search Insert Position
# retourne la position de l'entier dans la liste trié dans l'ordre croissant

def searchInsert(self, nums, target):
    i = 0
    while nums[i] < target:
        i+=1
        if i == len(nums):
            return len(nums)
    return i