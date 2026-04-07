class Vector:
    def __init__(self, lst):
        self._elems = lst
    def __str__(self):
        #estr = [str(e) for e in self._elems]
        estr = map(str, self._elems)
        s = ', '.join(estr)
        return f"Vec ({s})"

obj = Vector([1,2,3])
print(obj)

# s = 'xyz'.join(['ABC', 'FGI', 'KKKKKK'])
# print(s)