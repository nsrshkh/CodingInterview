from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    maxCandies = max(candies)
    moreCandies = []
    for x in candies:
        n = (x + extraCandies) >= maxCandies
        moreCandies.append(n)
    return moreCandies


candies = [2, 3, 5, 1, 3]
extraCandies = 3

print(kidsWithCandies(candies, extraCandies))
