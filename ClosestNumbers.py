def closestNumbers(arr):
    n_arr = []
    arr.sort()
    for i in range(len(arr) - 1):
        c = arr[i]
        n = arr[i + 1]
        d = abs(c - n)
        n_arr.append((c, n, d))
    m = min([i[2] for i in n_arr])
    return [f'{i[0]} {i[1]}' for i in n_arr if i[2] == m]


arr = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]
print(closestNumbers(arr))
