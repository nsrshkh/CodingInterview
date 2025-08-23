import cProfile
import collections
from GeneralConcepts import timer
from collections import Counter

def unique_counts(s):
    counts = Counter()
    for c in s:
        counts[c] += 1
        yield (c, counts[c])
@timer
def anagram(s):
    if len(s) % 2:
        return -1
    h = len(s) // 2
    s1_counts = set(unique_counts(s[:h]))
    s2_counts = set(unique_counts(s[h:]))
    return len(s1_counts - s2_counts)

# s = "aaabbb"
# s = "asdfjoieufoa"
# s = "mvdalvkiopaufl"
s = "fdhlvosfpafhalll"
# s = "xaxbbbxx"
# cProfile.run('print(anagram(s))')
print(anagram(s))
