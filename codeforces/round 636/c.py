def task(n, a):
    total = 0
    positive = a[0] > 0
    mx = a[0]

    for i in range(0, n):
        if positive:
            if a[i] > 0:
                mx = max(mx, a[i])
            else:
                total += mx
                positive = False
                mx = a[i]
        else:
            if a[i] < 0:
                mx = max(mx, a[i])
            else:
                total += mx
                positive = True
                mx = a[i]

    total += mx

    print(total)


t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
