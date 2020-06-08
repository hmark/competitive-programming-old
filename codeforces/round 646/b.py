def task(s):
    zeros = 0
    ones = 0
    ans = 1000

    for i in range(0, len(s)):
        if s[i] == '0':
            zeros += 1
        else:
            ones += 1

        one_swaps = ones
        zero_swaps = zeros
        for j in range(i + 1, len(s)):
            if s[j] == '0':
                one_swaps += 1
            else:
                zero_swaps += 1
        ans = min(ans, one_swaps, zero_swaps)

    print(ans)


t = int(input())
for i in range(0, t):
    s = input()
    task(s)
