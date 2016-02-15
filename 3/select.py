a1 = [1, 2, 4, 6, 8]
a2 = [3, 5, 7, 9, 10]
r = 11

def smallestR(a1, a2, r):
    smallestCounter = 1
    i = 0
    j = 0
    n = len(a1)
    while i < n and j < n:
        if a1[i] < a2[j]:
            if smallestCounter == r:
                return a1[i]
            smallestCounter += 1
            i += 1
        else:
            if smallestCounter == r:
                return a2[j]
            smallestCounter += 1
            j += 1

    if i == n:
        while j < n:
            if smallestCounter == r:
                return a2[j]
            smallestCounter += 1
            j += 1
    else:
        while i < n:
            if smallestCounter == r:
                return a1[i]
            smallestCounter += 1
            i += 1

print smallestR(a1, a2, r)
