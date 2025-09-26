n = 178

# 1 <= d <= n
for d in range(1, n+1):
    if n%d == 0:
        print(f'число {n} ділиться на {d}')