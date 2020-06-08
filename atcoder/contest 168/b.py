def task(k, s):
    if len(s) <= k:
        print(s)
    else:
        print(s[0:k] + '...')


k = int(input())
s = input()
task(k, s)
