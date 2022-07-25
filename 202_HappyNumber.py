#202. Happy Number

from math import sqrt
def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    a = str(n)
    l = []
    b = True
    while b:
        temp = 0
        for i in range(len(a)):
            temp = temp + int(a[i])**2
        a = str(temp)
        if temp in l:
            return False
        elif temp == 1:
            return True
        l.append(temp)