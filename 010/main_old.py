#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:04:08 2020

@author: hartouche
"""
from functools import reduce

# find next prime
def FindNextPrimeNumber(previous_primes):
    
    a = previous_primes[-1]+1        

    while True:
    
        # loop over primes    
        for prime in previous_primes:
    
            # if there is a zero remainder, must be a factor
            if not a % prime:
                break
            
            # if not broken after last prime, new prime
            if prime == previous_primes[-1]:
                print("new prime found: {}".format(a))
                return a
            
        a+=1
       
        
def SumTwoNumbers(a,b):
    return a+b
        

prime_list = [2, 3, 5, 7]

while True:

    next_prime = FindNextPrimeNumber(prime_list)

    if next_prime < 2e6:

        prime_list.append(next_prime)
        
    else:
        break
    
sum_of_primes = reduce(SumTwoNumbers, prime_list)
print("Sum of primes: {}".format(sum_of_primes))
