def find_missing(input_list):
    """
    Finds the single missing number in a list containing a sequence of integers
    from 1 to n.

    Args:
        input_list: A list of integers with one number missing from the sequence.

    Returns:
        The integer that is missing from the sequence.
    """
    n = len(input_list) + 1  # Since one number is missing
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(input_list)
    return expected_sum - actual_sum

# Example usage:
input_list = [1, 2, 3, 5, 6, 7]
missing_number = find_missing(input_list)
print(f"The missing number is: {missing_number}")  # Output: The missing number is: 3