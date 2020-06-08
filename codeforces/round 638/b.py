def task(n, k, a):
    table = {}

    for value in a:
        table[value] = True

    if len(table.keys()) > k:
        print(-1)
        return

    result = []
    keys = list(table.keys())
    keys_len = len(keys)

    if keys_len < k:
        for i in range(0, k - keys_len):
            keys.append(1)

    for value in a:
        for key in keys:
            result.append(key)

    print(len(result))
    print(" ".join(map(str, result)))


t = int(input())
for i in range(0, t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    task(n, k, a)
