def migratoryBirds(arr):
    n_arr = []
    for i in set(arr):
        k = 0
        for j in arr:
            if i == j:
                k += 1
                n_arr.append((i, k))

    m = max([i[1] for i in n_arr if i[1]])
    return min([i[0] for i in n_arr if i[1] >= m])


arr = [1, 1, 2, 2, 3]
# arr = [1 ,4 ,4 ,4 ,5 ,3]


n_arr = []
for i in set(arr):
    k = 0
    for j in arr:
        if i == j:
            k += 1
            n_arr.append((i, k))

m = max([i[1] for i in n_arr if i[1]])
min([i[0] for i in n_arr if i[1] >= m])

print(min([i[0] for i in n_arr if i[1] >= m]))
