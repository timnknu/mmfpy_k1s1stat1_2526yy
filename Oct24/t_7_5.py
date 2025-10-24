# функція, яка перетворює число з десяткової системи у двійкове представлення
def dec_to_bin(n): # n - задане число у десятковій системі
    base = 2
    digits = []
    while n > 0:
        d = n % base
        #print(d)
        digits.insert(0, d)
        n = n // base # або n //= base
    return digits


# y = dec_to_bin(13)
# print('-------------')
# print(f"{y=}")

# функція, яка перетворює список цифр числа у двійковій системі у число в десятковій системі
def bin_to_dec(digits): # digits -- список цифр числа у двійковій системі (0-й елемент списку -- найстарша цифра)
    base = 2
    s = 0
    for j, elem in enumerate(digits):
        t = elem * base**(len(digits) - 1 - j)
        s = s + t
    return s

# print(bin_to_dec([1,0,0,1]))

# функція, яка перетворює рядкове представлення числа в двійковій системі у список його цифр
def strbin_to_bin(s):
    res = []
    for ch in s:
        # if ch=='0':
        #     res.append(0)
        # else:
        #     res.append(1)
        res.append(int(ch))
    return res

#print(strbin_to_bin("100010111"))

#--------------------------------
# a = input("Введіть перше число у двійковій системі")
# b = input("Введіть друге число у двійковій системі")
a = "101"
b = "100"

decA = bin_to_dec(strbin_to_bin(a))
decB = bin_to_dec(strbin_to_bin(b))
#print(decA, decB)
sm = decA + decB
#print(*dec_to_bin(sm), sep="")
L = dec_to_bin(sm)
R =  "".join([str(elem) for elem in L])
print(R)