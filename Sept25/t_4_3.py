i = 0
sum_nums = 0
while True:
    a = int(input())
    if a == 0:
        break
    i += 1  # i = i + 1
    sum_nums += a
print(f'Number of non-zero values: {i}, and their sum: {sum_nums}')