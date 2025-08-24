
def valid_square(n):
    if n < 0:
        return False
    root = int(n**0.5)
    return root * root == n

# Example usage
print(valid_square(4))  # Output: True