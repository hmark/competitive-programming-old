   def task(n, k):
        reminder = k % (n - 1)
        deltas = k // (n - 1)
        total = (deltas * n - 1)
        if reminder > 0:
            total += reminder + 1
        print(total)

    t = int(input())
    for i in range(0, t):
        n, k = map(int, input().split())
        task(n, k)
