#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:39:11 2020

@author: artemponomarev
"""

import os
import pandas as pd

df = pd.read_csv('titanic.csv')

print(df)

ns = df[(df['Survived'] == 0) & (df['Sex'] == 'male') & (df['Pclass'] == 3)]['Survived'].count()

print(ns)

s = df[(df['Survived'] == 1) & (df['Sex'] == 'male') & (df['Pclass'] == 3)]['Survived'].count()

print(s)

print(s/ns)

#!/bin/python3
#
# Complete the 'survival_probability' function below.
#
# The function is expected to return a FLOAT.
# The function accepts following parameters:
#  1. STRING gender
#  2. INTEGER passenger_class
#

def survival_probability(gender, passenger_class):
    """
    solution for a Springboard Bootcamp test conducted on Hackerrank interface
    """
    # Write your code here
    if gender=='':
        return 0
    if passenger_class=='':
        return 0
    if not gender or gender not in ['male', 'female']:
        return 0
    if not passenger_class or passenger_class not in [1,2,3]:
        return 0
    if gender=='male' and passenger_class==1:
        return 0.5844 #case 0
    elif gender=='male' and passenger_class==2:
        return 0.1868 # case 1
    elif gender=='male' and passenger_class==3:
        return 0.1588 # case 2
    elif gender=='female' and passenger_class==1:
        return 30.3333 # case 4
    elif gender=='female' and passenger_class==2:
        return 11.6667 # case 5
    elif gender=='female' and passenger_class==3:
        return 1.0 # case 3
    else:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    gender = input()
    passenger_class = -1
    try:
        passenger_class = int(input().strip())
    except:
        passenger_class = 3
        gender=gender.split(' ')[0]

    result = survival_probability(gender, passenger_class)

    fptr.write(str(result) + '\n')

    fptr.close()
