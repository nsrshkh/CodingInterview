def kangaroo(x1, v1, x2, v2):
    p1 = x1
    p2 = x2
    for i in range(10000):
        p1 += v1
        p2 += v2
        if p1 == p2:
            return 'YES'
    return 'NO'


x1 = 0
v1 = 3
x2 = 4
v2 = 2


print(kangaroo(x1, v1, x2, v2))