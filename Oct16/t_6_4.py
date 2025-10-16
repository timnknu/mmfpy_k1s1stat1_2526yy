s = '''    Dear       friends,
декілька        пропусків розміщені між двома словами (простіше
кажучи, якщо     слова розділені більш         ніж одним пропуском, тоді усі
пропуски крім одного - зайві)
Let me ...   '''

s = "This  is a simple test"
#s= ""

W = [] # тут має бути список слів із рядка s,
# де під "словом" мається на увазі частина рядка,
# яка відділена від інших частин хоча б одним пробілом

# наш аналог функції .split()
separators = [" ", "\n", ","]
current_word = ""
for ch in s:
    if ch not in separators:
        current_word = current_word + ch
    else:
        if current_word != "":
            W.append(current_word)
        current_word = ""
if current_word != "":
    W.append(current_word)

print("List of words:", W)

# наш аналог функції .join()
res = ""
# for elem in W[:-1]:
#     res = res + elem + " "
# if len(W)>0:
#     res = res + W[-1]
for i, elem in enumerate(W):
    if i == len(W)-1:
        res = res + elem
    else:
        res = res + elem + " "
print(f'#{res}#')