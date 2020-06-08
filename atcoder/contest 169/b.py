def task(n, a):
    for value in a:
        if value == 0:
            print(0)
            return

    ans = a[0]
    limit = pow(10, 18)
    for i in range(1, n):
        ans *= a[i]
        if ans > limit:
            print(-1)
            return

    print(ans)


n = int(input())
a = list(map(int, input().split()))
task(n, a)
