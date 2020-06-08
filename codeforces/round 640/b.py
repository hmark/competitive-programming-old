def task(n, k):
    if k > n:
        print("NO")
        return

    if (n - k - 1) % 2 == 1:
        print("YES")
        result = [1] * (k - 1)
        result.append(n - k + 1)
        print(" ".join(map(str, result)))
        return

    if n % 2 == 0 and n >= k * 2:
        print("YES")
        result = [2] * (k - 1)
        result.append(n - 2 * (k - 1))
        print(" ".join(map(str, result)))
        return

    print("NO")


t = int(input())
for i in range(0, t):
    n, k = map(int, input().split())
    task(n, k)
