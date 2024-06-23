def marsExploration(s):
    n = []
    t = (len(s) // 3 * "SOS")
    for i in range(len(s)):
        if s[i] != t[i]:
            n.append(s[i])
    return len(n)


# s = "SOSTOT"

# s = "SOSSPSSQSSOR"
s = "SOSOOSOSOSOSOSSOSOSOSOSOSOS"
t = (len(s) // 3 * "SOS")

n = []
for i in range(len(s)):
    if s[i] != t[i]:
        n.append(s[i])

print(marsExploration(s))
