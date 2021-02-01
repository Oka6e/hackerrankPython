#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    ordered_arr = sorted(arr)
    swaps = 0
    arr_idc = {val:ind for ind, val in enumerate(arr)}
    for i in range(len(arr)):
        if arr[i] != ordered_arr[i]:
            corr_val_ind = arr_idc[ordered_arr[i]]
            # swap the values in the original array
            arr[i], arr[corr_val_ind] = arr[corr_val_ind], arr[i] 
            swaps += 1
            # update the current index locations of the swapped values
            arr_idc[arr[i]] = i
            arr_idc[arr[corr_val_ind]] = corr_val_ind
    return swaps
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
