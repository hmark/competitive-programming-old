class EllysWhatDidYouGet:
    def getCount(self, N):
        total = 0
        for x in range(1, 51):
            for y in range(1, 51):
                for z in range(1, 51):
                    result = None
                    found = True
                    for i in range(1, N + 1):
                        digits = (i * x + y) * z
                        suma = 0
                        for digit in str(digits):
                            suma += int(digit)

                        if result == None:
                            result = suma
                        else:
                            if result != suma:
                                found = False
                                break

                    if found:
                        total += 1

        return total


print(EllysWhatDidYouGet().getCount(9))
print(EllysWhatDidYouGet().getCount(5))
print(EllysWhatDidYouGet().getCount(13))
print(EllysWhatDidYouGet().getCount(42))
