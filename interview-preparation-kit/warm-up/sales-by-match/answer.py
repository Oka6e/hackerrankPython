#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if ar[i] == ar[j]:
                ar.pop(j)
                count +=1
                break
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    # One liner
    # return sum([ar.count(i)//2 for i in set(ar)])
