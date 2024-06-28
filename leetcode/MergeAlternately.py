def mergeAlternately(word1: str, word2: str):
    result = []
    l1 = len(word1)
    l2 = len(word2)
    if l1 > l2:
        diff = word1[l2:]
    else:
        diff = word2[l1:]
    for a, b in zip(word1, word2):
        result.append(a + b)
    # for i, a in enumerate(word1):
    #     for j, b in enumerate(word2):
    #         if i == j:
    #             result.append(a + b)
    return ''.join(result) + diff

def mergeAlternately1(word1: str, word2: str) -> str:
    merged = []

    for a, b in zip(word1, word2):
        merged.append(a + b)
    print(merged)
    merged.append(word1[len(word2):])
    merged.append(word2[len(word1):])

    return "".join(merged)

word1 = "abcdf"
word2 = "pqrs"
print(mergeAlternately(word1, word2))
