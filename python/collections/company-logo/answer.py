#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def three_most_distinct_charc(s):
    for i in Counter(sorted(s)).most_common(3):
        print(*i)

if __name__ == '__main__':
    s = input()
    three_most_distinct_charc(s)
