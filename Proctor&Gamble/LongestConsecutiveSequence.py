def longest_consecutive(nums):
    num_set = set(nums)  # Convert list to set for O(1) lookups
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:  # Start of a new sequence
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest

# Example usage:
num_list = [100, 4, 200, 1, 3, 2, 5]
print(longest_consecutive(num_list))  # Output: 4


from typing import List


def longest_consecutive_set(nums: List[int]) -> int:
    """
    Finds the length of the longest consecutive elements sequence using a set.

    This approach has an average time complexity of O(n) because each number
    is checked at most twice (once in the main loop, and once in the while loop).

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest consecutive sequence.
    """
    if not nums:
        return 0

    num_set = set(nums)  # Convert list to set for O(1) lookups
    longest_streak = 0

    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:  # Start of a new sequence
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)
    return longest_streak


def longest_consecutive_sorting(nums: List[int]) -> int:
    """
    Finds the length of the longest consecutive elements sequence by sorting.

    This approach has a time complexity of O(n log n) due to sorting.
    """
    if not nums:
        return 0

    unique_sorted_nums = sorted(list(set(nums)))
    longest_streak = 1
    current_streak = 1
    for i in range(1, len(unique_sorted_nums)):
        if unique_sorted_nums[i] == unique_sorted_nums[i - 1] + 1:
            current_streak += 1
        else:
            current_streak = 1
        longest_streak = max(longest_streak, current_streak)
    return longest_streak

# Example usage:
num_list = [100, 4, 200, 1, 3, 2, 5]
print(f"Using set method: {longest_consecutive_set(num_list)}")      # Output: 4
print(f"Using sorting method: {longest_consecutive_sorting(num_list)}")  # Output: 4