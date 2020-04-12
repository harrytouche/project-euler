"""

A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""
import math


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # array of numbers
nth_perm = int(1e6)  # which permutation


# get number of permutations to estimate where to start
nth_perm -= 1
n_perms = factorial(len(numbers))
print("N permutations: {}".format(n_perms))
print("Nth permutation to find: {}".format(nth_perm))

window_start = 0
window_end = n_perms
window_size = window_end - window_start
numbers_left = len(numbers)
output = []

# pop elements until
while len(numbers) > 0:

    print(" ")
    print("Numbers left: {}, with window size: {}".format(numbers_left, window_size))

    perm_percent = (nth_perm - window_start) / (window_end - window_start)
    print("The nth permutation is {:.0f}% into this run".format(perm_percent * 100))

    pop_index = math.floor(perm_percent * numbers_left)
    print("Popping index: {} which is {}".format(pop_index, numbers[pop_index]))
    output.append(numbers.pop(pop_index))

    window_end = int(window_start + window_size * (pop_index + 1) / numbers_left)
    window_start = int(window_start + window_size * pop_index / numbers_left)
    window_size = window_end - window_start
    numbers_left = len(numbers)

    print("Window start: {}".format(window_start))
    print("Window end: {}".format(window_end))
    print("Window size: {}".format(window_size))
    print("Numbers left: {}".format(numbers_left))
    print("Output: {}".format(output))

    input("Press enter to continue...")


print("N={} permutation is {}".format(nth_perm, "".join([str(x) for x in output])))
