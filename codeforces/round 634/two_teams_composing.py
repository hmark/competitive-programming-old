import math


def two_teams_composing(n, a):
    table = {}
    team1 = 0
    team2 = 1

    for i in range(0, n):
        if not a[i] in table:
            table[a[i]] = 1
            team1 += 1
        else:
            table[a[i]] += 1
            team2 = max(team2, table[a[i]])

    if team1 > team2:
        print(team2)
    elif team1 == team2:
        print(team2 - 1)
    else:
        print(team1)


t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    two_teams_composing(n, a)
