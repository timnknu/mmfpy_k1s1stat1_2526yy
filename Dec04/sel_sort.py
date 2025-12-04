L = [32, 15, 8, 1, 10, 100, 500]
   #  0   1  2  3  4    5   6

# [32, 15, 8, 1, 10, 100, 500]
#             |
#  +----------+
#  v
# [1, 32, 15, 8, 10, 100, 500]
#     ~~~~~~~~|~~~~~~~~~~~~~~
#     +-------+
#     v
# [1, 8, 32, 15, 10, 100, 500]
#        ~~~~~~~~~|~~~~~~~~~~
#         +-------+ елемент, який ми переміщаємо -- це є L[j]
#         |                    частина списку L[j+1:], яка залишилася правіше від (після) L[j]-го
#         v            ________/
# [1, 8, 10, <32, 15>, 100, 500]    де <...> - це є L[iFrom:j]
#  ====      ~~~~~~~~~~~~~~~~~~
#   ^вже
#   відсортована
#   частина
#   списку
#  L[0:iFrom]
#
# ....
#                         ...
#                          ^ len()-1


def get_min_element_index(a, iFrom):
    """
    повертає індекс найменшого елемента зі списку a починаючи з iFrom
    :param a: вхідний список
    :param iFrom: індекс, починаючи з якого робити пошук
    :return: знайдений індекс найменшого елемента
    """
    min_candidate_index = iFrom
    for i in range(iFrom, len(a)):
        if a[i] < a[min_candidate_index]:
            min_candidate_index = i
    return min_candidate_index

# перевіримо
# print(get_min_element_index(L, 0))
# exit()


for iFrom in range(0, len(L)-1):
    j = get_min_element_index(L, iFrom)
    L[j], L[iFrom] = L[iFrom], L[j]
    print(f'{iFrom=}, {j=}, {L[j]=}, {L=}')

