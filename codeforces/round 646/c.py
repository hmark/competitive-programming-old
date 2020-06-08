def task(n, x, u, v):
    tree = {}

    for i in range(0, n - 1):
        if not u[i] in tree:
            tree[u[i]] = set()

        if not v[i] in tree:
            tree[v[i]] = set()

        tree[u[i]].add(v[i])
        tree[v[i]].add(u[i])

    if not x in tree or len(tree[x]) < 2:
        print("Ayush")
        return

    traversed = {}
    traversed[x] = True
    nodes = list(tree[x])
    for node in nodes:
        traversed[node] = True
    count = len(nodes) - 1
    while len(nodes) > 0:
        current = nodes.pop()
        for node in tree[current]:
            if not node in traversed:
                traversed[node] = True
                nodes.append(node)
                count += 1

    if count % 2 == 1:
        print("Ashish")
    else:
        print("Ayush")


t = int(input())
for i in range(0, t):
    n, x = map(int, input().split())
    u = []
    v = []
    for j in range(0, n - 1):
        uu, vv = map(int, input().split())
        u.append(uu)
        v.append(vv)
    task(n, x, u, v)
