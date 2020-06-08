def task(n, x, d):
    size = 1000001
    # size = 100
    table = [0] * size
    # best_months = [0] * n
    suma = 0

    for i in range(1, size):
        suma += i
        table[i] = suma

    # for i in range(0, n):
    #     max_days = min(x, d[i])
    #     free_days = d[i] - max_days
    #     best_months[i] = table[d[i]] - table[free_days]

    start_month = (n * 2) - 1
    current_month = start_month
    total = 0
    best = 0
    days = 0
    while current_month >= 0:
        days += d[current_month % n]

        if days < x:
            total += table[d[current_month % n]]
            current_month -= 1
        else:
            total += table[d[current_month % n]] - table[days - x]
            # print(total)
            best = max(best, total)

            total -= table[d[current_month % n]] - table[days - x]
            days -= d[current_month % n]

            if start_month != current_month:
                days -= d[start_month % n]
                total -= table[d[start_month % n]]
                start_month -= 1
            else:
                current_month -= 1
                start_month -= 1

    print(best)


n, x = map(int, input().split())
d = list(map(int, input().split()))
task(n, x, d)
