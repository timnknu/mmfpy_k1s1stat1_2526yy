n = int(input())
lst_elements = input()
print("кількість елементів:", n)
print("другий рядок:", lst_elements)
print("другий рядок та .split():", lst_elements.split())

lst = []
for e in lst_elements.split():
    print("черговий елемент:", e)
    lst.append(int(e))
print("Сформований список lst:", lst)

if n != len(lst):
    print("Ой, а в списку то не та кількість елементів, яку обіцяли!")

if len(lst)==0:
    print("елементів немає!")
else:
    # якщо ми сюди потрапили, то в списку точно є хоча б один елемент => можна звертатися до списку по індексу [0]
    max_candidate = lst[0]
    for element in lst:
        if element > max_candidate:
            max_candidate = element
    print(max_candidate)