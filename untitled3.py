#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:47:40 2020

@author: artemponomarev
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
data = sys.stdin.read()
list_ = data.split('\n')
list1 = []
for l in list_:
    if l != '':
        list1.append(l)
set_ = set(list1)
print(len(set_))
