def task(n, m, x, y, a):
    ones = 0
    twos = 0
    for i in range(0, n):
        j = 0
        while j < m:
            if a[i][j] == ".":
                if j < m - 1 and a[i][j + 1] == ".":
                    twos += 1
                else:
                    ones += 1
                j += 2
            else:
                j += 1

    ans = min(ones * x + twos * y, (ones + twos * 2) * x)
    print(ans)


t = int(input())
for i in range(0, t):
    a = []
    n, m, x, y = map(int, input().split())
    for i in range(0, n):
        a.append(input())
    task(n, m, x, y, a)
