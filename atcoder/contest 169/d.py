def task(n):
    if n == 1:
        print(0)
        return

    primes = {}
    i = 2
    while i < 1000001 and i <= n:
        if n % i == 0:
            n = n // i
            if not i in primes:
                primes[i] = 0
            primes[i] += 1
        else:
            i += 1

    # print(primes)
    ans = 0

    if n > 1:
        ans = 1

    for prime in primes:
        e = 1
        count = primes[prime]
        while count >= e:
            count -= e
            e += 1
            ans += 1

    print(ans)


n = int(input())
task(n)
