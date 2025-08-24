def remove_duplicates(nums):
    if not nums:
        return 0
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1
    return nums[:j]


# Example usage:
arr = [1, 2, 2, 3, 3, 4]
print(remove_duplicates(arr))  # Output: [1, 2, 3, 4, 5]


def removeDuplicates(array):
    size = len(array)
    insertIndex = 1
    for i in range(1, size):
        if array[i - 1] != array[i]:
            # Updating insertIndex in our main array
            array[insertIndex] = array[i]
            # Incrementing insertIndex count by 1
            insertIndex = insertIndex + 1
    return insertIndex


array_1 = [1, 2, 2, 3, 3, 4]
print(removeDuplicates(array_1))
# 4


array_2 = [1, 1, 3, 4, 5, 6, 6]
print(removeDuplicates(array_2))
# 5
