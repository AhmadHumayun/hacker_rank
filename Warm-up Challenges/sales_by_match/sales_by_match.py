#!/bin/python3

import math
import random
import os
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    pair=0
    pair= sum(ar.count(i)//2 for i in set(ar))
    return pair
    # Write your code here


n = int(input().strip())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)
print("result is: ",result)

