#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    count = 0 
    for i, Person in enumerate(q):
        origin_pos = Person - 1
        if origin_pos - i > 2: # check if original index (person-1) is > then curr index
            print("Too chaotic")
            return
        # check 1 pos in front of the Person's original pos to 1 in front of current pos
        # to see if any numbers are larger than the Person's original position
        for j in range(max(origin_pos - 1, 0), i): 
            if q[j] > origin_pos:
                count += 1
    print(count)
    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
