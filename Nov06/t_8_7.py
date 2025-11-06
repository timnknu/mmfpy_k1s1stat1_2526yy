counters = [0, 0, 0, 0]

M = 3
total_printed = 0

def cubes_print(j):
    global total_printed
    for counters[j] in range(1, counters[j-1]+1):
        if j+1 < len(counters):
            cubes_print(j+1)
        else:
            print(counters, sum(counters))
            total_printed += 1

for counters[0] in range(1, M+1):
    cubes_print(1)

print(total_printed)