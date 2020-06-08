def task(a, b, c, d):
    print(b, c, c)


t = int(input())
for i in range(0, t):
    a, b, c, d = map(int, input().split())
    task(a, b, c, d)
