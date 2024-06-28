
def gcdOfStrings(str1: str, str2: str) -> str:

    if str1 + str2 != str2 + str1:
        return ""

    def gcd(len1, len2):
        while len2:
            len1, len2 = len2, len1 % len2
        return len1

    return str1[:gcd(len(str1), len(str2))]

import math
def gcdOfStrings1(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    gcd = math.gcd(*[len(str1), len(str2)])
    return str1[:gcd]

# str1 = "ABCABC"
# str2 = "ABC"

str1 = "ABABAB"
str2 = "ABAB"

# str1 = "LEET"
# str2 = "CODE"

print(gcdOfStrings1(str1, str2))
