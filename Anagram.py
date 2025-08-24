import cProfile
from collections import Counter


def count_anagram_changes(s: str) -> int:
    """
    Calculates the minimum character changes to make two halves of a string anagrams.

    The string is split in half. The function then counts how many characters
    in the first half need to be changed to make it an anagram of the second half.

    Args:
        s: The input string. Must have an even length.

    Returns:
        The number of character changes required.
        Returns -1 if the string has an odd length and cannot be split evenly.
    """
    if len(s) % 2 != 0:
        return -1

    half_len = len(s) // 2
    s1 = s[:half_len]
    s2 = s[half_len:]

    # Create frequency counts of characters in each half. This is O(n).
    count1 = Counter(s1)
    count2 = Counter(s2)

    # The difference gives us the characters that are in excess in s1.
    # The sum of the values of this difference is the number of changes needed.
    difference = count1 - count2
    return sum(difference.values())


# s = "aaabbb"
# s = "asdfjoieufoa"
# s = "mvdalvkiopaufl"
s = "fdhlvosfpafhalll"
# s = "xaxbbbxx"

cProfile.run('print(count_anagram_changes(s))')
# print(count_anagram_changes(s))
