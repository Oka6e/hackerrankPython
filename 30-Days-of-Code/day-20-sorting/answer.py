#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numSwaps = 0
for i in range(n):    
    for j in range(n-1):
        firstElement = a[0]
        lastElement = a[-1]
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            numSwaps += 1
print("Array is sorted in", numSwaps, "swaps.")
print("First Element:", firstElement)
print("Last Element:", lastElement)
