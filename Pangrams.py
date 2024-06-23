import string


def pangrams(s):
    unique = ""
    for i in s.lower():
        if i in string.ascii_lowercase and not i in unique:
            unique += i
    if len(unique) != 26:
        return "not pangram"
    else:
        return "pangram"


sentence = "the quick brown fox jumps over the lazy dog"
# unique = ""
# for i in sentence:
#     if i in string.ascii_lowercase and not i in unique:
#         unique += i

print(pangrams(sentence))
