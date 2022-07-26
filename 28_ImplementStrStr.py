#28. Implement strStr()

def strStr(haystack, needle):
    n = len(needle)
    i = 0
    while n <= len(haystack):
        if haystack[i:i+len(needle)] == needle:
            return i
        i+=1
        n+=1
    return -1