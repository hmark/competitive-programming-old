import math


def task(x, n, m):
    threshold = m * 10
    for i in range(0, n + 1):
        if x <= threshold:
            print("YES")
            return
        else:
            x = math.floor(x / 2) + 10

    print("NO")


t = int(input())
for i in range(0, t):
    x, n, m = map(int, input().split())
    task(x, n, m)
