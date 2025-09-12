import math
a, b, c = 1.0, -5.0, 6.0
D = b**2 - 4*a*c
if D > 0:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(f"Two roots: {x2} {x1}")
else:
    if abs(D) < 1e-12:
        x = (-b) / (2 * a)
        print(f"One root: {x}")
    else:
        print("No roots")