#!/bin/python

'''
Distributing M items in a circle of size N starting from D-th position
M items are to be delivered in a circle of size M. Find the position where
the M-th item will be delivered if we start from a given position D.
Note that items are distributed at adjacent positions starting from D.
'''

import math
import os
import random
import re
import sys



#
# Complete the 'findDamagedToy' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER T
#  3. INTEGER D
#

def findDamagedToy(N, T, D):
    if T <= (N - D + 1):
        return T + D - 1
    T = T - (N - D + 1)
    if (T % N) == 0:
        return N
    else:
        return T % N


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(raw_input().strip())

    T = int(raw_input().strip())

    D = int(raw_input().strip())

    result = findDamagedToy(N, T, D)

    fptr.write(str(result) + '\n')

    fptr.close()
