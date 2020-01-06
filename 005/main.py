"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""


divisors = list(range(2,21))
flag = False

# increase in multiples of the largest divisor
i = divisors[-1]
while flag == False:
    
    # for each divisor in the list
    for divisor in divisors:

        # if remainder, then move on
        if i % divisor:
            i += divisors[-1]
            break 
        
        # if the last divisor goes into it, then must the the answer
        if divisor == divisors[-1]:
            flag = True
            break

    
print(i)