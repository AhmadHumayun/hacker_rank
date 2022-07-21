#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    c=0
    for i in a:
        if i in b:
            c+=1
            b=b.replace(i,'',1)
    return len(b)+(len(a)-c)

if __name__ == '__main__':
    a = input()

    b = input()

    res = makeAnagram(a, b)
    print("Result is:",res)
