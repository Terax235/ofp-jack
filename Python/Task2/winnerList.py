"""
Winner List
"""


def winnerList(a_list: list, b_list: list):
    points_a = 0
    points_b = 0
    for i, a in enumerate(a_list):
        b = b_list[i % len(b_list)]
        if a > b:
            points_a += 1
        elif b > a:
            points_b += 1
    if points_a > points_b:
        return "A"
    elif points_a < points_b:
        return "B"
    else:
        return "0"


# Tests
print(winnerList([7, 9, 3], [5, 9, 2]))  # A
print(winnerList([7, 8, 1], [5, 9, 2]))  # B
print(winnerList([1, 1, 1], [1, 1, 2]))  # B
print(winnerList([1, 2, 3], [1, 2, 3]))  # 0
