#520. Detect Capital

def detectCapitalUse(word):
    temp = word
    temp2 = list(temp.lower())
    temp2[0] = temp2[0].upper()
    if word == temp.upper():
        return True
    elif word == temp.lower():
        return True
    elif word == ''.join(temp2):
        return True
    else:
        return False