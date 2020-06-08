class EllysPalMulDiv2:
    def getMin(self, X):
        for i in range(1, 1001):
            total = i * X
            if str(total) == str(total)[::-1]:
                return i

        return -1


print(EllysPalMulDiv2().getMin(42))
print(EllysPalMulDiv2().getMin(121))
print(EllysPalMulDiv2().getMin(1337))
print(EllysPalMulDiv2().getMin(13))
print(EllysPalMulDiv2().getMin(100))
print(EllysPalMulDiv2().getMin(39325))
