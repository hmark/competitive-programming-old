def task(n, a):
    occupied = {}
    for k in range(-2 * n - 1, 2 * n + 1):
        target = k + (a[k % n] % n)

        if target in occupied:
            # print(occupied)
            print('NO')
            return

        occupied[target] = True
    # print(occupied)
    print('YES')


t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
