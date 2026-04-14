import copy

class Vector:
    def __init__(self, lst):
        self._elems = copy.deepcopy(lst)
    def __str__(self):
        #estr = [str(e) for e in self._elems]
        #estr = map(str, self._elems)
        #s = ', '.join(estr)
        s = ''
        for e in self._elems:
            s = s + str(e) + "; "
        return f"Vec ({s})"
    def __add__(self, other):
        if isinstance(other, (float, int)):
            # other -- число
            new_elems = []
            for i in range(len(self._elems)):
                c = self[i] + other
                new_elems.append(c)
            new_vec = Vector(new_elems)
            return new_vec
        elif isinstance(other, Vector):
            # assert len(self._elems) == len(other._elems):
            if len(self) != len(other):
                raise ValueError("Вектори мають мати однакову кількість елементів")
            #
            new_elems = []
            for i in range(len(self)):
                c = self[i] + other[i]
                new_elems.append(c)
            # for a,b in zip(self._elems, other._elems):
            #     new_elems.append(a+b)
            new_vec = Vector(new_elems)
            return new_vec
        else:
            raise ValueError("Невідомий тип доданка")
    def __radd__(self, other):
        #return self.__add__(other)
        return self + other
    def __getitem__(self, item):
        return self._elems[item]
    def __setitem__(self, key, value):
        self._elems[key] = value
    def __len__(self):
        return len(self._elems)


row1 = Vector([1,2,3])
row2 = Vector([50,60,70])
a = Vector([row1, row2])

print(a)

row3 = Vector([10,20,30])
row4 = Vector([5,6,7])
b = Vector([row3, row4])

print(a + b)
