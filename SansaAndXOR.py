# Array with even number of elements will always result in 0
# Only do XOR operation with elements appear odd number of time

# XOR for array with even number of elements is always 0
# Only do XOR operation with elements appear odd number of time
def sansaXor(arr):
    arr_len = len(arr)
    if arr_len % 2 == 0:
        return 0
    c = 0
    for i in range(arr_len):
        if i % 2 == 0:
            c ^= arr[i]
    return c


arr = [4, 5, 7, 5]

print(sansaXor(arr))
