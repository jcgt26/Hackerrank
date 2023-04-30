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
    # Write your code here abc abc abc a
    if(len(s) == 1):
        return n
    sub = len(s);
    counter = s.count('a')
    return counter * n - ((sub - counter) * n)
    
if __name__ == '__main__':
    fptr = open('ans.txt', 'w')

    s = input()

    n = int(input().strip())
    
    fptr
    #result = repeatedString(s, n)
    fptr.write('a'*n)
   # fptr.write(str(result) + '\n')

    fptr.close()
