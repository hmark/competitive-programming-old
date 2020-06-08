import math

def little_artem(n, m):
    grid = []
    for row in range(0, n):
        grid.append([])
        for col in range(0, m):
            grid[row].append('B')

    whites = math.ceil(n * m / 2) - 1

    i = 0
    j = 1
    even = True
    while (whites > 0):
        grid[i][j] = 'W'
        whites -= 1

        if j + 2 < m:
            j += 2
        else:
            i += 1
            if even:
                j = 0
            else:
                j = 1
            even = not even

    for i in range(0, n):
        print("".join(grid[i]))

t = int(input())
for i in range(0, t):
    n, m = map(int, input().split())
    little_artem(n, m)