def read_matrix_from_file(file_name):
    with open(file_name) as f:
        M = []
        for line in f:
            line_cleaned = line.rstrip('\r\n')
            vals = [float(elem) for elem in line_cleaned.split()]
            M.append(vals)
    return M
#

A = read_matrix_from_file('inp1.txt')
print(A)


# обробка (транспонування матриці)

# запис вже транспонованої матриці у новий текстовий файл