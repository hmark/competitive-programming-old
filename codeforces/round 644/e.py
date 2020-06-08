def task(n, grid):
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            if grid[i][j] == 1 and grid[i + 1][j] == 0 and grid[i][j + 1] == 0:
                print("NO")
                return
    print("YES")


t = int(input())
for i in range(0, t):
    n = int(input())
    grid = []
    for j in range(0, n):
        row = [int(c) for c in input()]
        grid.append(row)
    task(n, grid)
