#169. Majority Element
#Retourne l'élément majoritaire

def majorityElement(nums):
    d = {}
    for i in range(len(list(set(nums)))):
        d[list(set(nums))[i]] = len([j for j in nums if j==list(set(nums))[i]])
    d2 = [o for o in d.values()]
    if len([m for m in d2 if m==max(d2)]) == 1:
        return [k for (k, val) in d.items() if val == max(d2)][0]

def majorityElement2(self, nums):
    dup = list(set(nums))
    for i in dup:
        temp = nums.count(i)
        if temp > len(nums)/2:
            return i