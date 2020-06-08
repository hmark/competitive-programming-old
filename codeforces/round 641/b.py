def dfs(index, divisor, count, s):
    best = count

    for i in range(index + divisor, len(s) + 1, divisor):
        if s[i - 1] > s[index - 1]:
            best = max(best, dfs(i, i, count + 1, s))

    return best


def task(n, s):
    best = 0
    for index in range(1, n + 1):
        best = max(best, dfs(index, index, 1, s))

    print(best)


t = int(input())
for i in range(0, t):
    n = int(input())
    s = list(map(int, input().split()))
    task(n, s)
