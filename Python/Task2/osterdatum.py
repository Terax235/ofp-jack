"""
Osterdatum
"""


def osterdatum(year: int):
    k = year // 100
    m = 15 + (3 * k + 3) // 4 - (8 * k + 13) // 25
    s = 2 - (3 * k + 3) // 4
    a = year % 19
    d = (19 * a + m) % 30
    r = (d + a // 11) // 29
    og = 21 + d - r
    sz = 7 - (year + year // 4 + s) % 7
    oe = 7 - (og - sz) % 7
    return og + oe


# Tests
print(osterdatum(2017))  # 47
print(osterdatum(2023))  # 40
print(osterdatum(2004))  # 42
