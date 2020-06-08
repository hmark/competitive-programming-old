import math


class EllysConjectureDiv2:
    def getSum(self, L, R):
        total = 0
        if L <= 1:
            total += 3
            L = 3
        elif L <= 2:
            total += 1
            L = 3

        if R <= 2:
            return total

        if (L % 3) == 0:
            LF = L
        elif ((L + 1) % 3) == 0:
            LF = L + 1
        elif ((L + 2) % 3) == 0:
            LF = L + 2

        total += (LF - L) * 4

        threes = math.ceil(float(R - LF + 1) / 3)
        total += 6 * threes
        total += 4 * ((R - LF + 1) - threes)

        return total


print(EllysConjectureDiv2().getSum(13, 17))
print(EllysConjectureDiv2().getSum(42, 1337))
print(EllysConjectureDiv2().getSum(12345, 67890))
print(EllysConjectureDiv2().getSum(42666, 133742))
print(EllysConjectureDiv2().getSum(123456789, 987654321))
