#!/bin/python3

import os


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    ap = s[-2:]
    hh = int(s[:2])
    mm = s[3:5]
    ss = s[6:8]
    if ap == 'PM':
        nt = f"{hh + 12}:{mm}:{ss}"
    else:
        nt = f"{hh}:{mm}:{ss}"
    return nt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    string = input()

    result = timeConversion(string)

    fptr.write(result + '\n')

    fptr.close()
