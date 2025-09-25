i = 0
sum_of_selected = 0
while True:
    a = int(input())
    if a == 0:
        break
    # пропустити подальшу частину блока коду, якщо число парне (і, відповідно, виконати її, якщо воно непарне)
    if a%2 == 0:
        continue
    # якщо програма вже добралася до цього рядочка, значить число було непарним
    # число непарне
    i += 1  # i = i + 1
    sum_of_selected += a
print(f'Number of non-zero values: {i}, and sum is {sum_of_selected}')