"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from functools import reduce
import math


def SumOfTwoNumbers(a,b):
    return a+b

def SumOfDivisorsOfNumber(n):
    
    output = []
    
    
    max_iteration = math.ceil(math.sqrt(n)) + 1
    
    for i in range(1, max_iteration):
        
        if n % i == 0:
            output.append(i)

            # only append the other factor if no the sqrt
            if i ** 2 != n and int(n/i) != n:
                output.append(int(n/i))
                
    
    return reduce(SumOfTwoNumbers, output)

SumOfDivisorsOfNumber(3)


ceiling = 10000
total = 0

for i in range(2, ceiling):
    
    print("{} / {}".format(i, ceiling))
    
    sum_divisors_i = SumOfDivisorsOfNumber(i)
    
    if sum_divisors_i != i:
        
        sum_sum_divisors_i = SumOfDivisorsOfNumber(sum_divisors_i)
        
        if sum_sum_divisors_i == i:
            
            print("Found amicable numbers: {} and {}".format(sum_divisors_i, sum_sum_divisors_i))
            total += sum_divisors_i + sum_sum_divisors_i
            
# half it as numbers will have counted twice
total = int(total / 2)
print(total)
        