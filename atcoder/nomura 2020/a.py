def task(h1, m1, h2, m2, k):
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2
    t = t2 - t1
    print(max(0, t - k))
    #print(h1, m1, h2, m2, k)


h1, m1, h2, m2, k = map(int, input().split())
task(h1, m1, h2, m2, k)
