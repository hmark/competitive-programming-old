import math


def task(x):
    table = {}
    for i in range(-1000, 1000):
        table[i] = int(math.pow(i, 5))

    for i in range(-1000, 1000):
        for j in range(-1000, 1000):
            if table[i] - table[j] == x:
                print(i, j)
                return
    print(0, 0)


x = int(input())

task(x)
