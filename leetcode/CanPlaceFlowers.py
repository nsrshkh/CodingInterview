from typing import List


def canPlaceFlowers1(flowerbed: List[int], n: int) -> bool:
    for i in range(0, len(flowerbed) - 1):
        previousSpot = flowerbed[i - 1] == 0 and flowerbed[i] == 0
        nextSpot = flowerbed[i] == 0 and flowerbed[i + 1] == 0
        if previousSpot == nextSpot == True:
            flowerbed[i] = 1
            n -= 1
    return n <=  0

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:

    for i in range(len(flowerbed)):
        left = i == 0 or flowerbed[i - 1] == 0
        right = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

        if left and right and flowerbed[i] == 0:
            flowerbed[i] = 1
            n -= 1

    return n <= 0


flowerbed = [0,0,1,0,1]
n = 1

# flowerbed = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# n = 5
# 1=1, 2=3, 3=5, 4=7,  5=9
# countZero = flowerbed.count(0)
# eligible = countZero - 2
# isOdd = countZero % 2 != 0
# r = 0
# if n == 1:
#     r += 1
# else:
#     r += (n * 2) - 1
# result = eligible >= (n * 2 - 1) and isOdd
# print(result)
print(canPlaceFlowers1(flowerbed, n))
