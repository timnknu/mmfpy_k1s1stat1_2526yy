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
    print(all_uniq_lengths)
    return M
#

file_name = 'inp1.txt'

try:
    A = read_matrix(file_name)
    print(A)
except FileNotFoundError:
    print("файл відсутній")
    if is_debigging:
        print(traceback.format_exc())
    print("та й таке...")