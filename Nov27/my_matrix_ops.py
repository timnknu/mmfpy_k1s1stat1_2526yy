print(__name__)


def determinant(M):

    print("I'm about to compute determinant of", M)
    #if len(M)==2:
    #    return M[0][0]*M[1][1] - M[0][1]*M[1][0]
    if len(M)==1:
        return M[0][0]

    res = 0
    for i in range(len(M)):
        smaller_matrix = []
        for j in range(len(M)):
            if j != i:
                jth_row = M[j]
                smaller_matrix.append(jth_row[1:])
        #print(smaller_matrix)
        res += (-1)**i * M[i][0] * determinant(smaller_matrix)
    return res

def transpose(A):
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
        row = []
        for j in range(B_n_cols):
            row.append(A[j][i])
        B.append(row)

    print('Here is our transposed matrix')
    for row in B:
        print('here is the row of B:', row)
    return B



if __name__ == "__main__":

    row1 = [1, 2, 3]
    row2 = [2, 3, 4]
    row3 = [2, 1, 1]
    print(row1, row2, row3)
    A = [row1, row2, row3]
    # A[2] == row3
    print(A)
    d = determinant(A)
    print(d)

    # ---------------

    print('-'*80)
    row1 = [1, 2, 3, 10]
    row2 = [2, 3, 4, 11]
    row3 = [2, 1, 1, 12]
    row4 = [-5, -8, 11, 12]
    A = [row1, row2, row3, row4]
    print(A)
    d = determinant(A)
    print(d)
    import numpy as np
    print(np.linalg.det(np.array(A)))
    del A


    row1 = [1, 2, 3]
    row2 = [2, 3, 4]
    row3 = [2, 1, 1]
    my_matrix = [row1, row2, row3]

    #try:
    print(transpose(my_matrix))
    #except:
    #    print('ERROR')