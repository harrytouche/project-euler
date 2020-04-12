"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


n_primes = 10001

primes = [2, 3, 5]
a = 6

while len(primes) < n_primes:

    # loop over primes
    for prime in primes:

        # if there is a zero remainder, must be a factor
        if not a % prime:
            break

        # if not broken after last prime, new prime
        if prime == primes[-1]:
            print("new prime found: {}".format(a))
            primes.append(a)

    a += 1

print(primes[-1])
