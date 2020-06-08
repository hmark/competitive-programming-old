def task(n, p):
    start = -1
    prev = -1

    for i in range(0, len(p)):
        if start == -1:
            start = p[i]
        else:
            if prev > p[i]:
                start = p[i]
            elif prev + 1 < p[i]:
                print("No")
                return

        prev = p[i]

    print("Yes")


t = int(input())
for i in range(0, t):
    n = int(input())
    p = list(map(int, input().split()))
    task(n, p)
