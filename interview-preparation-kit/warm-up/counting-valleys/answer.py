#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    pos = [0]
    val_count = 0
    for step in range(steps):
        if path[step] == 'U':
            cur_pos = pos[step] + 1
            pos.append(cur_pos)
        elif path[step] == 'D':
            cur_pos = pos[step] - 1
            pos.append(cur_pos)
    for i in range(len(pos) - 1):
        if pos[i] == 0 and pos[i+1] == -1:
            val_count += 1
    return val_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

# Better Answer
# def countingValleys(steps, path):
#     position = 0
#     valleys = 0
#     for step in range(steps):
#         position += 1 if path[step] == 'U' else -1
#         if path[step] == 'U' and position == 0:
#             valleys += 1
#     return valleys
