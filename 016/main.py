#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 13:00:18 2020

@author: hartouche
"""

from functools import reduce


def SumTwoNumbersAsInt(a,b):
    return int(a) + int(b)

def SumOfDigitsOfNumber(n):

    n_sum = reduce(SumTwoNumbersAsInt, list(str(n)))
    
    return n_sum

print(SumOfDigitsOfNumber(2**1000))
        