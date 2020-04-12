"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

total = 0
max_number = 1000
modulos = [3, 5]


for i in range(max_number):

    print("i = {}".format(i))

    for modulo in modulos:

        print("modulo = {}".format(modulo))

        remainder = i % modulo

        print("remainder= {}".format(remainder))

        if remainder == 0:

            total += i
            break


print(total)
