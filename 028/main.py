"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


# top right corner of nth circle is the number of numbers

def sum_of_nth_loop(n):

    output = 4 * (2*n+1)**2 - 12*n
    return output


x_spiral = 1001
sum_of_spiral_diagonals = 1

for x in range(1 , int((x_spiral-1)/2) + 1):
    
    sum_to_add = sum_of_nth_loop(x)
    
    print("x: {}, add: {}".format(x, sum_to_add))
        
    sum_of_spiral_diagonals += sum_to_add
    
print("Total: {}".format(sum_of_spiral_diagonals))
