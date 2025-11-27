import sys

sys.path.append('/home/tniko/tmp/MECHMAT/2025-2026_1курс/repo')
print('path:')
for i, p in enumerate(sys.path):
    print(f'FOLDER {i}: {p}')
print('----------------------')

import Oct31Nov3.t_10_5


row2 = [1, 2, 3]
row3 = [2, 3, 4]
row1 = [2, 1, 1]
A = [row1, row2, row3]


Oct31Nov3.t_10_5.determinant(A)