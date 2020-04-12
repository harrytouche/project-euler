"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import math

days = ["mon","tue","wed","thu","fri","sat","sun"]


n_sundays = 0
first_day_index = 0
last_day = ""


for i in range(1900, 2001, 1):
    
    is_leap_year = True if (i%4==0 and not (i%100==0 and not i%400==0)) else False
    n_days_in_year = 365 + (1 if is_leap_year else 0)
    
    n_sundays_in_jan = math.floor((31 + first_day_index) / 7)
    
        
    last_day_index = (math.floor(n_days_in_year % 7) + first_day_index - 1) % 7
    first_day_index = (last_day_index + 1) % 7
    
    if i != 1900:
        n_sundays += n_sundays_in_jan
    
    print("There are {} days in {}".format(n_days_in_year, i))
    print("{} is {} a leap year".format(i, "" if is_leap_year else "not"))
    print("n_sundays_in_jan for {} is {}".format(i, n_sundays_in_jan))
    print("last_day_index / last day in {} is {} / {}".format(i, last_day_index, days[last_day_index]))
    print("There have been {} Sundays so far".format(n_sundays))
    print("-----------------")
    
print("Total number of Sundays is {}".format(n_sundays))
    
#MISREAD THE QUESTION!
