
N = 7
counters = [0] * N

def cubes_print(j):
    for counters[j] in range(0, counters[j-1]+1):
    #for counters[j] in range(counters[j - 1] + 1):
        if j+1 < len(counters):
            cubes_print(j+1)
        else:
            if sum(counters) == N:
                for element in counters:
                    if element != 0:
                        print(element, end= ' ')
                    else:
                        break
                print()

for counters[0] in range(1, N+1):
    cubes_print(1)

