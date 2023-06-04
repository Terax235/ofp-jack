"""
Double even
"""


def doubleEven(numbers):
    for i, n in enumerate(numbers):
        if n % 2 == 0:
            numbers[i] = n * 2
    return numbers


# Tests
print(doubleEven([1, 2, 3, 4, 5, 6]))  # [1, 4, 3, 8, 5, 12]
print(doubleEven([2, 4, 6, 8, 10, 11, 14, 16, 17, 18, 28, 20]))  # [4, 8, 12, 16, 20, 11, 28, 32, 17, 36, 56, 40]
