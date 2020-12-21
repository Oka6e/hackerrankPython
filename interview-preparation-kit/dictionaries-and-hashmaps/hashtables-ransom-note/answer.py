#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag_count = {}
    
    # Creates a dictionary of all the words in the magazine and counts them.
    for word in magazine:
        if word in mag_count:
            mag_count[word] += 1
        else:
            mag_count[word] = 1

    for word in note:
        if word in mag_count:
            if mag_count[word] == 0: 
                print("No")
                return
            else: 
                mag_count[word] -= 1
        else: # Word does not exist
            print("No")
            return      
    print("Yes")
    
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
