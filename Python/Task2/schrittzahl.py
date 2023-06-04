"""
Schrittzahl
"""


def schrittZahl(n: int):
    steps = 0
    while n > 0:
        steps += 1
        if n % 3 == 0:
            n += 4
        elif n % 4 == 0:
            n /= 2
        else:
            n -= 1
    return steps


# Tests
print(schrittZahl(7))  # 11
print(schrittZahl(2))  # 2
print(schrittZahl(50))  # 16
