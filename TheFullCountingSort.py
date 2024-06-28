def countSort(arr):
    arr_sort = [[] for _ in range(100)]
    arr_len = len(arr)
    for j in range(arr_len):
        f = int(arr[j][0])
        s = arr[j][1]
        if j < arr_len // 2:
            arr_sort[f].append('-')
        else:
            arr_sort[f].append(s)

    res = [y for x in arr_sort for y in x]
    print(" ".join(res))


ans = '- - f e b c - a - -'

# arr = [['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['4', 'ij'], ['0', 'ab'], ['6', 'cd'], ['0', 'ef'],
#        ['6', 'gh'], ['0', 'ij'], ['4', 'that'], ['3', 'be'], ['0', 'to'], ['1', 'be'], ['5', 'question'], ['1', 'or'],
#        ['2', 'not'], ['4', 'is'], ['2', 'to'], ['4', 'the']]

arr = [['1', 'e'], ['2', 'a'], ['1', 'b'], ['3', 'a'], ['4', 'f'], ['1', 'f'], ['2', 'a'], ['1', 'e'], ['1', 'b'],
       ['1', 'c']] * 100000

print(countSort(arr))
