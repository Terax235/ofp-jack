"""
Euklidischer Algorithmus
"""


def ggT(a: int, b: int):
    if a == b:
        return a
    if a > b:
        return ggT(a - b, b)
    else:
        return ggT(a, b - a)


# One line function (alternative method)
def ggT_ol(a: int, b: int):
    return a if a == b else (ggT_ol(a - b, b) if a > b else ggT_ol(a, b - a))


# Tests
print(ggT(12, 24))  # 12
print(ggT(54, 38))  # 2
print(ggT(116, 58))  # 58
