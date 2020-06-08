def fill(table, s):
    last1 = -1
    last2 = -1
    last3 = -1
    index = 0
    for c in s:
        value = int(c)
        if value == 1:
            last1 = index
        elif value == 2:
            last2 = index
        elif value == 3:
            last3 = index

        if last1 != -1:
            table[0][index] = min(table[0][index], abs(last1 - index))
        if last2 != -1:
            table[1][index] = min(table[1][index], abs(last2 - index))
        if last3 != -1:
            table[2][index] = min(table[2][index], abs(last3 - index))
        index += 1

    last1 = -1
    last2 = -1
    last3 = -1
    index = len(s) - 1
    for c in reversed(s):
        value = int(c)
        if value == 1:
            last1 = index
        elif value == 2:
            last2 = index
        elif value == 3:
            last3 = index

        if last1 != -1:
            table[0][index] = min(table[0][index], abs(last1 - index))
        if last2 != -1:
            table[1][index] = min(table[1][index], abs(last2 - index))
        if last3 != -1:
            table[2][index] = min(table[2][index], abs(last3 - index))
        index -= 1


def task(s):
    n = len(s)
    table = [[1000000] * n, [1000000] * n, [1000000] * n]
    fill(table, s)
    mn = 1000000
    for i in range(0, n):
        suma = table[0][i] + table[1][i] + table[2][i] + 1
        mn = min(mn, suma)

    if mn == 1000000:
        print(0)
        return
    print(mn)
    # print(s)


t = int(input())
for i in range(0, t):
    s = input()
    task(s)
