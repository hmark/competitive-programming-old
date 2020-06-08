import math


def getprimes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def getdivisors(n, primeslist):
    divisors = [n]
    # nn = n
    for prime in primeslist:
        while n % prime == 0:
            divisors.append(prime)
            n = n // prime
        if n == 1:
            # print(nn, divisors)
            return divisors

    return divisors


def gettable(divisors):
    table = {}

    for divisor in divisors:
        if not divisor in table:
            table[divisor] = 0
        table[divisor] += 1

    return table


def mergetable(table1, table2):
    table = {}

    for key in list(table1.keys()) + list(table2.keys()):
        intable1 = key in table1
        intable2 = key in table2

        if intable1 and not intable2:
            table[key] = table1[key]
        elif not intable1 and intable2:
            table[key] = table2[key]
        else:
            table[key] = max(table1[key], table2[key])

    return table


def updatemintable(mintable, currenttable):
    keys = list(mintable.keys())
    for key in keys:
        if not key in currenttable:
            del mintable[key]
        else:
            mintable[key] = min(mintable[key], currenttable[key])


def task(n, a):
    primeslist = getprimes(450)
    # print(primeslist)
    divisors1 = getdivisors(a[0], primeslist)
    divisors2 = getdivisors(a[1], primeslist)
    tables = []
    table1 = gettable(divisors1)
    table2 = gettable(divisors2)
    table = mergetable(table1, table2)

    tables.append(table1)
    tables.append(table2)
    for i in range(2, n):
        divisors = getdivisors(a[i], primeslist)
        currenttable = gettable(divisors)
        tables.append(currenttable)
        updatemintable(table, currenttable)

    # print(table)
    # print(tables)

    total = 1
    for key in table:
        mn1 = 100000000
        found1 = False
        mn2 = 100000000
        found2 = False
        for ttable in tables:
            if not key in ttable:
                continue

            if ttable[key] < mn1:
                mn1 = ttable[key]
                found1 = True
            elif ttable[key] < mn2:
                mn2 = ttable[key]
                found2 = True

        if found1 and found2:
            total *= key**(max(mn1, mn2))
        elif found1:
            total *= key**mn1

    # print(table)
    print(total)

    # print(n, a)


n = int(input())
a = list(map(int, input().split()))
task(n, a)
