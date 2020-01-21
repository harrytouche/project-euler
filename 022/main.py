"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import csv
from functools import reduce


def NameValue(name):
    output = 0
    name = list(name)
    
    for letter in name:
        output += ord(letter) - 64
    
    return output
    
def GetNameScore(name_object):
    return int(name_object["alpha"] * name_object["value"])
    


with open('names.txt', 'r') as f:
    reader = csv.reader(f)
    names = list(reader)[0]
    names.sort()
    names = [{"name": names[i], "alpha":i+1, "value":NameValue(names[i])} for i in range(len(names))]
  


total = 0
for name in names:
    total += int(name["alpha"] * name["value"])
    
print("Total is: {}".format(total))