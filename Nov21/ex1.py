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
    assert len(all_uniq_lengths)==1, "поорушилося припущення про те, що в усіх рядках однакова кількість елементів"
    return M
#

file_name = 'inp1.txt'
try:
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
        print("1/0" , 1/0)
    except ValueError: # !: кілька блоків except стосуються одного і того ж блоку try
        print("Сталася помилка ValueError")
    except AssertionError as e:
        print("не виконалося припущення, на яке покладалася наша програма!")
        print("e=",e)
    finally:
        print("Ця частина виконається незалежно від того, була помилка, чи ні")
except:
    print("сталася помилка під час обробки помилки...")
    print(traceback.format_exc())
