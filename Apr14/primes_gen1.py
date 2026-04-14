def get_primes(max_n):
    known_primes = []

    for candidate in range(2, max_n):
        is_prime = True
        for d in known_primes :
            if candidate % d == 0:
                is_prime = False
                break
            if d > candidate**0.5:
                break
        if is_prime:
            known_primes.append(candidate)
    return known_primes

L1 = get_primes(100)
L2 = get_primes(100)
for i in range(len(L1)-1):
    if L1[i+1] - L2[i] == 2:
        print(L1[i+1], L2[i])