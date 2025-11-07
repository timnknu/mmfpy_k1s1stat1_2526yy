s = "-2 3 3 -3 -4 0 2 -3 -4 3"
L = [int(x) for x in s.split()]
print(L, len(L))
uniq_elements = set(L)
print(uniq_elements, len(uniq_elements))

positions = {} # елемнт -> список індексів, на яких він є в початковому списку
for elem in uniq_elements:
    ps = []
    for j, e in enumerate(L):
        if e==elem:
            ps.append(j)
    #print(elem, ps)
    positions[elem] = ps
#
print(positions)
filtered_positions = {}
print(f"{'key':10s} max(values)")
for x,y in positions.items():
    if len(y)>1:
        print(f"{str(x):10s} {max(y)} <- {y}")
        filtered_positions[x] = max(y)
print(filtered_positions.items())
def my_sorting_criteria(t):
    return t[1]
print(sorted(filtered_positions.items(), key=my_sorting_criteria))
