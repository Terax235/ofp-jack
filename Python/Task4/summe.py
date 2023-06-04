"""
Rekursive Summe
"""


def summe(m: int, n: int):
    if m > n:
        return 0
    return n + summe(m, n - 1)


# One line function (alternative method)
def summe_ol(m: int, n: int):
    return 0 if m > n else n + summe(m, n - 1)


# Tests
print(summe(5, 2))  # 0
print(summe(2, 5))  # 14
print(summe(7, 9))  # 24
print(summe(3, 9))  # 42
