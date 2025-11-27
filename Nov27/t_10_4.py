#import my_matrix_ops
from my_matrix_ops import determinant as det, transpose

row2 = [1, 2, 3]
row3 = [2, 3, 4]
row1 = [2, 1, 1]
A = [row1, row2, row3]
#A[0] = row2
print(det(A))

print(transpose(A))