from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    output = [1] * len(nums)
    left = 1
    right = 1
    for l, r in zip(range(n), range(n - 1, -1, -1)):
        output[l] *= left
        left *= nums[l]
        output[r] *= right
        right *= nums[r]
    return output


nums = [1, 2, 3, 4, 5]
# print(productExceptSelf(nums))
n = len(nums)
output = [1] * len(nums)
left = 1
right = 1
for l, r in zip(range(n), range(n - 1, -1, -1)):
    output[l] *= left
    left *= nums[l]
    output[r] *= right
    right *= nums[r]
print(output)
