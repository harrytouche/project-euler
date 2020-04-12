"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""


import inflect

max_number = 1000
sum_digits = 0

p = inflect.engine()
for i in range(1, max_number + 1):

    number_to_words = p.number_to_words(i)

    # remove spaces
    number_to_words = "".join(number_to_words.split(" "))

    # remove hyphens
    number_to_words = "".join(number_to_words.split("-"))
    sum_digits += len(number_to_words)

print(sum_digits)
