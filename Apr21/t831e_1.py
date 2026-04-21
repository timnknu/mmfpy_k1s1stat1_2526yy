import math

N = 1000

x = 30
an = x
y = an
for n in range(1, N+1):
    an = an * (-x**2/(2*n+1)/2/n)
    #print(n, an)
    y = y + an
print(y)
print(math.sin(x))
