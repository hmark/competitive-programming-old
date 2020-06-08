def task(n, m):
    if n == 1:
        print(0)
    elif n == 2:
        print(m)
    else:
        print(2 * m)


t = int(input())
for i in range(0, t):
    n, m = map(int, input().split())
    task(n, m)
