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


class QuadraticEquation(LinearEquation):
    def __init__(self, coef_a, coef_b, coef_c):
        self.a = coef_a
        super().__init__(coef_b, coef_c)
    def solve(self):
        if self.a == 0:
            return super().solve()
        else:
            D = self.b**2 - 4 * self.a * self.c
            if D < 0:
                return tuple()
            elif abs(D) < 1e-12: # або можна було D==0, якщо ми впевнені, що D - ціле число
                x0 = -self.b / (2*self.a)
                return (x0, )
            else:
                x1 = (-self.b + D**0.5) / (2*self.a)
                x2 = (-self.b - D**0.5) / (2 * self.a)
                return (x1, x2)
#

class BiQuadraticEquation(QuadraticEquation):
    def __init__(self, coef_a, coef_b, coef_c):
        super().__init__(coef_a, coef_b, coef_c)
    def solve(self):
        qe_roots = super().solve()
        if isinstance(qe_roots, AllRealNumbers):
            return ALL_REAL_NUMBERS
        elif len(qe_roots)==0:
            return tuple()
        else:
            x_roots = []
            for t in qe_roots:
                if t >= 0:
                    x_roots.append(t**0.5)
            return tuple(x_roots)
    #


e = LinearEquation(1, -2)
e.print_roots()


e = QuadraticEquation(1, -3, 2)
e.print_roots()

e = BiQuadraticEquation(1, -3, 2)
print(e.solve())