"""
List Handling (tests located in mainHandling.py)
"""


def appendElem(elem: int, liste: list):
    if type(liste) == list:
        liste.append(elem)
        return liste


def insertElem(elem: int, pos: int, liste: list):
    if type(liste) == list:
        liste.insert(pos, elem)
        return liste


def delElem(elem_index: int, liste: list):
    if type(liste) == list:
        liste.pop(elem_index)
        return liste


def popElem(elem_index: int, liste: list):
    if type(liste) == list:
        if elem_index < 0 or elem_index > len(liste):
            return liste
        else:
            liste.pop(elem_index)
            return liste


def sortList(sort_method: int, liste: list):
    if type(liste) == list:
        if sort_method == 1:
            liste.sort()
        elif sort_method == 2:
            liste.sort(reverse=True)
        return liste
