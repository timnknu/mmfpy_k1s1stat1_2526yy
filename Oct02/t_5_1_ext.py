n1 = 18
n2 = 27
lst = []
# заповнимо список остачами від ділення цілих чисел від n1 (включно) до n2 (включно) на 15

for n in range(n1, n2+1):
    lst.append(n % 15)
print("У нас сформувався такий список:", lst)


# якщо ми сюди потрапили, то в списку точно є хоча б один елемент => можна звертатися до списку по індексу [0]
max_candidate = lst[0]
for element in lst:
    if element > max_candidate:
        max_candidate = element
print(max_candidate)