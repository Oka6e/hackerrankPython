#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    check = 0
    for i in range(len(c)-1):
        if c[i] == 0 and c[i+1] == 1:
            jumps += 1
            check = 0
        elif c[i] == 0 and c[i+1] == 0 and check == 0:
            jumps += 1
            check = 1
        elif c[i] == 0 and c[i+1] == 0 and check == 1:
            check = 0
            continue
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
