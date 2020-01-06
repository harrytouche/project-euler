"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

from functools import reduce


def SquareNumber(n):
    return n**2


def SumTwoNumbers(a,b):
    return a+b

def SumOfSquareNumbersToNumber(n):
    
    list_of_numbers = list(range(1,n+1))
    list_of_numbers = map(SquareNumber,list_of_numbers)
    return reduce(SumTwoNumbers,list_of_numbers)

def SquareOfSumOfNumbersToNumber(n):
    list_of_numbers = list(range(1,n+1))
    sum_of_numbers = reduce(SumTwoNumbers, list_of_numbers)
    return sum_of_numbers ** 2


print(abs(SumOfSquareNumbersToNumber(100) - SquareOfSumOfNumbersToNumber(100)))