def task(t):
    ans = []
    for i in range(0, len(t)):
        if t[i] == "D" or t[i] == "P":
            ans.append(t[i])
        else:
            ans.append("D")

    print("".join(ans))


t = input()
task(t)
