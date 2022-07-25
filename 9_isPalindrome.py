def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        a = str(x)
        a = list(a)
        if len(a)%2 == 0:
            for i in range(int(len(a)/2)):
                temp = a[i]
                a[i] = a[-i-1]
                a[-i-1] = temp
        else :
            for i in range(int((len(a)+1)/2)):
                temp = a[i]
                a[i] = a[-i-1]
                a[-i-1] = temp
        a = "".join(a)
        return a==str(x)



'''La fonction join
>>> strList = ["Hi" , "welcome", "to", "WayToLearnX"]
>>> str = 'AZER'.join(strList)
>>> str
'HiAZERwelcomAZERtoAZERWayToLearnX'
'''