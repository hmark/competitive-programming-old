def task(t, x, y, m):
    time = 0
    for c in m:
        distance = abs(x) + abs(y) - time
        if distance <= 0:
            print("Case #" + str(t) + ":", time)
            return

        if c == 'S':
            y -= 1
        elif c == 'N':
            y += 1
        elif c == 'W':
            x -= 1
        elif c == 'E':
            x += 1

        time += 1

    distance = abs(x) + abs(y) - time
    if distance <= 0:
        print("Case #" + str(t) + ":", time)
        return

    print("Case #" + str(t) + ":", "IMPOSSIBLE")


t = int(input())
for i in range(0, t):
    x, y, m = input().split()
    x = int(x)
    y = int(y)
    task(i + 1, x, y, m)
