#!/bin/python3

import math
import os
import random 
import re
import sys

def appendUserName(firstNameEmailID):
    emailPattern = '[a-z]{1,50}@gmail\.com'
    namePattern = '[a-z]{1,20}'


    if re.search(emailPattern,emailID) and re.search(namePattern,firstName):
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
