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

from datetime import date

min_year = 1901
max_year = 2000
n_sundays_as_firsts = 0


for i in range(min_year, max_year + 1):

    for j in range(1, 13):

        current_date = date(i, j, 1)
        if current_date.weekday() == 6:
            n_sundays_as_firsts += 1

print(
    "There were {} Sundays as first of months between the years {} and {}".format(
        n_sundays_as_firsts, min_year, max_year
    )
)
