import math
#x1, y1, x2, y2, x3, y3 = [float(d) for d in input().split()]
x1, y1, x2, y2, x3, y3 = 3, 2, 7, 6.5, 10, 1
a = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
b = math.sqrt( (x3-x2)**2 + (y3-y2)**2 )
c = math.sqrt( (x3-x1)**2 + (y3-y1)**2 )
#print(a, b, c)
p = a + b + c
print(f"Perimeter p={p:.5f}, a={a}, b={b:.2e}")