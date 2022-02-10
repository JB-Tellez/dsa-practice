def ugly_numbers(n):
    if n == 1:
        return 1

    # candidate = ugly_numbers(n-1)

    primes = get_primes(n)

    primes.remove(2)
    primes.remove(3)
    primes.remove(5)

    candidate = 1
    ctr = 0

    for candidate in range(1, n):
        if candidate % 2 == 0 or candidate % 3 == 0 or candidate % 5 == 0:
            # need to know if any other primes are a factor

            print(candidate)


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def get_primes(n):
    primes = set()
    for i in range(1, n):
        if i not in primes:
            if is_prime(i):
                primes.add(i)

    return primes


ugly_numbers(23)
