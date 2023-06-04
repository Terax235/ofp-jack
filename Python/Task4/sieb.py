"""
Sieb des Eratosthenes
"""

"""
This implementation works fine for low prime numbers. It will not return the correct result in cases like sieb(1000),
but the task wants you to implement the function like below with only eliminating the multiples of 2,3,5 and 7.
Visit https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes for more information about the correct implementation.
"""


def vielfaches(n: int, numbers: list):
    new_list = []
    for i in numbers:
        if (i % n != 0 or i == n) and i not in new_list:
            new_list.append(i)
    return new_list


def sieb(n: int):
    prim = range(2, n)
    for i in [2, 3, 5, 7]:
        prim = vielfaches(i, prim)
    return prim


# Tests
print(sieb(50))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
print(sieb(100))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

