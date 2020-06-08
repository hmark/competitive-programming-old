def task(n, m):
    if n == 1 or m == 1:
        print("YES")
    elif n == 2 and m == 2:
        print("YES")
    else:
        print("NO")


t = int(input())
for i in range(0, t):
    n, m = map(int, input().split())
    task(n, m)
