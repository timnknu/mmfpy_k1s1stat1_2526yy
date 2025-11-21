import traceback

is_debigging = True
#is_debigging = False

def read_matrix(file_name):
    with open(file_name) as f:
        M = []
        for line in f:
            line_cleaned = line.rstrip('\r\n')
            vals = [float(elem) for elem in line_cleaned.split()]
            M.append(vals)
    return M
#

file_name = 'file_name'

try:
    A = read_matrix(file_name)
    print(A)
except FileNotFoundError:
    print("файл відсутній")
    if is_debigging:
        print(traceback.format_exc())
    print("та й таке...")