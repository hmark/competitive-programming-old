def task(n):
    k = 1
    exp = 1
    for i in range(1, 100):
        exp *= 2
        k += exp
        if n % k == 0:
            print(int(n / k))
            break


t = int(input())
for i in range(0, t):
    n = int(input())
    task(n)
