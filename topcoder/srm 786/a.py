class CutTheCube:
    def findWinner(self, L, B, H):
        LTurns = 0
        BTurns = 0
        HTurns = 0

        if L > 1:
            LTurns = L - 1
            if B > 1:
                B += (B - 1) * LTurns
            if H > 1:
                H += (H - 1) * LTurns
        if B > 1:
            BTurns = B - 1
            if H > 1:
                H += (H - 1) * BTurns
        if H > 1:
            HTurns = H - 1

        turns = LTurns + BTurns + HTurns

        if turns % 2 == 0:
            return 2
        else:
            return 1


print(CutTheCube().findWinner(1, 1, 1))
print(CutTheCube().findWinner(2, 1, 1))
print(CutTheCube().findWinner(2, 2, 1))
print(CutTheCube().findWinner(97931, 95210, 92383))
print(CutTheCube().findWinner(3, 1, 3))
print(CutTheCube().findWinner(2, 2, 2))
