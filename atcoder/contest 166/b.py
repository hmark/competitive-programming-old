def task(n, k, ak):
    table = {}

    for i in range(1, n + 1):
        table[i] = False

    for a in ak:
        for snack in a:
            table[snack] = True

    total = 0
    for flag in table.values():
        if not flag:
            total += 1

    print(total)


n, k = map(int, input().split())
ak = []
for i in range(0, k):
    d = int(input())
    a = list(map(int, input().split()))
    ak.append(a)

task(n, k, ak)
