def task(a, b, c, k):
    pluses = min(a, k)
    zeros = min(b, k - pluses)
    minuses = min(c, k - pluses - zeros)

    total = pluses - minuses
    print(total)


a, b, c, k = map(int, input().split())
task(a, b, c, k)
