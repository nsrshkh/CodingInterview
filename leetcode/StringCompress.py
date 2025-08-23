from typing import List


def compress(self, chars: List[str]) -> int:
    return 1


chars = ["a", "a", "b", "b", "c", "c", "c", "a"]
# chars = ["a", "b", "b", "c", "c", "c", "a", "a", "b", "b", "b", "c", "c"]

s = [chars[0] + '0']
n = len(chars)
chars_set = list(set(chars))
chars_set.sort()
# print(chars_set)
c = 0
for i in range(n - 1):

    if chars[i] == chars[i + 1]:
        s.append(chars[i] + str(c))
        # s.append(chars[i + 1] + str(c))
    else:
        c += 1
        s.append(chars[i + 1] + str(c))
        print(s)

d = dict.fromkeys(s, 0)

for i in s:
    d[i] += 1

print(d)
