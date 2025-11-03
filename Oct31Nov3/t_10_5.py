def determinant(M):
    global rec_cut_cntr

    print("I'm about to compute determinant of", M)
    #if len(M)==2:
    #    return M[0][0]*M[1][1] - M[0][1]*M[1][0]
    if len(M)==1:
        rec_cut_cntr += 1
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


row1 = [1, 2, 3]
row2 = [2, 3, 4]
row3 = [2, 1, 1]
print(row1, row2, row3)
A = [row1, row2, row3]
# A[2] == row3
print(A)
rec_cut_cntr = 0
d = determinant(A)
print(d)
print(rec_cut_cntr)

# ---------------

print('-'*80)
row1 = [1, 2, 3, 10]
row2 = [2, 3, 4, 11]
row3 = [2, 1, 1, 12]
row4 = [-5, -8, 11, 12]
A = [row1, row2, row3, row4]
print(A)
rec_cut_cntr = 0
d = determinant(A)
print(d)
print(f'{rec_cut_cntr=}')
import numpy as np
print(np.linalg.det(np.array(A)))
