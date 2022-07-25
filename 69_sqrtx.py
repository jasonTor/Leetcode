#69. srtx
#retourne la partie entiere de la racine carré

def mySqrt(x):
    i = 0
    if x == 0:
        return 0
    while i*i <= x:
        i+=1
    return  i-1