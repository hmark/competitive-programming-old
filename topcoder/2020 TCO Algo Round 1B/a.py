class EllysCandies:
    def getWinner(self, boxes):
        boxes = list(boxes)
        elliesTurn = True
        e = 0
        k = 0
        boxes.sort()

        suma = 0
        for box in reversed(boxes):
            if elliesTurn:
                e += box + suma
            else:
                k += box + suma

            suma += box
            elliesTurn = not elliesTurn

        if e > k:
            return "Elly"
        elif e < k:
            return "Kris"
        else:
            return "Draw"


print(EllysCandies().getWinner([4, 2]))
print(EllysCandies().getWinner([1, 1, 1000]))
print(EllysCandies().getWinner([42, 42, 42, 42, 42, 42, 42, 42]))
print(EllysCandies().getWinner([42, 13, 17, 666, 55, 100, 3, 20, 81, 42, 123]))
