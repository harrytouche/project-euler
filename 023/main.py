"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


from functools import reduce
import math
import numpy as np


def SumOfTwoNumbers(a,b):
    return a+b

def SumOfDivisorsOfNumber(n):
    
    output = []
    max_iteration = math.ceil(n/2) + 1
    
    for i in range(1, max_iteration):
        
        if n % i == 0:
            
            if i not in output:
                output.append(i)

            # only append the other factor if no the sqrt
            if i ** 2 != n and int(n/i) != n and int(n/i) not in output:
                output.append(int(n/i))
                
    
    return reduce(SumOfTwoNumbers, output)


def GetAbundantNumbersUpToN(n):
    abundant_numbers_ceiling = n
    abundant_numbers = []
    
    for i in range(1, abundant_numbers_ceiling+1):
        if SumOfDivisorsOfNumber(i) > i:
            abundant_numbers.append(i)

    return abundant_numbers


abundant_max = 28123


try:
    print("There are {} abundant numbers up to {}".format(len(abundant_numbers),abundant_max))
except Exception:
    abundant_numbers = GetAbundantNumbersUpToN(abundant_max)

# create matrix of all abundant number sums
matrix = np.zeros((len(abundant_numbers),len(abundant_numbers)), dtype=int)
for i in range(len(abundant_numbers)):
    for j in range(len(abundant_numbers)):
        
        new_addition =  abundant_numbers[i] + abundant_numbers[j]
        
        if new_addition < abundant_max:
            matrix[i,j] = new_addition
        
# get the uniques and sum, then take from the sum of all numbers
unique_sums = list(np.unique(matrix))
unique_sums_sum = reduce(SumOfTwoNumbers, unique_sums)
sum_of_all_numbers_to_abundant_max = reduce(SumOfTwoNumbers, range(abundant_max))
difference = sum_of_all_numbers_to_abundant_max - unique_sums_sum

print(difference)



