def twoArrays(k, A, B):
    C = []
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        if (A[i] + B[i]) >= k:
            C.append((A[i], B[i]))

    if len(C) >= len(A):
        return 'YES'
    else:
        return 'NO'


# A = [2, 1, 3]
# B = [7, 8, 9]
# k = 10

A = [1, 2, 2, 1]
B = [3, 3, 3, 4]
k = 5

# a = [20, 1]
# b = [1, 1]
# k = 4

# a = [10000, 1, 1, 1]
# b = [1, 1, 1, 1]
# k = 10

# A = [7, 6, 8, 4, 2]
# B = [5, 2, 6, 3, 1]
# k = 10

print(twoArrays(k, A, B))
