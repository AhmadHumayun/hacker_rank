#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    i=0
    c=0
    while i<len(s)-1:
        if s[i]==s[i+1]:
            s=s.replace(s[i],'',1)
            c+=1
        else:
            i+=1
    return c

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print("Result is:",result)
