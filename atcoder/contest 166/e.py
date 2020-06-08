
def task(n, a):
    total = 0
    tl = [0] * n
    tr = [0] * n

    for i in range(0, n):
        l = i - a[i]
        r = i + a[i]

        if l >= 0:
            tl[l] += 1

        if r < n:
            tr[r] += 1

    for i in range(0, n):
        if tl[i] > 0 and tr[i] > 0:
            total += tl[i] * tr[i]

    print(total)


n = int(input())
a = list(map(int, input().split()))

task(n, a)
