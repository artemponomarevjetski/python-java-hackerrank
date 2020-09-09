#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#
import requests, json

def getTotalGoals(team, year):
    # Write your code here
    year_str=str(year)
    hometeam=team
    visitingteam=hometeam
    page1='1'
    page2='1'
    url1='https://jsonmock.hackerrank.com/api/football_matches?year='+year_str+'&team1='+hometeam+'&page='+page1
    r1=requests.get(url1)

    url2='https://jsonmock.hackerrank.com/api/football_matches?year='+year_str+'&team2='+visitingteam+'&page='+page2
    r2=requests.get(url2)

    dict1=r1.json()
    dict2=r2.json()

    npages1=dict1['total_pages']
    npages2=dict2['total_pages']

    sum1=0
    for i in range(npages1):
        url1='https://jsonmock.hackerrank.com/api/football_matches?year='+year_str+'&team1='+hometeam+'&page='+str(i+1)
        r1=requests.get(url1)
        dict1=r1.json()
        list1=dict1['data']
        for el in list1:
            sum1+=int(el['team1goals'])

    sum2=0
    for i in range(npages2):
        url2='https://jsonmock.hackerrank.com/api/football_matches?year='+year_str+'&team2='+hometeam+'&page='+str(i+1)
        r2=requests.get(url2)
        dict2=r2.json()
        list2=dict2['data']
        for el in list2:
            sum2+=int(el['team2goals'])

    result=sum1+sum2

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)

    fptr.write(str(result) + '\n')

    fptr.close()
