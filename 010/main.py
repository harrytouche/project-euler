#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:04:08 2020

@author: hartouche
"""


import math


def IsPrimeNumber(number):

    for i in range(2, int(math.sqrt(number)) + 1):

        if number % i == 0:
            # print("{} is a factor of {}".format(i, number))
            return False

    print("{} is a prime number!".format(number))
    return True


a = 3
prime_sum = 2
prime_max = 2000000
while a < prime_max + 1:

    # print(a)

    if IsPrimeNumber(a):
        prime_sum += a

    a += 1


print("Sum of primes under {} is {}".format(prime_max, prime_sum))
