import math


def task(a, b, n):
    x = min(b - 1, n)
    print(math.floor(a * x / b) - a * math.floor(x / b))


a, b, n = map(int, input().split())
task(a, b, n)
