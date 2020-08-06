#!/bin/python3

import math
import os
import random
import re
import sys

def backwards_array(n, arr):
    print(' '.join([str(arr[n]) for n in range(len(arr) - 1, -1, -1)]))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    backwards_array(n, arr)