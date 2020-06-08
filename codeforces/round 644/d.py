def task(n, k):
    if n <= k:
        print(1)
        return

    best = 1000000000
    for i in range(2, min(31623, k + 1)):
        if n % i == 0:
            div = n // i
            if div <= k:
                best = min(best, i)
            else:
                best = min(best, div)

    if best != 1000000000:
        print(best)
    else:
        print(n)


t = int(input())
for i in range(0, t):
    n, k = map(int, input().split())
    task(n, k)
