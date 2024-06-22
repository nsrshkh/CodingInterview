#!/bin/python3

import os


#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    combinations = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                combinations += 1
    return combinations


# arr = [1, 2, 3, 4, 5, 6]
# n = 6
# k = 5

# arr = [1, 3, 2, 6, 1, 2]
# n = 6
# k = 3

arr = [43, 95, 51, 55, 40, 86, 65, 81, 51, 20, 47, 50, 65, 53, 23, 78, 75, 75, 47, 73, 25, 27, 14, 8, 26, 58, 95, 28, 3,
       23, 48, 69, 26, 3, 73, 52, 34, 7, 40, 33, 56, 98, 71, 29, 70, 71, 28, 12, 18, 49, 19, 25, 2, 18, 15, 41, 51, 42,
       46, 19, 98, 56, 54, 98, 72, 25, 16, 49, 34, 99, 48, 93, 64, 44, 50, 91, 44, 17, 63, 27, 3, 65, 75, 19, 68, 30,
       43, 37, 72, 54, 82, 92, 37, 52, 72, 62, 3, 88, 82, 71]
n = 100
k = 22
print(divisibleSumPairs(n, k, arr))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     first_multiple_input = input().rstrip().split()
#
#     n = int(first_multiple_input[0])
#
#     k = int(first_multiple_input[1])
#
#     ar = list(map(int, input().rstrip().split()))
#
#     result = divisibleSumPairs(n, k, ar)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
