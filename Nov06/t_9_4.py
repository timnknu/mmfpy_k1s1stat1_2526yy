#print(set([1,1,1, 2]))

s = "-2 3 3 -3 -4 0 2 -3 -4 3 -2 -2 -2 -2"
L = [int(x) for x in s.split()]
print(L, len(L))
uniq_elements = set(L)
print(uniq_elements, len(uniq_elements))
counts = {} # або counts = dict()
for elem in uniq_elements:
    print(elem, L.count(elem))
