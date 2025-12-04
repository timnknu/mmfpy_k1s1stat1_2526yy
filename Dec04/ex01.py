L = [32, 15, 8, 1, 10, 100, 500]
   #  0   1  2  3  4    5   6
j = 3

# b = L[0:j] + L[j+1:]
# b.insert(0, L[j])
# print(b)
print([ L[j] ] + L[0:j] + L[j+1:])