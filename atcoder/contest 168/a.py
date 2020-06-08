def task(n):
    c = int(n[-1])
    if c in [2, 4, 5, 7, 9]:
        print('hon')
    elif c in [0, 1, 6, 8]:
        print('pon')
    elif c in [3]:
        print('bon')


n = input()
task(n)
