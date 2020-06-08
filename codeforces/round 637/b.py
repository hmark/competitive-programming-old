def task(n, k, a):
    peeks = {}

    for i in range(0, n):
        if i == 0 or i == n - 1:
            continue

        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            peeks[i] = True

    current_peeks = 0
    for i in range(1, k - 1):
        if i in peeks:
            current_peeks += 1

    best = current_peeks
    best_l = 0

    for l in range(1, n - k + 1):
        if l in peeks:
            current_peeks -= 1

        r = l + k - 1
        if (r - 1) in peeks:
            current_peeks += 1

        if current_peeks > best:
            best = current_peeks
            best_l = l

    print(best + 1, best_l + 1)


t = int(input())
for i in range(0, t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    task(n, k, a)
