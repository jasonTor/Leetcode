#136. Single Number
# renvoie l'élément unique dans la liste ou il n'y a que des éléments qui apparaissent 2 fois

def singleNumber(nums):
    nums.sort()
    for i in range(int(len(nums)/2+1)):
        if i == int(len(nums)/2):
            return nums[i*2]
        if nums[2*i] != nums[2*i+1]:
            return nums[2*i]