def task(n):
    if n <= 3:
        print(-1)
        return

    if n == 4:
        print('3 1 4 2')
        return

    used = [False] * (n + 1)
    current = 1
    direction = 1
    directionChanged = False
    results = [1]
    used[1] = True

    while True:
        found = False
        if direction == 1:
            for i in [2, 4, 3]:
                if current + i <= n and not used[current + i]:
                    used[current + i] = True
                    current += i
                    results.append(current)
                    found = True
                    directionChanged = False
                    break
        else:
            for i in [-4, -3, -2]:
                if current + i >= 1 and not used[current + i]:
                    used[current + i] = True
                    current += i
                    results.append(current)
                    found = True
                    directionChanged = False
                    break
        if not found:
            if directionChanged:
                break
            else:
                directionChanged = True
                direction *= -1

    print(" ".join(map(str, results)))


t = int(input())
for i in range(0, t):
    n = int(input())
    task(n)
