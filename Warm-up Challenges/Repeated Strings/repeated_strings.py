#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    a=n//len(s)
    q=s.count("a")
    q=a*q
    re=n%len(s)
    ns=s[:re]
    w=ns.count("a")
    return q+w
   
   #     OR
   ####     return s.count('a')*(n//len(s))+ s[:n%len(s)].count('a')
    # Write your code here


s = input()

n = int(input())

result = repeatedString(s, n)

print("Result is : ",result)