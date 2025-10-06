lst = [1, 12, -8, 127, 15, 24, -1]

new_list = []

for e in lst:
    if e >= 0:
        print("Цей елемент НЕвід'ємний:", e)
        new_list.append(e + 2)
    else:
        print("Цей елемент від'ємний:", e)
        new_list.append(e)
print("Початковий список", lst)
print("Новий список:", new_list)