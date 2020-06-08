def task(n):
    arrs = [10000, 1000, 100, 10, 1]
    results = []

    for value in arrs:
        a = value * (n // value)
        if a > 0:
            results.append(str(a))
        n -= a
    print(len(results))
    print(" ".join(results))


t = int(input())
for i in range(0, t):
    n = int(input())
    task(n)
