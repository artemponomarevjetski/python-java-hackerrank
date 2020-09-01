#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 18:53:14 2020

@author: artemponomarev
"""
import json

line = '''{
    "report":[
        {
            "enrollment": "rit2011001",
            "name": "Julia",
            "subject":[
                {
                    "code": "DSA",
                    "grade": "A"
                }
            ]
        },
        {
            "enrollment": "rit2011020",
            "name": "Samantha",
            "subject":[
                {
                    "code": "COM",
                    "grade": "B"
                },
                {
                    "code": "DSA",
                    "grade": "A"
                }
            ]
        }
    ]
}'''
# parse x:
y = json.loads(line)
# the result is a Python dictionary:
print(y)
print()

output = []
for i in range(len(y['report'])):
    for j in range(len(y['report'][i]['subject'])):
        output.append(y['report'][i]['subject'][j]['code']+'\t'\
                      +y['report'][i]['subject'][j]['grade']+'\t'\
                      +y['report'][i]['enrollment']+'\t'\
                      +y['report'][i]['name']\
                      +'\n')

output = sorted(output)
string=''
for s in output:
    string+=s
print(string)

z = '''COM B rit2011020 Samantha
DSA A rit2011001 Julia
DSA A rit2011020 Samantha'''
print()
print(z)
