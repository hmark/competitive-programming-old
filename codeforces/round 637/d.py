# NOT FINISHED !!!


def diff(d1, d2):
    suma = 0
    for i in range(0, 7):
        if d1[i] != d2[i]:
            suma += 1
    return suma


def task(n, k, table):
    digits = ["1110111", "0010010", "1011101", "1011011", "0111010",
              "1101011", "1101111", "1010010", "1111111", "1111011"]

    uses = []
    finals = []

    for i in range(0, n):
        best = 7
        digit = -1
        for j in reversed(range(0, len(digits) - 1)):
            suma = diff(table[i], digits[j])
            if suma < best:
                best = suma
                digit = j

        k -= best

        if k < 0:
            print(-1)
            return

        uses.append(best)
        finals.append(digit)

    for i in range(0, n):
        k += uses[i]

        for j in reversed(range(0, len(digits) - 1)):
            suma = diff(table[i], digits[j])
            if suma <= k:
                finals[i] = j
                k -= suma
                break

        if k == 0:
            print("".join(map(str, finals)))


n, k = map(int, input().split())
table = []
for i in range(0, n):
    table.append(input())
task(n, k, table)
