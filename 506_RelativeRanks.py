#506. Relative Ranks

def findRelativeRanks(score):
    temp = list(score)
    temp.sort()
    l = []
    d = {}
    for i in range(1,len(score)+1):
        if i == 1:
            d[temp[-i]] = "Gold Medal"
        elif i == 2:
            d[temp[-i]] = "Silver Medal"
        elif i == 3:
            d[temp[-i]] = "Bronze Medal"
        else:
            d[temp[-i]] = str(i)
    for i in score:
        l.append(d[i])
    return l
