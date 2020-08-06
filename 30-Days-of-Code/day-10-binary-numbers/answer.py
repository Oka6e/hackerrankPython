#!/bin/python3

import math
import os
import random
import re
import sys

def convert_to_binary(n):
    c = 0
    max = c
    while n > 0:
        remainder = n%2
        n = n//2

        if remainder == 1:
            c +=1
        else:
            c = 0
        if max<c:
            max=c
    print(max)
    
if __name__ == '__main__':
    n = int(input())
    convert_to_binary(n)