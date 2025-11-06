M = 6 # максимальне число, яке наявне на кубику
for i1 in range(1, M+1):
    for i2 in range(1, M + 1):
        for i3 in range(1, M + 1):
            print(i1, i2, i3)


counters = [0, 0, 0]
for counters[0] in range(1, M+1):
    for counters[1] in range(1, M + 1):
        for counters[2] in range(1, M + 1):
            print(*counters)


