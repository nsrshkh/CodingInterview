def unique(s):
    n = []
    for i in range(len(s)):
        e = s[:i + 1]
        n.append(f'{s[i]}{e.count(s[i])}')
    return n


def anagram(s):
    ls = len(s)
    h = ls // 2
    if ls % 2 == 1:
        return -1
    s1 = s[:h]
    s2 = s[h:]
    return len(set(unique(s1)) - set(unique(s2)))


# s = "aaabbb"
# s = "asdfjoieufoa"
# s = "mvdalvkiopaufl"
# s = "fdhlvosfpafhalll"
s = "xaxbbbxx"

print(anagram(s))
