#!/bin/python3

import math
import os
import random
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


def sockMerchant(n, socks):
    
    buffer = list()
    pairs = list()

    for sock in socks: 
        
        if(sock in buffer):   
            index = buffer.index(sock)
            pairs.append(buffer.pop(index))
            
        else:
            buffer.append(sock)
            
    return len(pairs)


if __name__ == '__main__':
    fptr = open('ans.txt', 'w')

    n = int(input().strip())

    socks = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, socks)

    fptr.write(str(result) + '\n')

    fptr.close()
