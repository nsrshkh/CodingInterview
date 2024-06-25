def minimumAbsoluteDifference(arr):
    n_arr = []
    arr.sort()
    for i in range(len(arr) - 1):
        c = arr[i]
        n = arr[i + 1]
        d = abs(c - n)
        n_arr.append(d)
    return min(n_arr)


arr = [-2, 2, 4]

print(minimumAbsoluteDifference(arr))
