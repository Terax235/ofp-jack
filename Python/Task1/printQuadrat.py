"""
Print Quadrat
"""


def print_Quadrat(n: int):
    s = 0
    for i in range(n):
        s += i * i
    return s


# Tests
print(print_Quadrat(2))  # 1
print(print_Quadrat(5))  # 30
print(print_Quadrat(10))  # 285
print(print_Quadrat(-5))  # 0
