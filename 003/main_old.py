"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


# number = 600851475143
number = 100000


# get prime numbers up to number
def ZeroOutNumbersWhichAreFactor(number, factor):
    if number == 0:
        return 0

    elif number == factor:
        return number

    elif number % factor == 0:
        return 0

    else:
        return number


def RemoveFalsyNumbers(number):
    return not not number


def PrimeNumbersUpToNumber(n):

    number_list = range(2, int((n / 2) + 1))
    prime_list = number_list

    # loop through all numbers
    for i in range(len(number_list)):

        if not i % 1000:
            print("i = {} out of {}".format(i, len(number_list)))

        # if number not zeroed
        if prime_list[i] != 0:

            # zero out numbers which are a factor
            prime_list = [
                ZeroOutNumbersWhichAreFactor(x, prime_list[i]) for x in prime_list
            ]

    return list(filter(RemoveFalsyNumbers, prime_list))


my_list = PrimeNumbersUpToNumber(number)


# loop down the recorded prime numbers until one is a factor of number
