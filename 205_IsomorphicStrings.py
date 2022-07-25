#205. Isomorphic Strings

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    d = {}
    for i in list(enumerate(s)):
        if i[1] not in d.keys():
            if t[i[0]] not in d.values():
                d[i[1]] = t[i[0]]
            else :
                return False
        else:
            if d[i[1]] != t[i[0]]:
                return False
    return True