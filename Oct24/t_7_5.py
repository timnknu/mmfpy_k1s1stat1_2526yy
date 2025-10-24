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


y = dec_to_bin(17)
print('-------------')
print(f"{y=}")

def bin_to_dec(digits):
    base = 2
    s = 0
    for j, elem in enumerate(digits):
        t = elem * base**(len(digits) - 1 - j)
        s = s + t
    return s

print(bin_to_dec([1,0,0,1]))