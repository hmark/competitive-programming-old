import math


def task(n):
    amount = 1
    mass = 1
    days = 0
    adds = []

    while True:
        if mass + 4 * amount <= n:
            news = amount
        elif mass + 2 * amount >= n:
            news = n - mass - amount
        else:
            news = max(0, math.floor((n - mass - amount * 2) / 2))

        amount += news
        adds.append(news)
        mass += amount

        days += 1

        if mass == n:
            break

    print(days)
    print(" ".join(map(str, adds)))

    #print(n, k, s, mn, mx)


t = int(input())
for i in range(0, t):
    n = int(input())
    task(n)
