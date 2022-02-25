import random
from Cryptography import cryptomath

first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]


def get_best_choice(bitlength):

    while True:
        
        prime_choice = random.randrange(2 ** (bitlength - 1) + 1, 2 ** bitlength - 1)

        for divisor in first_primes_list:
            if prime_choice % divisor == 0:
                break
        else:
            return prime_choice


def is_millar_rabin_passed(prime_choice):

    r = prime_choice - 1
    max_division_by_two = 0

    while r % 2 == 0:
        
        r >>= 1  
        max_division_by_two += 1
    assert (2 ** max_division_by_two * r == prime_choice - 1)  

    def is_composite(number):

        if pow(number, r, prime_choice) == 1:
            return False

        for i in range(max_division_by_two):
            if pow(number, 2 ** i * r, prime_choice) == (prime_choice - 1):
                return False

        return True

    no_of_iteration = 20
    for _ in range(no_of_iteration):
        tester = random.randrange(2, prime_choice - 2)  
        if is_composite(tester):
            return False

    return True


def generate_prime_number():

    while True:
        bitlength = 1024
        prime_choice = get_best_choice(bitlength)

        if not is_millar_rabin_passed(prime_choice):
            continue
        else:
            return prime_choice


def generate_key_pair():

    p = generate_prime_number()
    q = generate_prime_number()

    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randrange(1, phi)
        if cryptomath.gcd(e, phi) == 1:
            break

    d = cryptomath.mod_inverse(e, phi)

    return (e, n), (d, n)
