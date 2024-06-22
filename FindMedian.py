#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    arr.sort()
    l = len(arr)
    m = int(l/2)
    return arr[m]


arr = [5, 3, 1, 2, 4]
arr.sort()
l = len(arr)

print(l, arr[int(l/2)])

