"""
If/Else
"""


def check(a: int | float, b: int | float):
    if a > b:
        return a
    elif b > a:
        return b
    elif a == b:
        return 0


# Tests
print(check(1.5, 2))  # 2
print(check(2, 1))  # 2
print(check(-5, 10))  # 10
print(check(2, 5 ** 2))  # 25 (5**2)
