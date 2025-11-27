#import my_matrix_ops
from my_matrix_ops import determinant as det, transpose

row2 = [1, 2, 3]
row3 = [2, 3, 4]
row1 = [2, 1, 1]
A = [row1, row2, row3]
#A[0] = row2
print(det(A))

b = [-1, -2, 15]

x = []
for i in range(len(b)):
    A_transposed = transpose(A)
    A_transposed[i] = b
    #A_with_b_at_i = transpose(A_transposed)
    #sol_i = det(A_with_b_at_i) / det(A)
    sol_i = det(A_transposed) / det(A)
    print(f'{i}-th variable:', sol_i)
    x.append(sol_i)
print(x)

row = A[2]
res = 0
for i in range(len(b)):
    res += row[i] * x[i]
print(res)
