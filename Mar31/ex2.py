class C:
    def __init__(self, x):
        self._x = x
    def show(self):
        print('Hello:', self._x)


obj = C(12)

obj.show()

print(isinstance(obj, C))
print(isinstance(obj, int))
print(type(obj))

print('----')

print(isinstance(obj._x, C))
print(isinstance(obj._x, int))
print(type(obj._x))

print('----')

print(hasattr(obj, '_x'))