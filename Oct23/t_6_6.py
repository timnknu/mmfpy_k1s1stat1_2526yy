def is_letter(symb):
    if symb>='a' and symb <= 'z':
        return True
    if symb >= '0' and symb <= '9':
        return True
    if symb >= 'A' and symb <= 'Z':
        return True
    return False
#
# print(is_letter('5'))
# print(is_letter('b'))
# print(is_letter('!'))

def my_split(s):
    W = []  # тут має бути список слів із рядка s,
    # де під "словом" мається на увазі частина рядка,
    # яка відділена від інших частин хоча б одним пробілом
    # наш аналог функції .split()
    current_word = ""
    for ch in s:
        if is_letter(ch):
            current_word = current_word + ch
        else:
            if current_word != "":
                W.append(current_word)
            current_word = ""
    if current_word != "":
        W.append(current_word)

    return W

print(my_split("Hello, wo6y46545HJVJTC!Rrld"))