#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    def max_func(arr,i,j):
        return sum(arr[i][j:j+3])+arr[i+1][j+1]+sum(arr[i+2][j:j+3])
    max_sum=float("-inf")
    for i in range(4):
        for j in range(4):
            initial_sum=max_func(arr,i,j)
            max_sum=max(max_sum,initial_sum)
    return max_sum  

    #### OR
    
    
#def hourglassSum(arr):
    # res=0
    # x=0
    # z=3
    # res1=[]
    # c=0
    # v=3
    # for b in range(0,4):
    #     for a in range(0,4):
    #         for i in range(c,v):
    #             for j in range(x,z):
    #                 temp = arr[i][j]
    #                 if (i==c+1 and j==x) or (i==c+1 and j==x+2):
    #                     res +=0
    #                 else:
    #                     res +=temp
    #         res1.append(res)
    #         res=0
    #         x=x+1
    #         z=z+1
    #     x=0
    #     z=3
    #     c=c+1
    #     v=v+1
    #return max(res1)        
    # Write your code here


arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

result = hourglassSum(arr)
print("Result is :",result)