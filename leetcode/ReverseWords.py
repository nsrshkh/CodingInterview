def reverseWords(s: str) -> str:
    string = []
    for i in s.split(' '):
        if i:
            string.append(i)
    string.reverse()
    return ' '.join(string)


s = "a good   example"
print(reverseWords(s))
