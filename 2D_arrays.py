import math
import os
import random
import re
import sys

def max_hourglass(arr):
    results = []
    for n in range(0,4):
        for m in range(0, 4):
            s = sum(arr[n][m:m+3]) + arr[n+1][m+1] + sum(arr[n+2][m:m+3])
            results.append(s)
    print(max(results))


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    max_hourglass(arr)
