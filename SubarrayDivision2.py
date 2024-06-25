def birthday(s, d, m):
    c = 0
    for i in range(len(s)):
        if sum(s[i:i + m]) == d:
            c += 1
    return c


s = [2, 2, 1, 3, 2]
d = 4
m = 2

# s = [4]
# d = 4
# m = 1

print(birthday(s, d, m))
