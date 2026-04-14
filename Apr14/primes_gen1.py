def get_primes():
    known_primes = []

    candidate = 2
    while True:
        is_prime = True
        for d in known_primes :
            if candidate % d == 0:
                is_prime = False
                break
            if d > candidate**0.5:
                break
        if is_prime:
            yield candidate
            known_primes.append(candidate)
        candidate += 1

# основна програма:
for e in get_primes():
    print('-----')
    print(e)
    print('******')
    if e > 1000:
        break