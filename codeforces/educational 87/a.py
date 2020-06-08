import math


def task(a, b, c, d):
    remaining = a - b
    total = b

    if remaining <= 0:
        print(b)
        return

    if d >= c:
        print(-1)
        return

    diff = c - d
    sleeps = math.ceil(remaining / diff)

    total += sleeps * c
    print(total)


t = int(input())
for i in range(0, t):
    a, b, c, d = map(int, input().split())
    task(a, b, c, d)
