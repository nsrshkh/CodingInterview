# matrix = [[1, 2], [3, 4]]

matrix = [[112, 42, 83, 119],
          [56, 125, 56, 49],
          [15, 78, 101, 43],
          [62, 98, 114, 108]]


def flippingMatrix(matrix):
    sum = 0
    n = len(matrix)
    rng = n // 2
    print(rng)
    for i in range(rng):
        for j in range(rng):
            print(i, j, n - j - 1, n - i - 1)
            if i < rng and j < rng:
                sum += max(matrix[i][j], matrix[i][n - j - 1], matrix[n - i - 1][j], matrix[n - i - 1][n - j - 1])
    return sum


def row_flip(matrix, c):
    r_arr = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == c:
                r_arr.append(matrix[::-1][i][j])
            else:
                r_arr.append(matrix[i][j])
    return [r_arr[i:i + len(matrix)] for i in range(0, len(r_arr), len(matrix))]


def column_flip(matrix, r):
    c_arr = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == r:
                c_arr.append(matrix[i][::-1][j])
            else:
                c_arr.append(matrix[i][j])
    return [c_arr[i:i + len(matrix)] for i in range(0, len(c_arr), len(matrix))]

print(flippingMatrix(matrix))
