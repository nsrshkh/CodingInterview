def min_max_num(arr):
    arr.sort()
    max_sum = sum(arr[-4:])
    min_sum = sum(arr[:4])
    print(min_sum, max_sum)


if __name__ == '__main__':
    sample = [1, 2, 3, 4, 5]

    min_max_num(sample)
