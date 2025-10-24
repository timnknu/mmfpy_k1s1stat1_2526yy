#the_number = 17

def is_prime(the_number):
    result = True
    for d in range(2, the_number): # 2, 3, ..., n-1
        if the_number % d == 0:
            result = False
    return result
#

# the_number >= n
# the_number <= 2*n
# the_number+2 >= n         => the_number >= n-2
# the_number+2 <= 2*n       => the_number <= 2*n-2
#
# the_number >= n
# the_number <= 2*n-2

n = 150
for the_number in range(n, 2*n+1-2):
    if is_prime(the_number) and is_prime(the_number+2):
        print(the_number, the_number+2)
