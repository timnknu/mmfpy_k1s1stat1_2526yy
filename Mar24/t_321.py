import math

class AllRealNumbers:
    def __str__(self):
        return 'infinite number of solutions - all real numbers'

# "константа", яка відповідає "всі дійсні числа"
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
    #
    def print_roots(self):
        print(self.solve())
    #
    def number_of_root(self): # повертає кількість розв'язків
        s = self.solve()
        if isinstance(s, tuple):
            return len(s)
        else:
            return math.inf # використали "вбудовану" константу для +infinity


class