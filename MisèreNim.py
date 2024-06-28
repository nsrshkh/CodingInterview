from functools import reduce


def misereNim(s):
    xor = reduce((lambda x, y: x ^ y), s)
    if max(s) == 1:
        return "First" if xor == 0 else "Second"
    else:
        return "Second" if xor == 0 else "First"


s = [9, 8, 4, 4, 4, 7]
# s = [2, 1, 3]

print(misereNim(s))
