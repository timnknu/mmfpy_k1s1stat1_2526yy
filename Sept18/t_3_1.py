a = 30
b = 8
a, b = [int(x) for x in input().split()]
# оптимізуємо: зробимо так, щоб завжди було a<b (навіть якщо користувач ввів навпаки)
if a > b:
    # поміняємо значення в цих змінних місцями
    tmp = a
    a = b
    b = tmp
    # специфічний для Python варіант того самого: a,b=b,a
    print("a and b swapped!")
# накопичити у the_sum суму доданків, кожен з яких рівний b, а кількість доданків рівна a
i = 0
the_sum = 0
while i < a :
    the_sum = the_sum + b
    #print(b)
    i = i + 1
print("Result is:", the_sum)
print("done!")