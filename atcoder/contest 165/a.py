def task(k, a, b):
    for i in range(a, b + 1):
        if i % k == 0:
            print("OK")
            return

    print("NG")


k = int(input())
a, b = map(int, input().split())
task(k, a, b)
