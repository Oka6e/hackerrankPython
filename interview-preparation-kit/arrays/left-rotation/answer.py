#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    new_arr = []
    for j in range(len(a)):
        new_arr.append(0)
    for i in range(len(a)):
        if i-d < 0: # if the index subtracted by d is a negative number
            new_ind = len(a) + (i-d)
            new_arr[new_ind] = a[i]
        else:
            new_ind = i - d
            new_arr[new_ind] = a[i]

    return new_arr

# WAY BETTER ANSWER
# def rotLeft(a, d):
#   d = d%len(a)   
#   return a[d:] + a[:d]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
