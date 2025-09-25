i = 0
sum_of_selected = 0
while True:
    a = int(input())
    if a == 0:
        break
    if a%2 == 1:
        # число непарне
        i += 1  # i = i + 1
        sum_of_selected += a
print(f'Number of non-zero values: {i}, and sum is {sum_of_selected}')