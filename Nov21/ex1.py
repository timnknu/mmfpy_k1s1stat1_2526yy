import traceback

is_debigging = True
#is_debigging = False

def read_matrix(file_name):
    all_uniq_lengths = set()
    with open(file_name) as f:
        M = []
        for line in f:
            line_cleaned = line.rstrip('\r\n')
            vals = [float(elem) for elem in line_cleaned.split()]
            M.append(vals)
            n_elems = len(vals)
            all_uniq_lengths.add(n_elems)
            #all_uniq_lengths = all_uniq_lengths | {n_elems}
    if len(all_uniq_lengths)==1:
        print("з матрицею все гаразд")
    else:
        print("різні рядки матриці мають різну кількість елементів")
        raise ValueError("некоректна структура матриці")
    return M
#

file_name = 'inp1.txt'

try:
    A = read_matrix(file_name)
    print(A)

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
        row = []
        for j in range(B_n_cols):
            row.append(A[j][i])
        B.append(row)

    print('Here is our transposed matrix')
    for row in B:
        print('here is the row of B:', row)

except FileNotFoundError:
    print("файл відсутній")
    if is_debigging:
        print(traceback.format_exc())
    print("та й таке...")
except ValueError: # !: кілька блоків except стосуються одного і того ж блоку try
    print("Сталася помилка ValueError")