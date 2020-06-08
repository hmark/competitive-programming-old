def task(n, a):
    a.sort()

    p0 = 0
    p1 = 0
    diff1 = 0

    for value in a:
        if value % 2 == 0:
            p0 += 1
        else:
            p1 += 1

    index = 1
    while index < n:
        if abs(a[index - 1] - a[index]) == 1:
            diff1 += 1
            index += 1

        index += 1

    if p0 % 2 == 0 and p1 % 2 == 1:
        print("NO")
    elif p0 % 2 == 1 and p1 % 2 == 0:
        print("NO")
    elif p0 % 2 == 0 and p1 % 2 == 0:
        print("YES")
    elif p0 % 2 == 1 and p1 % 2 == 1:
        if diff1 >= 1:
            print("YES")
        else:
            print("NO")


t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
