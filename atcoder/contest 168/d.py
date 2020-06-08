def task(n, m, a, b):
    graph = []
    for i in range(0, n + 1):
        graph.append(set())

    for i in range(0, m):
        graph[a[i]].add(b[i])
        graph[b[i]].add(a[i])
    # print(graph)

    stack = [1]
    ans = 0
    traversed = {}
    traversed[1] = True

    while len(stack):
        nxtstack = set()
        ans += 1
        while len(stack):
            nxt = stack.pop()
            for value in graph[nxt]:
                if not value in traversed:
                    nxtstack.add(value)
                    traversed[value] = nxt
        stack = nxtstack

    for i in range(1, n + 1):
        if not i in traversed:
            print("No")
            return

    print("Yes")
    for i in range(2, n + 1):
        print(traversed[i])


n, m = map(int, input().split())
a = []
b = []
for i in range(0, m):
    aa, bb = map(int, input().split())
    a.append(aa)
    b.append(bb)
task(n, m, a, b)
