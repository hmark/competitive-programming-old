import math

def kind_anton(n, a, b):
    plus = False
    minus = False
    
    for i in range(0, n):
        if a[i] < b[i] and not plus:
            print('NO')
            return

        if a[i] > b[i] and not minus:
            print('NO')
            return

        if a[i] == 1:
            plus = True
        elif a[i] == -1:
            minus = True

    print('YES')

t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    kind_anton(n, a, b)