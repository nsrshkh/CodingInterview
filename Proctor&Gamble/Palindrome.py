def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()  # Remove non-alphanumeric and convert to lowercase
    return s == s[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("hello"))  # Output: False
