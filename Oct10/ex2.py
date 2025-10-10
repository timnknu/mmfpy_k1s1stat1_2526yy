L = [1,2,15]
t = (L, 'hello', 128)
print(t, id(t))

t[0].append(-127)
print(t, id(t))