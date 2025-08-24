lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

res_lst = []
for i in range(0, len(lst1)):
    res_lst.append(lst1[i] + lst2[i])
print(res_lst)


# Another approach
a = [1, 2, 3]
b = [4, 5, 6]

c = [x + y for x, y in zip(a, b)]
print(c)