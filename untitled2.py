#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 19:49:11 2020

@author: artemponomarev

a Hackerrank test for Springboard Bootcamp
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import json
import sys
data = sys.stdin.read()
# parse x:
y = json.loads(data)
output = []
for i in range(len(y['report'])):
    for j in range(len(y['report'][i]['subject'])):
        output.append(y['report'][i]['subject'][j]['code']+' '\
                      +y['report'][i]['subject'][j]['grade']+' '\
                      +y['report'][i]['enrollment']+' '\
                      +y['report'][i]['name']\
                      +'\n')

output = sorted(output)
string = ''
for s in output:
    string.join(s)
print(string)
