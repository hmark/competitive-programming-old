def task(n, k):
    divisor = 0
    for i in range(0, k):
        if n % 2 == 0:
            n += (k - i) * 2
            break

        for i in range(2, n + 1):
            if n % i == 0:
                divisor = i
                break
        n += divisor

    print(n)


t = int(input())
for i in range(0, t):
    n, k = map(int, input().split())
    task(n, k)
