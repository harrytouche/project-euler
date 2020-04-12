"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


number = 600851475143


# count up, attempting to divide by successive numbers
# when the dividing number is the number itself, that's the biggest prime factor


def LargestPrimeFactor(number):

    i = 2

    while number > 1:

        # if i is a factor, divide by that number
        if number % i == 0:
            number = number / i

        else:
            i += 1

    return i


LargestPrimeFactor(number)
