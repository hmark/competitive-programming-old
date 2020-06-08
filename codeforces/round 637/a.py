def task(n, a, b, c, d):
    if ((a - b) * n) <= c + d and ((a + b) * n) >= c - d:
        print("YES")
    else:
        print("NO")


t = int(input())
for i in range(0, t):
    n, a, b, c, d = map(int, input().split())
    task(n, a, b, c, d)
