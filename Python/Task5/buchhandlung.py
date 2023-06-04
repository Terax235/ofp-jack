"""
Buchhandlung
"""


def biblio(liste):
    return list(map(lambda x: (x[0], x[2] * x[3] + 10 if x[2] * x[3] < 100 else x[2] * x[3]), liste))


# For better understanding (does the same as lambda function p)
def process(x):
    bestell_nr = x[0]
    anzahl = x[2]
    preis = x[3]
    kosten = anzahl * preis
    if anzahl * preis < 100:
        kosten += 10
    return bestell_nr, kosten


# Tests
print(biblio([
    ["34587", "Learning Python, Mark Lutz", 4, 40.95],
    ["98762", "Programming Python, Mark Lutz", 5, 56.80],
    ["77226", "Head First Python, Paul Barry", 3, 32.95]
]))  # [('34587', 163.8), ('98762', 284.0), ('77226', 108.85000000000001)]
