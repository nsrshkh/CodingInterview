import numpy as np


def getTotalX(a, b):
    a_fac = []
    for k in range(1, min(b) + 1):
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if k % a[i] == 0 and k % a[j] == 0:
                    a_fac.append(k)

    b_fac = []
    for k in set(a_fac):
        for i in range(len(b)):
            for j in range(i + 1, len(b)):
                if b[i] % k == 0 and b[j] % k == 0:
                    b_fac.append(k)
    return len(set(b_fac))


def factors(n):
    i = 1
    a = []
    while i <= n:
        if n % i == 0:
            a.append(i)
        i = i + 1
    return a

# a = [2, 4]
# b = [16, 32, 96]

# a = [2, 6]
# b = [24, 36]

# a = [3, 4]
# b = [24, 48]

# a  = [2]
# b = [20, 30, 12]

a = [3, 9, 6]
b = [36, 72]

max_num = [3, 4, int(np.prod(a))]
# print(factors(min(b)))
a_fac = []

for k in range(1, min(b) + 1):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for l in range(i + 2, len(a)):
                if k % a[i] == 0 and k % a[j] == 0 and k % a[l] == 0:
                    a_fac.append(k)
print(set(a_fac))

b_fac = []
for k in set(a_fac):
    for i in range(len(b)):
        for j in range(i + 1, len(b)):
            if b[i] % k == 0 and b[j] % k == 0:
                b_fac.append(k)
print(set(b_fac))



# print(getTotalX(a, b))
