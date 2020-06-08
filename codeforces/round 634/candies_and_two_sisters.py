import math


def candies_and_two_sisters(n):
    a = math.floor(n / 2) + 1
    total = n - a
    print(total)


t = int(input())
for i in range(0, t):
    n = int(input())
    candies_and_two_sisters(n)
