"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


a + b + c = 1000

a**2 + b**2 = c**2

"""


sum_number = 1000
complete = 0
loop_max = sum_number


for a in range(1, loop_max):
    for b in range(1, loop_max - a):

        # c is defined once a and b are
        c = loop_max - a - b

        if (a ** 2 + b ** 2) == c ** 2:
            print("Found! a={}, b={}, c={}".format(a, b, c))
            print("Product is: {}".format(a * b * c))
            complete = 1

        if complete == 1:
            break
    if complete == 1:
        break
