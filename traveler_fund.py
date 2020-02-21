#!/bin/python

'''
A traveler visits multiple cities. He can work daily and make some money.
He also spends some money on each day. An array is given depicting his daily savings
(earnings – expenses) over the course of his journey. How much minimum money he should
start with in order to have atleast some saving ( > 0) at the end of each day.
Examples:-
Input : arr[] = { 10, -5, 7, -8, 5, -9 }
Let’s say he starts with x.
At end of:-
Day 1, he has a saving of(x + 10)
Day 2, he has a saving of(x + 5)
Day 3, he has a saving of(x + 12)
Day 4, he has a saving of(x + 4)
Day 5, he has a saving of(x + 9)
Day 6, he has a saving of(x + 0)
So, minimum value of x to satisfy the given condition is 1 (one).

https://www.geeksforgeeks.org/goldman-sachs-interview-experience-3/
'''

import math
import os
import random
import re
import sys



#
# Complete the 'requiredAmountAtStart' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY netSaving as parameter.
#

def requiredAmountAtStart(netSaving):
    # Write your code here
    sumTillDay = 0
    requiredAmount = 0
    for e in netSaving:
        if e < 0 and abs(e) > sumTillDay:
            requiredAmount = abs(sumTillDay + e) + 1
        sumTillDay = sumTillDay + e
    return requiredAmount



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    netSaving_count = int(raw_input().strip())

    netSaving = []

    for _ in xrange(netSaving_count):
        netSaving_item = int(raw_input().strip())
        netSaving.append(netSaving_item)

    result = requiredAmountAtStart(netSaving)

    fptr.write(str(result) + '\n')

    fptr.close()
