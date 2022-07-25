#128. Longest Consecutive Sequence
#retourne le nombre d'élément de la plus grande suite d'éléments consécutive

def longestConsecutive(nums):
    a = list(set(nums))
    a.sort()
    s = []
    l = []
    for i in range(len(a)):
        if i == 0:
            l.append(a[i])
        else :
            if a[i] == a[i-1] + 1:
                l.append(a[i])
            else :
                s.append(len(l))
                l.clear()
                l.append(a[i])
    s.append(len(l))
    return max(s)
