def task(n, k, a, b):
    a.sort()
    b.sort(reverse=True)

    for i in range(0, k):
        if a[i] < b[i]:
            tmp = a[i]
            a[i] = b[i]
            b[i] = tmp
        else:
            break

    print(sum(a))


t = int(input())
for i in range(0, t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    task(n, k, a, b)
