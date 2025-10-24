# функція, яка перетворює число з десяткової системи у представлення в іншій системі числення
def dec_to_other(n, base): # n - задане число у десятковій системі, base - основа нової системи числення
    res = ""
    while n > 0:
        d = n % base
        #print(d)
        if d >= 0 and d<=9:
            d_str = str(d)
        else:
            d_str = chr(ord('A') + d - 10)
        res = d_str + res
        #print(d_str, ">>", res)
        n = n // base # або n //= base
    return res


print(dec_to_other(255123, 16))