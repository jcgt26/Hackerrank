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
    wentThroughTheValley = 0
    iGoThroughTheValley = False
    seaLevel = 0

    for step in path:
        
        seaLevel += -1 if step == 'D' else 1
        if(seaLevel < 0):
            iGoThroughTheValley = True
        elif(seaLevel >= 0 and iGoThroughTheValley == True):
            iGoThroughTheValley = False
            wentThroughTheValley+=1 

    # Write your code here
    return wentThroughTheValley


def iGoThroughTheValley(seaLevel):
    return seaLevel < 0


if __name__ == '__main__':
    fptr = open('ans.txt', 'w')

    steps = int(input().strip())

    path = input()

    re = re.search(path, '')
    if (not (2 <= steps <= 10**6)):
        raise Exception('Out of bound')

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
