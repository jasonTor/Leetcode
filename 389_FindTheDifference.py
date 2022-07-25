#389. Find the Difference
#renvoie la lettre qui a été rajouté dans s à une position aléatoire

def findTheDifference(s, t):
    for i in range(len(t)):
        if t.count(t[i]) != s.count(t[i]):
            return t[i]