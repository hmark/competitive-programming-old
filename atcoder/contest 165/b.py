import math


def task(x):
    years = 0
    yens = 100
    while yens < x:
        yens = math.floor(yens * 1.01)
        years += 1

    print(years)


x = int(input())
task(x)
