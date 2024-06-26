import string


def minimumNumber(n, password):
    d = {'L': 0, 'U': 0, 'N': 0, 'S': 0}
    l, u, t, s = 1, 1, 1, 1
    for i in password:
        if i in string.ascii_lowercase:
            d['L'] = l
            l += 1
        if i in string.ascii_uppercase:
            d['U'] = u
            u += 1
        if i in string.digits:
            d['N'] = t
            t += 1
        if i in string.punctuation:
            d['S'] = s
            s += 1
    print(d)
    chars = len([v for k, v in d.items() if v == 0])
    if (n + chars) < 6:
        return 6 - n
    else:
        return chars


# password = "Ab1"
# n = 3
# password = "0#)+g!"
# n = 6
# password = "4700"
# n = 4
# password = "#HackerRank"
# n = 11
password = "9"
n = 1


print(minimumNumber(n, password))
