
with open('inp1.txt') as f:
    M = []
    for line in f:
        line_cleaned = line.rstrip('\r\n')
        vals = [float(elem) for elem in line_cleaned.split()]
        M.append(vals)
    print(M)
#

# обробка (транспонування матриці)

# запис вже транспонованої матриці у новий текстовий файл