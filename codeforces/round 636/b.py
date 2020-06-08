def task(n):
    if n % 4 != 0:
        print('NO')
        return

    a = [0] * n
    half = int(n / 2)
    chunks = int(n / 4)
    for i in range(0, chunks):
        a[i * 2] = i * 6 + 2
        a[i * 2 + 1] = i * 6 + 4
        a[half + i * 2] = i * 6 + 1
        a[half + i * 2 + 1] = i * 6 + 5

    print('YES')
    print(" ".join(map(str, a)))


t = int(input())
for i in range(0, t):
    n = int(input())
    task(n)
