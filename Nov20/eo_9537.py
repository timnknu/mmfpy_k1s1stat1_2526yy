f = open('inp1.txt')

M = []
for line in f:
    line_cleaned = line.rstrip('\r\n')
    vals = [float(elem) for elem in line_cleaned.split()]
    M.append(vals)
print(M)

f.close()

# обробка (транспонування матриці)

# запис вже транспонованої матриці у новий текстовий файл