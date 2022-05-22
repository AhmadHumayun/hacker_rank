#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    # Write your code here
    l=[]
    for i in range(0,d):
        z=a.pop(0)
        a.append(z)
    return a


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

d = int(first_multiple_input[1])

a = list(map(int, input().rstrip().split()))

result = rotLeft(a, d)
print("Result is :",result)