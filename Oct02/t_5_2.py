lst = [1, 12, -8, 127, 15, 24, -1]

print(list(enumerate(lst)))

for i, e in enumerate(lst):
    if e >= 0:
        lst[i] = e + 2
        # але так теж робити не дуже добре
print(lst)
