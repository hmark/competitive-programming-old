def eugene_and_an_array(n, a):
    table = {}
    total = 0
    table[0] = 0
    ans = 0
    posFrom = 0

    for posTo in range(0, n):
        if a[posTo] == 0:
            posFrom = posTo + 1
            continue

        ans += a[posTo]
        
        if ans in table:
            posFrom = max(table[ans] + 1, posFrom)

        total += posTo - posFrom + 1
        table[ans] = posTo + 1
    
    print(total)


n = int(input())
a = list(map(int, input().split()))
eugene_and_an_array(n, a)