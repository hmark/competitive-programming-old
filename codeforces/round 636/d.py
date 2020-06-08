def task(n, k, a):
    sums = {}
    maxk = k * 2 + 2
    mins = [0] * maxk
    maxs = [0] * maxk

    half = int(n / 2)

    for i in range(0, half):
        c = a[i]
        d = a[n - 1 - i]
        suma = c + d

        if not suma in sums:
            sums[suma] = 0

        sums[suma] += 1

        mins[min(c, d) + 1] += 1
        maxs[max(c, d) + k + 1] += 1

    value = 0
    best = half

    for i in range(0, maxk):
        value += mins[i] - maxs[i]
        if i in sums:
            one_swap = value - sums[i]
            two_swaps = half - value
            swaps = one_swap + 2 * two_swaps
            best = min(best, swaps)

    print(best)


t = int(input())
for i in range(0, t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    task(n, k, a)
