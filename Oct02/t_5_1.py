lst = [1, 15, -8, 88, 21, 53.7]

if len(lst)==0:
    print("елементів немає!")
else:
    # якщо ми сюди потрапили, то в списку точно є хоча б один елемент => можна звертатися до списку по індексу [0]
    max_candidate = lst[0]
    for element in lst:
        if element > max_candidate:
            max_candidate = element
    print(max_candidate)