text = '''    Dear       friends,
декілька        пропусків розміщені між двома словами (простіше
кажучи, якщо     слова розділені більш         ніж одним пропуском, тоді усі
пропуски крім одного - зайві)
Let me ...   '''

s = "This  is a simple test"
#s= ""

def my_split(s):
    W = []  # тут має бути список слів із рядка s,
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

    return W

lstw = my_split(text)
print("List of words:", lstw)

# наш аналог функції .join()
res = ""
# for elem in W[:-1]:
#     res = res + elem + " "
# if len(W)>0:
#     res = res + W[-1]
for i, elem in enumerate(lstw):
    if i == len(lstw)-1:
        res = res + elem
    else:
        res = res + elem + " "
print(f'#{res}#')