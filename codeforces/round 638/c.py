import math


def task(n, k, s):
    s = [char for char in s]
    s.sort()

    mn = min(s[0:k])
    mx = max(s[0:k])

    if mn != mx or k == n:
        print(mx)
        return

    a = [mn]

    mn = min(s[k:])
    mx = max(s[k:])

    if mn != mx:
        a += s[k:]
        print("".join(map(str, a)))
        return

    repeats = math.ceil((n - k) / k)
    a += repeats * mx
    print("".join(map(str, a)))

    #print(n, k, s, mn, mx)


t = int(input())
for i in range(0, t):
    n, k = map(int, input().split())
    s = input()
    task(n, k, s)
