"""
Ist Schaltjahr
"""


def ist_Schaltjahr(jahr: int):
    if jahr % 4 == 0:
        if jahr % 100 == 0:
            return False
        return True
    if jahr % 100 == 0:
        return False
    if jahr % 400 == 0:
        return True
    return False


# One line function (alternative method)
def ist_Schaltjahr_ol(jahr: int):
    return True if jahr % 4 == 0 and jahr % 100 != 0 else (jahr % 100 != 0 and jahr % 400 == 0)


# Tests
print(ist_Schaltjahr(2023))  # False
print(ist_Schaltjahr(2013))  # False
print(ist_Schaltjahr(2004))  # True
print(ist_Schaltjahr(1996))  # True
print(ist_Schaltjahr(2012))  # True
