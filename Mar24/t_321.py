class AllRealNumbers:
    def __str__(self):
        return 'GOOD!!!'

ALL_REAL_NUMBERS = AllRealNumbers()

class LinearEquation:
    def __init__(self, coef_b, coef_c):
        self.b = coef_b
        self.c = coef_c

    def solve(self):
        if self.b != 0:
            x = -self.c / self.b
            return (x,)
        else:
            # b==0
            if self.c != 0:
                return tuple()
            else:
                return ALL_REAL_NUMBERS

x1 = ALL_REAL_NUMBERS
x2 = (1, 2)

print(x1)
print(x2)

