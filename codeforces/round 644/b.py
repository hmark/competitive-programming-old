def task(n, s):
    s.sort()

    best = 1000000
    for i in range(1, len(s)):
        diff = abs(s[i - 1] - s[i])
        if diff < best:
            best = diff
    print(best)


t = int(input())
for i in range(0, t):
    n = int(input())
    s = list(map(int, input().split()))
    task(n, s)
