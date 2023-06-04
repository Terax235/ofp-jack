def querSum(n: int):
    text = str(n)
    result = 0
    for char in text:
        result += int(char)
    return result


# Tests
print(querSum(174))  # 12
print(querSum(392))  # 14
