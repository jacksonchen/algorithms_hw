def ksort(a):
    outofOrder = []
    for i in range(1, len(a)):
        for j in range(0, i):
            if (a[j] > a[i]):
                outofOrder.append(a[i])
                break
    return outofOrder

print ksort([1,3,5,2,7,10,8])
