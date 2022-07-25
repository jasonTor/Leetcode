def isPrime(n):
    for i in range(2,int(n/2)+1):
        if n%i == 0:
            return False
    return True

def primeDecomp(n):
    l = []
    if isPrime(n):
        return [n]
    else :
        for i in range(2,n):
            #print(i)
            if n%i == 0:
                l = l + primeDecomp(i)
    l = list(set(l))
    return l


def isUgly(n):
    if n == 1:
        return True
    return all(i in [2,3,5] for i in primeDecomp(n))

