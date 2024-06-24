def pickingNumbers(a):
    a.sort()
    ret = count = 0
    last_seen = a[0]

    for i in range(len(a)):
        print(a[i], last_seen, count)
        if abs(a[i] - last_seen) <= 1:
            count += 1
            if count > ret:
                ret = count
        else:
            last_seen = a[i]
            count = 1

    return ret


def pickingNumbers1(a):
    a.sort()
    k = []
    for i in a:
        k.append(a.count(i) + a.count(i + 1))
    return max(k)


# a = [4, 6, 5, 3, 3, 1]
a = [1, 2, 2, 3, 1, 2]
# a = [4, 6, 5, 3, 3, 1]

a.sort()
print(a)
b = []
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        print(a[i], a[j])
        # if abs(a[i] - a[j]) <= 1 and a[i] != a[j]:
        #     b.append(a[i])
# print(b)

print(pickingNumbers1(a))
