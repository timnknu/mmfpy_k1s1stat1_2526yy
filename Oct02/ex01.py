# знайти мінімальне з введених користувачем чисел, аж допоки користувач не введе 0

this_is_first_number = True
the_lowest = 0
while True:
    n = int(input())
    if n==0:
        break
    if this_is_first_number:
        the_lowest = n
    else:
        if n < the_lowest:
            the_lowest = n
    this_is_first_number = False
print(the_lowest)


# Вправа: модифікувати цю програму так, щоб вона обчислювала
# max_i ( a_i - min_j<i(a_j)), де {a_i} -- введені користувачем числа
