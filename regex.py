#!/bin/python3

import math
import os
import random 
import re
import sys

def appendUserName(firstNameEmailID):
    pattern = '^[a-z]{1,20}+\s+[a-z]{1,50}+@gmail\.com$'

    if re.search(pattern,emailID):
        userList.append(firstName)

if __name__ == '__main__':
    N = int(input())
    userList = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        appendUserName(firstNameEmailID)

    print(*sorted(userList), sep = '\n')
