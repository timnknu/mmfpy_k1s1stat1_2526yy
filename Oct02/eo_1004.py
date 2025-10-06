n = 197564
base = 10
digits = []
while n > 0:
    d = n % base
    #print(d)
    digits.insert(0, d)
    n = n // base # або n //= base
print(digits)

L1 = [digits[-1]]
print("Список із лише останнього елемента", L1)
L2 = digits[:-1]
print("Зріз до останнього елемента НЕВКЛЮЧНО", L2)
digits = L1 + L2

print(digits)
