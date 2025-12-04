L = [32, 15, 8, 500, 1, 10, 100]
   #  0   1  2  3    4   5   6

# [32, 15, 8, 500, 1, 10, 100]

# Злиття двох списків в один "в порядку зростання"
# [ <32 >, 15, 8, 500]
# [ <1 >, 10, 100]
#    |
# [ 1 ]
#
# [ <32 >, 15, 8, 500]
# [ <10>, 100]
#
# [ 1 ]
#
# [ <32 >, 15, 8, 500]
# [ <100>]
#
# [ 1, 10, 32 ]
#
# [ <15>, 8, 500]
# [ <100>]
#
# [ 1, 10, 32 ]
#
# [ <8>, 500]
# [ <100>]
#
# [ 1, 10, 32, 15 ]
#
# [ <500>]
# [ <100>]
#
# [ 1, 10, 32, 15, 8 ]
#
# [ <500>]
# [ ]
#
# [ 1, 10, 32, 15, 8, 100 ]
#
# [ ]
# [ ]
#
# [ 1, 10, 32, 15, 8, 100, 500 ]
#

def merge_two_lists(A, B):
    i = 0
    j = 0
    res = []
    while i<len(A) and j<len(B):
        if A[i] < B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
    # "запускаємо в кімнату" всю частину "черги" A, яка ще лишалася "під дверима"
    while i<len(A):
        res.append(A[i])
        i += 1
    # "запускаємо в кімнату" всю частину "черги" B, яка ще лишалася "під дверима"
    while j<len(B):
        res.append(B[j])
        j += 1
    print('Ми змішуємо:', A, B, '-->', res)
    return res
# test:
#print(merge_two_lists([32, 15, 8, 500], [1, 10, 100]))

def merge_sort(L):
    if len(L)<=1:
        return L
    left_part = L[:len(L)//2]
    right_part = L[len(L) // 2:]
    return merge_two_lists(merge_sort(left_part), merge_sort(right_part))

print(merge_sort(L))