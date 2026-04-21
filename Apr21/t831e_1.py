import math

def sg(x):
    an = x
    yield x
    n = 1
    while True:
        an = an * (-x**2/(2*n+1)/2/n)
        yield an
        n += 1


eps = 1e-5  # 10**(-5) = 0.00001
y = 0
x = 12.0
for term in sg(x):
    y += term
    print( ':', term, y)
    if abs(term) < eps:
        break
print(y)
print(math.sin(x))