import math

t = [5, 10, 2, 8, 10]
p = [[2, 1, 3, 4, 5], [3, 2, 4, 1, 5], [4, 2, 3, 5, 1], [1, 2, 3, 5, 4], [3, 4, 2, 1, 5]]

temp = []
for i in range(24):
    temp.append(0)

mina = 100000
for i in range(0, 21):
    for j in range(i+1, 22):
        for k in range(j+1, 23):
            for l in range(k+1, 24):
                for m in range(l+1, 25):
                    a = p[int(math.floor(i/5))][i % 5] + p[int(math.floor(j/5))][j % 5] + p[int(math.floor(k/5))][k % 5] + p[int(math.floor(l/5))][l % 5] + p[int(math.floor(m/5))][m % 5]
                    if a < mina:
                        mina = a
print mina
