"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


def findReciprocalRepeat(number):

    output = []
    mapping = {}
    counter = 0
    remainder = 1 % number

    while remainder != 0 and counter < 10000 and str(remainder) not in mapping:

        mapping[str(remainder)] = len(output)
        remainder *= 10
        output.append(int(remainder / number))
        remainder = remainder % number
        counter += 1

        # print("")
        # print("Remainder: {}".format(remainder))
        # print("Mapping: {}".format(mapping))
        # print("Output: {}".format(output))

    return (
        0
        if remainder == 0
        else "".join([str(x) for x in output[mapping[str(remainder)] :]])
    )


longest = (2, 0)
max_range = 1000
for x in range(2, max_range):

    attempt = (x, findReciprocalRepeat(x))
    if len(str(attempt[1])) > len(str(longest[1])):
        longest = attempt
        print("New longest: {}".format(longest))

print("")
print(
    "Longest reciprocal up to {} is {}, which is {} of length {}".format(
        max_range, longest[0], longest[1], len(longest[1])
    )
)
