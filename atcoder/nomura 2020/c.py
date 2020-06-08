def task(n, a):
    mxs = []
    current = 1

    for i in range(0, n + 1):
        mxs.append(current)
        current = (current - a[i]) * 2

        if current < 0:
            print(-1)
            return

    # print(mxs)

    v = 0
    nodes = 0
    for i in reversed(range(0, n + 1)):
        nodes = min(nodes + a[i], mxs[i])
        v += nodes

    print(v)


n = int(input())
a = list(map(int, input().split()))
task(n, a)
