#70 Climbing Stairs
#Le but est de trouver en combien de façon on peut arriver à la marche n sachant qu'on peut monter que d'une marche ou de 2 d'un coup l'un après l'autre

def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fact(n-1)

def climbStairs(n):
    i = 0
    c1 = n
    c2 = 0
    for j in range(n//2+1):
        i += fact(c1+c2)/(fact(c1)*fact(c2))
        c1 -= 2
        c2 += 1
    return int(i)

#nombre de permutation possible d'une liste l = [1,..,1,2,...,2] avec card(1)=p card(2)=q card(l)=n est de n!/(p!*q!)

#exemple : l = [1,1,1,2,2]
#nombre de permut = 120/(6*2) = 10