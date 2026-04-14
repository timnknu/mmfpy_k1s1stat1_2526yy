class MySource:
    def __init__(self):
        self._idx = 0
        self._letters = 'abcdef'
    def __next__(self):
        if self._idx >= len(self._letters):
            raise StopIteration
        c = self._letters[self._idx]
        self._idx += 1
        return c
    def __iter__(self):
        return self


obj = MySource()

for e in obj:
    print(e)
    for J in obj:
        print('...', J)