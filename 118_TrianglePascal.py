#118. Pascal's Triangle

def generate(numRows):
    if numRows == 1:
        return [[1]]
    l = [[1]]
    for i in range(numRows-1):
        a = [1]
        if len(l[i]) == 1:
            l.append([1,1])
        else :
            for j in range(len(l[i])-1):
                a.append(l[i][j] + l[i][j+1])
            a.append(1)
            l.append(a)
    return l

