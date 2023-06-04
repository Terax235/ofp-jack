"""
Char Frequenz
"""


def charFrequenz(s: str):
    char_count = {}
    special = "äöüß"
    s = s.lower()  # Lowercase string to only count lowercase letters
    for c in s:
        if c.isalpha() and c not in special and c not in char_count:
            char_count[c] = s.count(c)
    # Value sorting
    char_list = [(k, v) for k, v in char_count.items()]
    char_list.sort(key=lambda a: a[1], reverse=True)
    return char_list


# Tests
print(charFrequenz("Das ist ein Teststring"))
# --> [('s', 4),('t', 4),('i', 3),('e', 2),('n', 2),('d', 1),('a', 1),('r', 1), ('g', 1)]
print(charFrequenz("Bananen sind lecker!"))
# --> [('n', 4), ('e', 3), ('a', 2), ('b', 1), ('s', 1), ('i', 1), ('d', 1), ('l', 1), ('c', 1), ('k', 1), ('r', 1)]
