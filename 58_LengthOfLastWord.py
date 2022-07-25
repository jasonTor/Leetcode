#58. Length of Last Word
#Renvoie le nombre de charactère du dernier mot d'une phrase

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    c = 0
    for i in range(1,len(s)+1):
        while s[-i] != ' ':
            c += 1
            if i == len(s):
                return c
            if s[-i-1] == ' ':
                return c
            i += 1

#Plus rapide
def lengthOfLastWord(self, s: str) -> int:
    return len(s.strip().split()[-1])


# strip() supprime les espaces à gauche et a droite
# autre exemple : strip("abc") supprime toute les a b et c a gauche et a droite

# split() : renvoie la liste des chaines de charactère séparé par un espace
# autre exemple : split("a") renvoie la liste des chaines de charactère séparé par un "a"