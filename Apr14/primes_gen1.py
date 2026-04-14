
primes = []

candidate = 17
is_prime = True
for d in range(2, int(candidate**0.5 + 1)) :
    if candidate % d == 0:
        is_prime = False
        break
print(is_prime)