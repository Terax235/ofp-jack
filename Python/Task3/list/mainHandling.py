"""
Main Handling
"""
import listHandling

liste = [1, 2, 5, 3, 8, 20, 11]

print(listHandling.appendElem(22, liste))  # [1, 2, 5, 3, 8, 20, 11, 22]
print(listHandling.insertElem(10, 5, liste))  # [1, 2, 5, 3, 8, 10, 20, 11, 22]
print(listHandling.delElem(6, liste))  # [1, 2, 5, 3, 8, 10, 11, 22]
print(listHandling.sortList(1, liste))  # [1, 2, 3, 5, 8, 10, 11, 22]
print(listHandling.sortList(2, liste))  # [22, 11, 10, 8, 5, 3, 2, 1]
