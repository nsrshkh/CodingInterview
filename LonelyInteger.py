def lonelyinteger(a):
    return [i for i in set(a) if a.count(i) == 1][0]


a = [1, 2, 3, 4, 3, 2, 1]

print(lonelyinteger(a))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input().strip())
#
#     a = list(map(int, input().rstrip().split()))
#
#     result = lonelyinteger(a)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
