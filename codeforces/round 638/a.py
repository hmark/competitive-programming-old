def task(n):
    suma = 1
    arr = []

    for i in range(0, n):
        suma *= 2
        arr.append(suma)

    a = 0
    b = 0

    while len(arr) > 0:
        if a <= b:
            a += arr.pop()
            b += arr.pop()
        else:
            a += arr.pop(0)
            b += arr.pop()

    diff = abs(a - b)

    print(diff)


t = int(input())
for i in range(0, t):
    n = int(input())
    task(n)
