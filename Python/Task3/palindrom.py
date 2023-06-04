"""
Is Palindrom
"""


def isPalindrom(text: str):
    text_reversed = text.lower()[::-1]
    if text_reversed == text.lower():
        return 1
    else:
        return 0


# Tests
print(isPalindrom("Lagerregal"))  # 1
print(isPalindrom("Hans"))  # 0
print(isPalindrom("12321"))  # 1
print(isPalindrom("Otto"))  # 1
print(isPalindrom("Lotto"))  # 0
