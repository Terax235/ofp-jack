"""
Print It
"""


def printIT(n: int):
    result = ""
    for i in range(1, n + 1):
        result += str(i)
    return result


# Tests
print(printIT(5))  # 12345
print(printIT(7))  # 1234567
print(printIT(10))  # 12345678910
print(printIT(-1))  # Leerer String
