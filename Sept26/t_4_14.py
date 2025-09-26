n = 17

# 1 < d <= n -- для задачі 4.5
for d in range(2, n+1):
    if n%d == 0:
        print(f'число {n} ділиться на {d}')
        break
print('Готово!')