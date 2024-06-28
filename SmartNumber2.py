import math


# Only square numbers have odd factors.
def is_smart_number(num):
    val = int(math.sqrt(num))
    if num == int(math.pow(val, 2)):
        return True
    return False


print(is_smart_number(7))

# for _ in range(int(input())):
#     num = int(input())
#     ans = is_smart_number(num)
#     if ans:
#         print("YES")
#     else:
#         print("NO")
