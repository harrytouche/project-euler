"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def NextCollatzNumber(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return int(3 * number + 1)


sequence_to_zero = {}
starting_max = int(1e6)
starting_number = 2

while starting_number < starting_max:

    print("n = {}".format(starting_number))
    current_number = starting_number
    steps_to_one = 1  # itself

    while current_number > 1:

        if str(current_number) in sequence_to_zero:
            # print("sequence to zero for {} is {}".format(current_number, sequence_to_zero[str(current_number)]))
            steps_to_one += sequence_to_zero[str(current_number)]
            current_number = 1

        else:
            current_number = NextCollatzNumber(current_number)
            # print("current number: {}".format(current_number))
            steps_to_one += 1

    sequence_to_zero[str(starting_number)] = steps_to_one
    starting_number += 1


max_value = max(sequence_to_zero.values())
max_key = [k for k, v in sequence_to_zero.items() if v == max_value][0]
