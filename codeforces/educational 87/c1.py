import math


def task(n):
    angles = ((2 * n) - 2) * 180
    angle = (angles / (2 * n)) / 2
    # print(2*n)
    # print(angle)
    radians = math.radians(angle)
    if n % 2 == 1:
        x = 0.5 / math.cos(radians)
    else:
        x = math.tan(radians)

    # print(n, x, round(y * 2, 9))
    print("{:.9f}".format(round(x, 9)))


t = int(input())
for i in range(0, t):
    n = int(input())
    task(n)
