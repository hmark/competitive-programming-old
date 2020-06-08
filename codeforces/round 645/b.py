def task(n, a):
    table = {}

    for aa in a:
        if not aa in table:
            table[aa] = 0
        table[aa] += 1

    g = 1

    nxt = 0
    for i in sorted(table.keys()):
        if table[i] > 0:
            if g + nxt + table[i] > i:
                g += nxt + table[i]
                nxt = 0
            else:
                nxt += table[i]

    print(g)


t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
