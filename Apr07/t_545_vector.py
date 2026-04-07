import copy

class Vector:
    def __init__(self, lst):
        self._elems = copy.copy(lst)
    def __str__(self):
        #estr = [str(e) for e in self._elems]
        estr = map(str, self._elems)
        s = ', '.join(estr)
        return f"Vec ({s})"
    def __add__(self, other):
        # assert len(self._elems) == len(other._elems):
        if len(self._elems) != len(other._elems):
            raise ValueError("Вектори мають мати однакову кількість елементів")
        #
        new_elems = []
        for i in range(len(self._elems)):
            c = self._elems[i] + other._elems[i]
            new_elems.append(c)
        # for a,b in zip(self._elems, other._elems):
        #     new_elems.append(a+b)
        new_vec = Vector(new_elems)
        return new_vec


a = Vector([1,2,3])
b = Vector([100, 500, 800])
print(a)
print(b)
print(a + b)



