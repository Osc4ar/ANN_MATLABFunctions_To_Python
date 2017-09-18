import math

def hardlim(n):
    if not (type(n) is list):
        if n < 0:
            return 0
        else:
            return 1
    else:
        a = []
        for i in n:
            if i < 0:
                a.append(0)
            else:
                a.append(1)
        return a

def hardlims(n):
    if not (type(n) is list):
        if n < 0:
            return -1
        else:
            return 1
    else:
        a = []
        for i in n:
            if i < 0:
                a.append(-1)
            else:
                a.append(1)
        return a

def purelin(n):
    return n

def satlin(n):
    if not(type(n) is list):
        if n < 0:
            return 0
        elif n > 1:
            return 1
        else:
            return n
    else:
        a = []
        for i in n:
            if i < 0:
                a.append(0)
            elif i > 1:
                a.append(1)
            else:
                a.append(i)
        return a

def satlins(n):
    if not(type(n) is list):
        if n < -1:
            return -1
        elif n > 1:
            return 1
        else:
            return n
    else:
        a = []
        for i in n:
            if i < -1:
                a.append(-1)
            elif i > 1:
                a.append(1)
            else:
                a.append(i)
        return a

def logsig(n):
    if not (type(n) is list):
        return 1 / (1 + math.exp(-n))
    else:
        a = []
        for i in n:
            a.append(1 / (1 + math.exp(-i)))
        return a

def tansig(n):
    if not (type(n) is list):
        return (math.exp(n) - math.exp(-n)) / (math.exp(n) + math.exp(-n))
    else:
        a = []
        for i in n:
            a.append((math.exp(i) - math.exp(-i)) / (math.exp(i) + math.exp(-i)))
        return a

def poslin(n):
    if not (type(n) is list):
        if n < 0:
            return 0
        else:
            return n
    else:
        a = []
        for i in n:
            if i < 0:
                a.append(0)
            else:
                a.append(i)
        return a

def compet(n):
    maxn = n[0]
    imax = 0
    for index, i in enumerate(n):
        if i > maxn:
            imax = index
            maxn = i
    a = [0]*len(n)
    a[imax] = 1
    return a

print(hardlim([-1,  23]))
print(hardlims([-1,  23]))
print(purelin([-1,  23]))
print(satlin([20, -12, 2, 0.3, 1, 0.9]))
print(satlins([20, -12, 2, -0.3, 1, 0.9]))
print(logsig([1, -1, 23, -10]))
print(compet([100, 2, 200, -100, 23, 1202, -20]))
