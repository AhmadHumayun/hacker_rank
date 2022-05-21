#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    jump=0
    num=0
    end=len(c)
    
    z=0
    while(end>2):
        if end>2:
            if c[2]==0:
                c.pop(0)
                c.pop(1)
                end=end-2
                num+=1
                if end<3:
                    break
            if c[2]==1:
                c.pop(0)
                end=end-1
                num+=1
    if end==2:
        num+=1        
    return num
    # Write your code here



n = int(input().strip())

c = list(map(int, input().rstrip().split()))

result = jumpingOnClouds(c)
print("Result is : ",result)
