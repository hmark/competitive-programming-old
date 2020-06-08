def task(n, m, x, c, a):
    mx = [0] * m
    for i in range(0, n):
        for j in range(0, m):
            mx[j] += a[i][j]

    for j in range(0, m):
        if mx[j] < x:
            print(-1)
            return

    states = [0] * m

    best = 100000000
    for i in range(1, 2**n):
        price = 0

        for k in range(0, m):
            states[k] = 0

        for j in range(0, n):
            if ((i >> j) & 1):
                price += c[j]
                for k in range(0, m):
                    states[k] += a[j][k]

        if price < best:
            found = True
            for k in range(0, m):
                if states[k] < x:
                    found = False
                    break

            if found:
                best = price

    print(best)


n, m, x = map(int, input().split())
c = []
a = []
for i in range(0, n):
    values = list(map(int, input().split()))
    c.append(values[0])
    a.append(values[1:])

task(n, m, x, c, a)
