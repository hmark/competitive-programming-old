import math
from decimal import Decimal


def task(a, b):
    b = b.replace('.', '')
    if b[0] == '0':
        b = b[1:]
    if b[0] == '0':
        b = b[1:]
    b = int(b)
    res = a * b

    if res < 100:
        print(0)
    else:
        print(str(res)[:-2])


a, b = input().split()
task(int(a), b)
