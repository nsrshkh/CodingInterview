def countingValleys(steps, path):
    n = 0
    p = 0
    for i in path:
        if i == 'D':
            n -= 1
        else:
            n += 1
            if n == 0:
                p += 1
    return p


path = "DDUUDDUDUUUD"
steps = 12

# path = "UDDDUDUU"
# steps = 8


# path = "UDUUUDUDDD"
# steps = 10



n = 0
p = 0
for i in path:
    if i == 'D':
        n -= 1
    else:
        n += 1
        if n == 0:
            p += 1
    print(i, n)
print(p)

# print(countingValleys(steps, path))
