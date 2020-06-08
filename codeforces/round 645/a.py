import math


def task(n, m):
    cells = n * m
    lamps = math.floor(cells / 2)

    if cells % 2 == 1:
        lamps += 1

    print(lamps)


t = int(input())
for i in range(0, t):
    n, m = map(int, input().split())
    task(n, m)
