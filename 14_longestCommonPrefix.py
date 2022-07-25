#retourne le préfixe commun d'une liste de chaine de charactère

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    len_strs = []
    for i in strs:
        len_strs.append(len(i))
        if len(i) == 0:
            return ""

    ind_pp =  0
    while len_strs[ind_pp] != min(len_strs):
        ind_pp += 1

    l = []
    ind_char = 0
    while ind_char < min(len_strs):
        for i in strs:
            if strs[ind_pp][ind_char] != i[ind_char]:
                return "".join(l)
        l.append(strs[ind_pp][ind_char])
        ind_char += 1
    return "".join(l)
