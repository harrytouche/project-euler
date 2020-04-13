"""
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. 
However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""

import math
from tqdm import tqdm
import numpy as np


def n_consecutive_primes(a, b):
    n_reached = 0
    is_prime = True

    while is_prime:

        # create formula
        candidate = n_reached ** 2 + a * n_reached + b

        # check if prime
        if is_prime_number(candidate):

            n_reached += 1

        # otherwise output
        else:
            is_prime = False

    return n_reached


def is_prime_number(number):

    if number <= 1:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):

        if number % i == 0:
            # print("{} is a factor of {}".format(i, number))
            return False

    # print("{} is a prime number!".format(number))
    return True


a_max = 1000
b_max = 1001
output = (0, 0, 0)

v_n_consecutive_primes = np.vectorize(n_consecutive_primes)

for i in tqdm(range(-a_max, a_max)):

    # test it
    x = v_n_consecutive_primes(i, [x for x in range(-b_max, b_max + 1)])

    # find location of max consecutive in run
    max_in_run = max(x)
    index_of_max_in_run = np.where(x[:] == max_in_run)[0][0]

    if max_in_run > output[2]:
        output = (i, index_of_max_in_run - b_max, max_in_run)


print("")
print("All done: {}".format(output))
print("Product of coefficients: {}".format(output[0] * output[1]))
