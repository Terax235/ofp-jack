"""
Kapitalwert
"""


def kapitalWert(k_wert, zinssatz, jahre):
    zinsen = zinssatz / 100
    if jahre <= 0:
        return k_wert
    else:
        k_wert += zinsen * k_wert
        return kapitalWert(k_wert, zinssatz, jahre - 1)


# One line function (alternative method)
def kapitalWert_ol(k, z, j):
    return k if j <= 0 else kapitalWert(k + z / 100 * k, z, j - 1)


print(kapitalWert(1000, 5, 2))  # 1102.5
print(kapitalWert(500, 10, 3))  # 665.5
