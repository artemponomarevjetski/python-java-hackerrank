#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'longestSubarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def longestSubarray(arr):
    # Write your code here
    current_min=1e9
    current_max=0
    stack=[]
    seq_max=0
    seq=0
    i=0
    while i<len(arr):
        current_min=min(arr[i], current_min)
        current_max=max(arr[i], current_max)
        if current_max-current_min<=1: 
            stack.append(arr[i])
            seq=len(stack)
            seq_max=max(seq, seq_max)
        else:
            if stack:
                popped=stack.pop(0)
                i-=1
                if stack:
                    current_min=min(stack)
                    current_max=max(stack)
                else:
                    current_min=1e9
                    current_max=0
        i+=1
    
    return seq_max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestSubarray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
