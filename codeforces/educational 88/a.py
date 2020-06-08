import math


def task(n, m, k):
    hand = n // k
    handbest = min(hand, m)

    otherbest = int(math.ceil((m - handbest) / (k - 1)))
    best = handbest - otherbest
    print(best)


t = int(input())
for i in range(0, t):
    n, m, k = map(int, input().split())
    task(n, m, k)
