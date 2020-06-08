def task(n, m, h, a, b):
    roads = {}

    for i in range(1, n + 1):
        roads[i] = set()

    for i in range(0, m):
        roads[a[i]].add(b[i])
        roads[b[i]].add(a[i])

    total = 0
    for i in range(0, n):
        highest = True

        for road in roads[i + 1]:
            if h[road - 1] >= h[i]:
                highest = False
                break

        if highest:
            total += 1

    print(total)


n, m = map(int, input().split())
h = list(map(int, input().split()))
a = []
b = []
for i in range(0, m):
    aa, bb = map(int, input().split())
    a.append(aa)
    b.append(bb)

task(n, m, h, a, b)
