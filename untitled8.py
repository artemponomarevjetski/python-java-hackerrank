#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:02:50 2020

@author: artemponomarev
"""

#!/bin/python3

# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    """
    Hackerrank sample test
    """
    if not 0 < n < 2e5:
        return -1
    for i in range(1, n+1):
        if i//3-i/3 == 0 and i//5-i/5 == 0:
            print("FizzBuzz")
        elif i//3-i/3 == 0 and not i//5-i/5 == 0:
            print("Fizz")
        elif not i//3-i/3 == 0 and i//5-i/5 == 0:
            print("Buzz")
        else:
            print(i)
    return None

if __name__ == '__main__':
    fizzBuzz(10)
