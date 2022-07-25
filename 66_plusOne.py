#66. Plus One
# exemple1 : [1,2,3] -> [1,2,4]
# exemple2 : [9] -> [1,0]

#De manière propre en baclant la complexité spatiale/temporelle
def plusOne1(digits):
    a = [str(i) for i in digits]
    join = "".join(a)
    b = str(int(join) + 1)
    return [int(i) for i in b]


#De manière plus puissante
def plusOne2(digits):
    return [int(j) for j in str(int("".join([str(i) for i in digits])) + 1)]

