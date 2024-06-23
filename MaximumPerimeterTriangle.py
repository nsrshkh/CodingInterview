def maximumPerimeterTriangle(sticks):
    n_tri = []
    sticks.sort()
    for i in range(len(sticks)):
        tri = sticks[i:i + 3]
        if len(tri) == 3 and valid_triangle(tri):
            n_tri.append((tri, sum(tri)))
    if len(n_tri) > 0:
        m = max([i[1] for i in n_tri if i[1]])
        n = max([i[0] for i in n_tri if i[1] >= m])
    else:
        n = [-1]
    return n


# sticks = [1, 2, 3, 4, 5, 10]
# sticks = [1, 2, 3]

sticks = [3 ,9 ,2 ,15 ,3]

def valid_triangle(tri):
    if tri[0] + tri[1] > tri[2] and tri[1] + tri[2] > tri[0] and tri[2] + tri[0] > tri[1]:
        return True
    return False


# tri = [1, 2, 3]
# l = len(tri)
# print(valid_triangle(tri))
# for i in range(l):
# print(i,  l - i - 1 if i + 1 >= l else i + 1, l - i-2 if i + 2 >= l else i + 2)
# for j in range(len(tri)):
#     for k in range(len(tri)):
#         if i != j and j != k and i != k:
#             print(i, j, k)
n_tri = []
sticks.sort()
for i in range(len(sticks)):
    tri = sticks[i:i + 3]
    print(tri)
    if len(tri) == 3 and valid_triangle(tri):
        n_tri.append((tri, sum(tri)))
        print(n_tri)
if len(n_tri) > 0:
    m = max([i[1] for i in n_tri if i[1]])
    n = max([i[0] for i in n_tri if i[1] >= m])
else:
    n = [-1]

print(n)
