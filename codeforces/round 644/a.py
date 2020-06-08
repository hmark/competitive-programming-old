def task(a, b):
    short = min(a, b)
    long = max(a, b)

    if 2 * short >= long:
        size = 2 * short
        print(size * size)
    else:
        size = long
        print(size * size)


t = int(input())
for i in range(0, t):
    a, b = map(int, input().split())
    task(a, b)
