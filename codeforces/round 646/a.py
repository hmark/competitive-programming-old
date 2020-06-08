def task(n, x, a):
    odds = 0
    evens = 0
    for value in a:
        if value % 2 == 0:
            evens += 1
        else:
            odds += 1

    if odds == 0:
        print("No")
        return

    if evens == 0:
        if x % 2 == 1:
            print("Yes")
            return
        else:
            print("No")
            return

    if x < evens + odds:
        print("Yes")
        return
    else:
        if odds % 2 == 1:
            print("Yes")
            return
        else:
            print("No")
            return


t = int(input())
for i in range(0, t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    task(n, x, a)
