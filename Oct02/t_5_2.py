lst = [1, 12, -8, 127, 15, 24, -1]

for e in lst:
    if e >= 0:
        print("Цей елемент НЕвід'ємний:", e)
        e = e + 2
    else:
        print("Цей елемент від'ємний:", e)
print(lst)