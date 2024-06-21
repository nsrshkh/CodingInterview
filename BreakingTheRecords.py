#!/bin/python3

import os


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(s):
    j = 0
    k = 0
    p_min = scores[0]
    p_max = scores[0]
    for i in range(len(scores)):
        n_scores = scores[0:i + 1]
        min1 = min(n_scores)
        max1 = max(n_scores)
        if max1 > p_max:
            j += 1
            p_max = max1
        if min1 < p_min:
            k += 1
            p_min = min1
    return [j, k]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())

    scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
    # scores = [12, 24, 10, 24]
    result = breakingRecords(scores)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
