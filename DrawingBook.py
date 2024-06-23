def pageCount(n, p):
    global r, l
    g = []
    for i in range(0, n + 1, 2):
        g.append([i, i + 1])
    for j in g:
        if p in j:
            l = g.index(j)
    g.reverse()
    for j in g:
        if p in j:
            r = g.index(j)
    return min(l, r)


n = 6
p = 2

# n = 5
# p = 4


t = min(p, (n // 2) * 2 + 1 - p) // 2
print(t)
print(pageCount(n, p))
