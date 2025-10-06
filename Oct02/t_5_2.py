lst = [1, 12, -8, 127, 15, 24, -1]

print(list(enumerate(lst)))

for i, e in enumerate(lst):
    print(f"Індекс {i}, а відповідний елемент списка: {e}, і він рівний {lst[i]}")


# num_elements = len(lst)
# print("Загалом у нас є", num_elements)
# for i in range(num_elements):
#     print(f"же елемент, отриманий за індексом {i} рівний", lst[i])
#     if lst[i] >= 0:
#         lst[i] = lst[i] + 2
# print(lst)
