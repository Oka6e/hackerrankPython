#!/bin/python3

import math
import os
import random
import re
import sys

def maxBitwiseAnd(nk):
    maxAndLessK = 0
    for i in range(n-1, 1, -1):
        for j in range(n, i, -1):
            bitAnd = i&j
            if bitAnd > maxAndLessK and bitAnd < k:
                maxAndLessK = bitAnd
            if maxAndLessK == k-1:
                break
        if maxAndLessK == k-1:
            break
    print(maxAndLessK)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        maxBitwiseAnd(nk)
