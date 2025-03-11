from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    f = float('inf')
    s = float('inf')
    for n in nums:
        if n <= f:
            f = n
        elif n <= s:
            s = n
        else:
            return True
    return False


# nums = [1, 2, 3, 4, 5]
# nums = [5, 4, 3, 2, 1]
# nums = [2, 1, 5, 0, 4, 6]
nums = [20, 100, 10, 12, 5, 13]
print(increasingTriplet(nums))
