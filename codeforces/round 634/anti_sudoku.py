import math


def anti_sudoku(sudoku):
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku[i][j] == 1:
                sudoku[i][j] = 2

    for i in range(0, 9):
        print("".join(map(str, sudoku[i])))


t = int(input())
for i in range(0, t):
    sudoku = []
    for j in range(0, 9):
        sudoku.append([int(char) for char in input()])
    anti_sudoku(sudoku)
