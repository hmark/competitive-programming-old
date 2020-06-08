def task(t, u, q, r):
    table = {}
    for i in range(0, len(q)):
        for j in range(0, len(r[i])):
            if not r[i][j] in table:
                table[r[i][j]] = [True] * 10

        table[r[i][0]][0] = False

        if int(q[i]) == -1:
            q[i] = str(pow(10, u) - 1)
            continue

        if len(q[i]) != len(r[i]):
            continue

        for k in range(int(q[i][0]) + 1, 10):
            table[r[i][0]][k] = False

    result = ["_"] * 10

    for i in range(0, 10):
        for letter in table.keys():
            count = 0
            lastIndex = -1
            for i in range(0, 10):
                if table[letter][i]:
                    count += 1
                    lastIndex = i

            if count == 1:
                result[lastIndex] = letter

                for letter2 in table.keys():
                    table[letter2][lastIndex] = False

    if "_" in result:
        for letter in table.keys():
            for i in range(0, 10):
                if table[letter][i]:
                    result[i] = letter

                    for j in range(0, 10):
                        table[letter][j] = False

                    for letter2 in table.keys():
                        table[letter2][i] = False

    print("Case #" + str(t) + ":", "".join(map(str, result)))


t = int(input())
for i in range(0, t):
    u = int(input())
    q = []
    r = []
    for j in range(0, 10000):
        qa, ra = input().split()
        q.append(qa)
        r.append(ra)
    task(i + 1, u, q, r)
