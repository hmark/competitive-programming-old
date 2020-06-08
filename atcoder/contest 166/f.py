def task(n, a, b, c, s):
    choices = []

    for i in range(0, n):
        seta = 'A' in s[i]
        setb = 'B' in s[i]
        setc = 'C' in s[i]

        picka = seta
        pickb = setb
        pickc = setc

        if seta and a - 1 < 0:
            pickb = False
            pickc = False

        if setb and b - 1 < 0:
            picka = False
            pickc = False

        if setc and c - 1 < 0:
            picka = False
            pickb = False

        nextseta = True
        nextsetb = True
        nextsetc = True

        if i < n - 1:
            nextseta = 'A' in s[i + 1]
            nextsetb = 'B' in s[i + 1]
            nextsetc = 'C' in s[i + 1]

        if picka and nextseta:
            pickb = False
            pickc = False
        elif pickb and nextsetb:
            picka = False
            pickc = False
        elif pickc and nextsetc:
            picka = False
            pickb = False

        if seta and picka:
            choices.append('A')
            a += 1
            if setb:
                b -= 1
            if setc:
                c -= 1
        elif setb and pickb:
            choices.append('B')
            b += 1
            if seta:
                a -= 1
            if setc:
                c -= 1
        elif setc and pickc:
            choices.append('C')
            c += 1
            if seta:
                a -= 1
            if setb:
                b -= 1
        else:
            print('No')
            return

    print('Yes')
    for choice in choices:
        print(choice)


n, a, b, c = map(int, input().split())
s = []
for i in range(0, n):
    s.append(input())

task(n, a, b, c, s)
