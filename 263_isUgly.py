#263. UglyNumber
#un nombre est Ugly lorsque ses facteurs premiers sont limités à 2,3 et 5

def isUgly(n):
    if n == 1:
        return True
    elif n < 1:
        return False
    while n>1:
        if n%2 == 0:
            n = n/2
        elif n%3 == 0:
            n = n/3
        elif n%5 == 0:
            n = n/5
        else:
            return False
    return True