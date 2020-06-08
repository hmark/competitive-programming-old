def task(n, a):
    aa = 0
    bb = 0
    moves = 0
    Alice = True

    last = 0
    candies = 0
    while True:
        if Alice:
            candy = a.pop(0)
            candies += candy
            aa += candy
        else:
            candy = a.pop()
            candies += candy
            bb += candy

        if len(a) == 0:
            moves += 1
            break

        if candies > last:
            last = candies
            candies = 0
            Alice = not Alice
            moves += 1


    print(moves, aa, bb)


t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    task(n, a)
