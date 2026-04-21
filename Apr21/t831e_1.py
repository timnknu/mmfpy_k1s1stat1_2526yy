import math

N = 1000
eps = 1e-5 # 10**(-5) = 0.00001
x = 10
an = x
y = an
n = 1
while True:
    an = an * (-x**2/(2*n+1)/2/n)
    y = y + an
    print(n, ':', an, y)
    if abs(an) < eps:
        break
    n += 1
print(y)
print(math.sin(x))
