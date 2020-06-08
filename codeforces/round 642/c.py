import math


def task(n):
    total = 0
    cells = 0
    distance = 0

    for i in range(0, (n - 1) // 2):
        cells += 8
        distance += 1
        total += cells * distance

    print(total)


t = int(input())
for i in range(0, t):
    n = int(input())
    task(n)
