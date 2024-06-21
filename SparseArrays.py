#!/bin/python3

import os


#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    s = []

    for i in queries:
        c = 0
        for j in strings:
            if i == j:
                c += 1
        s.append(c)
    return s


# strings = ['ab', 'ab', 'abc']
# queries = ['ab', 'abc', 'bc']

# strings = ['aba','baba','aba','xzxb']
# queries = ['aba','xzxb','ab']

strings = ['lekgdisnsbfdzpqlkg', 'eagemhdygyv', 'jwvwwnrhuai', 'urcadmrwlqe', 'mpgqsvxrijpombyv', 'mpgqsvxrijpombyv',
           'urcadmrwlqe', 'mpgqsvxrijpombyv', 'eagemhdygyv', 'eagemhdygyv', 'jwvwwnrhuai', 'urcadmrwlqe', 'jwvwwnrhuai',
           'kvugevicpsdf', 'kvugevicpsdf', 'mpgqsvxrijpombyv', 'urcadmrwlqe', 'mpgqsvxrijpombyv', 'exdafbnobg',
           'qhootohpnfvbl', 'suffrbmqgnln', 'exdafbnobg', 'exdafbnobg', 'eagemhdygyv', 'mpgqsvxrijpombyv',
           'urcadmrwlqe', 'jwvwwnrhuai', 'lekgdisnsbfdzpqlkg', 'mpgqsvxrijpombyv', 'lekgdisnsbfdzpqlkg', 'jwvwwnrhuai',
           'exdafbnobg', 'mpgqsvxrijpombyv', 'kvugevicpsdf', 'qhootohpnfvbl', 'urcadmrwlqe', 'kvugevicpsdf',
           'mpgqsvxrijpombyv', 'lekgdisnsbfdzpqlkg', 'mpgqsvxrijpombyv', 'kvugevicpsdf', 'qhootohpnfvbl',
           'lxyqetmgdbmh', 'urcadmrwlqe', 'urcadmrwlqe', 'kvugevicpsdf', 'lxyqetmgdbmh', 'urcadmrwlqe', 'lxyqetmgdbmh',
           'jwvwwnrhuai', 'qhootohpnfvbl', 'qhootohpnfvbl', 'jwvwwnrhuai', 'lekgdisnsbfdzpqlkg', 'kvugevicpsdf',
           'mpgqsvxrijpombyv', 'exdafbnobg', 'kvugevicpsdf', 'lekgdisnsbfdzpqlkg', 'qhootohpnfvbl', 'exdafbnobg',
           'qhootohpnfvbl', 'exdafbnobg', 'mpgqsvxrijpombyv', 'suffrbmqgnln', 'mpgqsvxrijpombyv', 'qhootohpnfvbl',
           'jwvwwnrhuai', 'mpgqsvxrijpombyv', 'qhootohpnfvbl', 'lekgdisnsbfdzpqlkg', 'eagemhdygyv', 'jwvwwnrhuai',
           'kvugevicpsdf', 'eagemhdygyv', 'eagemhdygyv', 'lxyqetmgdbmh', 'qhootohpnfvbl', 'lxyqetmgdbmh', 'exdafbnobg',
           'qhootohpnfvbl', 'qhootohpnfvbl', 'exdafbnobg', 'suffrbmqgnln', 'mpgqsvxrijpombyv', 'urcadmrwlqe',
           'eagemhdygyv', 'lxyqetmgdbmh', 'urcadmrwlqe', 'suffrbmqgnln', 'qhootohpnfvbl', 'kvugevicpsdf',
           'lekgdisnsbfdzpqlkg', 'lxyqetmgdbmh', 'mpgqsvxrijpombyv', 'jwvwwnrhuai', 'lxyqetmgdbmh', 'lxyqetmgdbmh',
           'lekgdisnsbfdzpqlkg', 'qhootohpnfvbl']
queries = ['exdafbnobg', 'eagemhdygyv', 'mpgqsvxrijpombyv', 'kvugevicpsdf', 'lekgdisnsbfdzpqlkg', 'kvugevicpsdf',
           'exdafbnobg', 'qhootohpnfvbl', 'eagemhdygyv', 'kvugevicpsdf', 'suffrbmqgnln', 'jwvwwnrhuai',
           'lekgdisnsbfdzpqlkg', 'lekgdisnsbfdzpqlkg', 'mpgqsvxrijpombyv', 'jwvwwnrhuai', 'kvugevicpsdf',
           'lekgdisnsbfdzpqlkg', 'exdafbnobg', 'suffrbmqgnln', 'qhootohpnfvbl', 'eagemhdygyv', 'exdafbnobg',
           'suffrbmqgnln', 'jwvwwnrhuai', 'qhootohpnfvbl', 'eagemhdygyv', 'exdafbnobg', 'exdafbnobg', 'jwvwwnrhuai',
           'qhootohpnfvbl', 'lxyqetmgdbmh', 'qhootohpnfvbl', 'suffrbmqgnln', 'lxyqetmgdbmh', 'qhootohpnfvbl',
           'eagemhdygyv', 'jwvwwnrhuai', 'eagemhdygyv', 'qhootohpnfvbl', 'mpgqsvxrijpombyv', 'qhootohpnfvbl',
           'jwvwwnrhuai', 'exdafbnobg', 'eagemhdygyv', 'eagemhdygyv', 'kvugevicpsdf', 'kvugevicpsdf', 'jwvwwnrhuai',
           'urcadmrwlqe', 'lxyqetmgdbmh', 'qhootohpnfvbl', 'exdafbnobg', 'exdafbnobg', 'eagemhdygyv', 'qhootohpnfvbl',
           'exdafbnobg', 'exdafbnobg', 'lekgdisnsbfdzpqlkg', 'jwvwwnrhuai', 'eagemhdygyv', 'urcadmrwlqe',
           'kvugevicpsdf', 'lekgdisnsbfdzpqlkg', 'jwvwwnrhuai', 'eagemhdygyv', 'lekgdisnsbfdzpqlkg', 'exdafbnobg',
           'kvugevicpsdf', 'jwvwwnrhuai', 'exdafbnobg', 'lxyqetmgdbmh', 'exdafbnobg', 'lxyqetmgdbmh', 'jwvwwnrhuai',
           'mpgqsvxrijpombyv', 'eagemhdygyv', 'urcadmrwlqe', 'kvugevicpsdf', 'qhootohpnfvbl', 'jwvwwnrhuai',
           'eagemhdygyv', 'urcadmrwlqe', 'urcadmrwlqe', 'exdafbnobg', 'qhootohpnfvbl', 'exdafbnobg', 'eagemhdygyv',
           'exdafbnobg', 'jwvwwnrhuai', 'eagemhdygyv', 'jwvwwnrhuai', 'mpgqsvxrijpombyv', 'urcadmrwlqe', 'urcadmrwlqe',
           'eagemhdygyv', 'eagemhdygyv', 'jwvwwnrhuai', 'suffrbmqgnln', 'eagemhdygyv']

# g = [[i,queries.count(i)] for i in set(queries)]
#
# print(g)


print(matchingStrings(strings, queries))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     strings_count = int(input().strip())
#
#     strings = []
#
#     for _ in range(strings_count):
#         strings_item = input()
#         strings.append(strings_item)
#
#     queries_count = int(input().strip())
#
#     queries = []
#
#     for _ in range(queries_count):
#         queries_item = input()
#         queries.append(queries_item)
#
#     res = matchingStrings(strings, queries)
#
#     fptr.write('\n'.join(map(str, res)))
#     fptr.write('\n')
#
#     fptr.close()
