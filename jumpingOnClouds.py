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


def jumpingOnClouds(clouds):
    jumps = 0
    i = 0
    numberOfClouds = len(clouds)
    while (i <= numberOfClouds - 1):  # <= 3
        if(numberOfClouds - i -1  > 1):
            i += 2 if clouds[i+2] == 0 else 1
            print(i)
            jumps += 1
        if(i == numberOfClouds -1):
            i += 1
    return jumps


def isCloudSafe(index, clouds):
    return clouds[index] == 0


if __name__ == '__main__':
    fptr = open('ans.txt', 'w')

    #n = int(input().strip())

    #c = list(map(int, input().rstrip().split()))
    #    0  1  2  3  4
    c = [0, 0, 0, 0]
    if(2 <= len(c) >= 100):
        raise Exception('Out Of bounds')

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
