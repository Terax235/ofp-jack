"""
Find String
"""


def findString(text: str, query: str, index: int):
    start_index = 0
    final_index = 0
    counter = 0
    while counter < index:
        idx = text.find(query, start_index)
        if idx > -1:
            final_index = idx
            start_index = idx + 1
            counter += 1
        else:
            final_index = -1
            counter = index + 1
    return final_index


# Tests
print(findString("Dies ist ein Beispiel", "ei", 1))  # 9
print(findString("Dies ist ein Beispiel", "ei", 3))  # -1
