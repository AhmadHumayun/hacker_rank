#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here

    mv=0
    z=0
    state=[0]
    #level=[0]
    level=0
    #a=path.count("D",2,5)
    #print(a)
    for i in range(steps):
        if path[i] == 'D':
            level-=1
        #    state.append(-1)
        if path[i]=='U':
            level+=1
        if level==0 and z<0:
            mv+=1
        z=level
    return mv
        



steps = int(input().strip())

path = input()

result = countingValleys(steps, path)
print("Result is: ",result)
