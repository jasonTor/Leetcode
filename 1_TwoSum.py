#1. Two Sum
# retourne la position des 2 entiers dans la liste nums tel que la somme fait l'entier target

def twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return[i,j]