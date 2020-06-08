class SmallestRegular:
    def findLexSmallest(self, S):
        swaps = []
        a = -1
        b = -1
        c = -1
        repeat = True
        while repeat:
            repeat = False
            # print(S)
            for i in range(0, len(S)):
                if S[i] == '(':
                    if a == -1:
                        continue
                    elif b == -1:
                        b = i - 1
                    else:
                        continue
                elif S[i] == ')':
                    if a == -1:
                        a = i
                    elif b == -1:
                        continue
                    elif c == -1:
                        c = i - 1
                        S = S[0:a] + S[b + 1:c + 1] + S[a:b + 1] + S[c+1:]
                        swaps.append(a)
                        swaps.append(b)
                        swaps.append(c)
                        a = -1
                        b = -1
                        c = -1
                        repeat = True
                        break
        return tuple(swaps)


# print(SmallestRegular().findLexSmallest('(())'))
# print(SmallestRegular().findLexSmallest("(()())"))
# print(SmallestRegular().findLexSmallest("()()()()"))
# print(SmallestRegular().findLexSmallest("((())((()((())))))(())()"))
