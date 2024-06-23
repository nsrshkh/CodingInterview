def diagonalDifference(arr):
    r = 0
    l = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                r += arr[i][j]
            if i + j == len(arr) - 1:
                l += arr[i][j]
    return abs(r - l)


matrix = [[1, 2, 3],
          [4, 5, 6],
          [9, 8, 9]]

print(diagonalDifference(matrix))
