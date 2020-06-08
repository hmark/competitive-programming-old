def task(s, t):
    for i in range(0, len(s)):
        if s[i] != t[i]:
            print("No")
            return

    print("Yes")


s = input()
t = input()
task(s, t)
