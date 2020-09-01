#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 13:04:01 2020

@author: artemponomarev
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
data = sys.stdin.read()
prices = data.split()
sum_ = 0
for pp in prices:
    p = int(pp)
    if p <= 0:
        print("Price is negative or 0...\n")
        break
    if  100 <= p < 200:
        sum_ += (1-0.25)*p
    elif p >= 200:
        sum_ += (1-0.5)*p
    else:
        sum_ += p

if sum_ >= 300:
    sum_ -= 50

print(int(sum_))
