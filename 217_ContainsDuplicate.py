#217. Contains Duplicate
# Retourne True si la liste d'entier contient un ou des doublons

def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    return len(set(nums)) != len(nums)