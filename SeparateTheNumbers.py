# def separateNumbers(s):
#     for i in range(1, len(s)):
#         seq = [int(s[:i])]
#         print(seq)
#         while len(''.join(map(str, seq))) < len(s):
#             seq.append(seq[-1] + 1)
#         if ''.join(map(str, seq)) == s:
#             print(f"YES {seq[0]}")
#             return
#     print("NO")


def separateNumbers(s):
    for i in range(1, len(s)):
        length = len(s)
        i_seq = [int(s[:i])]  # individual sequence
        ns = ''
        while len(ns) < length:
            i_seq.append(i_seq[-1] + 1)
            ns = ''.join([str(i) for i in i_seq])
        if ns == s:
            print(f'YES {i_seq[0]}')
            return
    print('NO')


s = '99910001001'
# s = "1234"

# for i in range(1, len(s) // 2 - 1):
#     length = len(s)
#     seq = [int(s[:i])]
#     ns = ''
#     while len(ns) < length:
#         seq.append(seq[-1] + 1)
#         ns = ''.join([str(i) for i in seq])
#     if ns == s:
#         print(f'YES {seq[0]}')
#     print('NO')


print(separateNumbers(s))
