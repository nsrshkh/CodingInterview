def flippingBits(n):
    return 2 ** 32 - n - 1
    # a = ''
    # b = format(n, '032b')
    # for i in b:
    #     if i == '1':
    #         a += '0'
    #     else:
    #         a += '1'
    # return int(a, 2)


n = 9

print(flippingBits(n))
