def task(a, b, c):
    # astart = a
    # bstart = b
    # cstart = c

    s = ''

    if a > 0:
        s += '0' * (a + 1)

    if b > 0 and a > 0:
        s += '1'
        b -= 1

    if c > 0:
        if a == 0:
            s += '1' * (c + 1)
        else:
            s += '1' * c

    if b > 0:
        if a == 0 and c == 0:
            s += '01'
            b -= 1

        s += '01' * (b // 2)
        b -= 2 * (b // 2)

        if b == 1:
            s += '0'
            b -= 1

    print(s)

    # aa = 0
    # bb = 0
    # cc = 0

    # for i in range(1, len(s)):
    #     if s[i - 1] == '0' and s[i] == '1':
    #         bb += 1
    #     elif s[i - 1] == '1' and s[i] == '0':
    #         bb += 1
    #     elif s[i - 1] == '0' and s[i] == '0':
    #         aa += 1
    #     elif s[i - 1] == '1' and s[i] == '1':
    #         cc += 1

    # if astart != aa or bstart != bb or cstart != cc:
    #     print('THIS!!!', s, astart, bstart, cstart)


t = int(input())
for i in range(0, t):
    a, b, c = map(int, input().split())
    task(a, b, c)

# for a in range(0, 10):
#     for b in range(0, 10):
#         for c in range(0, 10):
#             task(a, b, c)
