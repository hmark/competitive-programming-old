# import time


def task(n, m, grid):
    areacount = 0
    rowsState = [0] * n
    colsState = [0] * m
    filled = False
    startprev = -2
    endprev = -2

    for i in range(0, n):
        start = -1
        end = -1
        for j in range(0, m):
            if grid[i][j] == "#":
                if rowsState[i] == 0:
                    rowsState[i] = 1
                    start = j
                    end = j

                if colsState[j] == 0:
                    colsState[j] = 1

                if rowsState[i] == 2 or colsState[j] == 2:
                    print(-1)
                    return

                end = j

            elif grid[i][j] == '.':
                if rowsState[i] == 1:
                    rowsState[i] = 2
                if colsState[j] == 1:
                    colsState[j] = 2
        if start != -1 and not (end >= startprev and start <= endprev):
            # print(start, end, startprev, endprev)
            areacount += 1

        startprev = start
        endprev = end

    filled = False
    emptyRow = False
    emptyCol = False

    for value in rowsState:
        if value == 0:
            emptyRow = True
        else:
            filled = True

    for value in colsState:
        if value == 0:
            emptyCol = True
        else:
            filled = True

    if not filled:
        print(0)
        return

    if (emptyRow and not emptyCol) or (emptyCol and not emptyRow):
        print(-1)
        return

    # print(n, m, grid)
    print(areacount)


# start_time = time.time()
n, m = map(int, input().split())
grid = []
for j in range(0, n):
    s = input()
    row = [c for c in s]
    grid.append(row)
task(n, m, grid)
# print("--- %s seconds ---" % (time.time() - start_time))
