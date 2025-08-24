import string

def has_digit(password: str) -> bool:
    return any(char in string.digits for char in password)

print(f"Password 'secret123' has a digit: {has_digit('secret123')}")
print(f"Password 'secret' has a digit: {has_digit('secret')}")

import re

text_blob = """
Contact us at support@example.com for help.
For sales, email sales-team@example.co.uk.
John's phone is (123) 456-7890, and Jane's is 555-876-5432.
"""

def extract_emails(text: str) -> list[str]:
    """
    Extracts all valid email addresses from a block of text using regular expressions.
    This is nearly impossible to do reliably with simple string methods.
    """
    # A regex for finding email-like patterns.
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)

def extract_phone_numbers(text: str) -> list[str]:
    """
    Extracts North American-style phone numbers from a block of text.
    The variable formatting makes this a perfect job for regular expressions.
    """
    # Regex to find patterns like (xxx) xxx-xxxx, xxx-xxx-xxxx, etc.
    phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.]?\d{4}'
    return re.findall(phone_pattern, text)


print("--- Extracting Information ---")
print(f"Found emails: {extract_emails(text_blob)}")
print(f"Found phone numbers: {extract_phone_numbers(text_blob)}")