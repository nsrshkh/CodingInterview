def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:  # added == instead of = (assignment)
            res += '0'  # added += instead of = (assignment)
        else:
            res += '1'
    return res


s = '10101'
t = '00101'
print(strings_xor(s, t))
