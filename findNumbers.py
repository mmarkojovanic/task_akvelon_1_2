def findNumbers(y):
    y1 = []
    y2 = []
    for i in range(len(y)):
        if y[i]<0:
            y1.append(y[i])
        else:
            y2.append(y[i])
    x1 = sorted(y1, reverse=True)
    x2 = sorted(y2)
    i = 0
    j = 0
    ret1 = 0
    ret2 = 0
    summ = 2000000000
    while( i<len(x1) and j<len(x2)):
        if(x1[i]+x2[j]==0):
            return x1[i], x2[j]
        elif abs(x1[i]+x2[j])<summ:
            ret1 = x1[i]
            ret2 = x2[i]
            summ = abs(x1[i]+x2[j])
            if(x1[i]+x2[j]<0):
                j+=1
            else:
                i+=1
    return ret1, ret2
    





x = [1, 3, 2, -4, 5, -6, 4, 0, -3]
print(findNumbers(x))
