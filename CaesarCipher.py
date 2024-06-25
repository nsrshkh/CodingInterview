import string
def caesarCipher(s, k):
    n = []
    m = k % 26
    for i in s:
        if i in string.ascii_letters:
            asc = ord(i) + m
            if asc > 122 and ord(i) in range(97, 123):
                asc = asc - 26
            if asc > 90 and ord(i) in range(65, 91):
                asc = asc - 26
            n.append(chr(asc))
        else:
            n.append(i)
    return ''.join(n)

# k = 5
# s = 'Always-Look-on-the-Bright-Side-of-Life'
# r = 'Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj'
s = "www.abc.xy"
r = "fff.jkl.gh"
k = 87

print(k % 26)

print(caesarCipher(s, k))
