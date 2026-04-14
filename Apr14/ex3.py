class MyIterator:
    def __next__(self):
        return 12

class MySource:
    def __iter__(self):
        finger = MyIterator()
        return finger


obj = MySource()

for e in obj:
    print(e)