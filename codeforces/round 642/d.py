import math


def task(n):
    table = {}
    for i in range(0, n):
        table[i] = []

    table[n] = [[1, n, 1]]
    array = [0] * n
    i = 0

    for size in reversed(range(1, n + 1)):
        if len(table[size]) == 0:
            continue

        intervals = sorted(table[size], key=lambda x: (x[0]))
        for interval in intervals:
            i += 1
            l, r = interval[0], interval[1]

            if (r - l + 1) % 2 == 0:
                index = (l + r - 1) // 2
            else:
                index = (l + r) // 2

            array[index - 1] = i

            if l <= index - 1:
                intervalsize = index - 1 - l + 1
                table[intervalsize].append([l, index - 1])

            if index + 1 <= r:
                intervalsize = r - index - 1 + 1
                table[intervalsize].append([index + 1, r])

            # print(l, r)

    print(" ".join(map(str, array)))


t = int(input())
for i in range(0, t):
    n = int(input())
    task(n)
