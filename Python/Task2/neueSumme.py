"""
Summe
"""


def neueSumme(n: int):
    result = 0
    for i in range(n + 1):
        if i % 7 == 0 and i % 3 != 0:
            result += i
    return result


# Tests
print(neueSumme(77))  # 336
print(neueSumme(25))  # 21
print(neueSumme(40))  # 84
