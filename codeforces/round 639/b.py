def task(n, table):
    builds = 0
    while n > 1:
        for i in range(1, len(table)):
            if table[i] > n:
                builds += 1
                # print(n, table[i - 1], n - table[i - 1])
                n -= table[i - 1]
                break
    print(builds)


table = [0]
triangles = 0
rows = 0
for i in range(1, 30001):
    triangles += i
    rows += i - 1
    total = triangles * 2 + rows
    table.append(total)
# print(table)
t = int(input())
for i in range(0, t):
    n = int(input())
    task(n, table)
