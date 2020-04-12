"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def IsNumberPalindrome(number):
    number_as_string = str(number)
    number_as_string_backwards = number_as_string[::-1]
    # print("Number as string: {}".format(number_as_string))
    # print("Number as string backwards: {}".format(number_as_string_backwards))

    if number_as_string == number_as_string_backwards:
        return True
    else:
        return False


a = list(range(100, 1000))
b = list(range(100, 1000))
max_palindrome = 0

for i in range(len(a)):
    for j in range(len(b)):

        new_number = a[i] * b[j]
        if IsNumberPalindrome(new_number) and new_number > max_palindrome:
            print("New largest palindrom! {}".format(new_number))
            max_palindrome = new_number

print(max_palindrome)
