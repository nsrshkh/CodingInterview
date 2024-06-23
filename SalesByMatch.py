def sockMerchant(n, ar):
    s = 0
    for i in set(ar):
        c = 0
        for j in ar:
            if i == j:
                c += 1
        if c >= 2:
            s += (c // 2)
    return s


ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9

print(sockMerchant(n, ar))
