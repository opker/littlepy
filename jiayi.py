# _*_ coding: utf-8 _*_

def pulsine(l):
    for i in range(len(l)-1,-1,-1):
        if (l[i] < 9):
            l[i] = l[i] + 1
            return l
        l[i] = 0

    t = [0]*(len(l)+1)
    t[0] = 1
    return t

l = [1,2,3]
print(pulsine(l))
