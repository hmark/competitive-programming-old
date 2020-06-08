def eugene_and_an_array(n, a):

    valPossible = [0]
    dp = {}
    sm = 0

    for i in range(0, n):
        sm += a[i]
        valPossible.append(sm)

    dp[0] = 1
    posFrom = 1
    result = 0

    for posTo in range(1, n + 1):
        val = valPossible[posTo]

        if a[posTo - 1] == 0:
            posFrom = posTo + 1
            continue

        posFrom = max(posFrom, dp[val] + 1 if val in dp else 0)
        dp[val] = posTo + 1
        result += posTo - posFrom + 1

    
    # print(n)
    # print(a)
    # print(table)
    print(result)


n = int(input())
a = list(map(int, input().split()))
eugene_and_an_array(n, a)