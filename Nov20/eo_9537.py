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
print('Here is our original matrix')
for row in A:
    print('here is the row of A:', row)
print(A[2][1])
# r = A[0.....len(A)-1] == A[0...A_n_rows-1]
# r[0...len(r)-1s] == r[0...A_n_cols-1]
# =>
# A[0...A_n_rows-1][0...A_n_cols-1] <-> A[i][j]: 0<=i<=A_n_rows-1, 0<=j<=A_n_cols-1

# B[i][j] = A[j][i]
A_n_rows = len(A)
A_n_cols = len(A[0])
print(f"матриця має {A_n_rows} рядк(и/ів) та {A_n_cols} стопвці(в)")

B_n_rows = A_n_cols
B_n_cols = A_n_rows
# B[0...B_n_rows-1][0..B_n_cols-1]
# тепер в B[i][j] елемент матриці B треба записати A[j][i] елемент матриці A

# обробка (транспонування матриці)
B = []
for i in range(B_n_rows):
    # row = [0]*B_n_cols
    row = []
    for j in range(B_n_cols):
        row.append(0)
    B.append(row)

for i in range(B_n_rows):
    for j in range(B_n_cols):
        B[i][j] = A[j][i]

print(B)



# запис вже транспонованої матриці у новий текстовий файл