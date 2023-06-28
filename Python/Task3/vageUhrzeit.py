"""
Vage Uhrzeit
"""


def vageUhrzeit(time: str):
    split_time = time.split(":")
    hours = int(split_time[0])
    minutes = int(split_time[1])
    if 60 - minutes < 15:
        return "Ungefähr " + str(hours + 1) + " Uhr!"
    elif 60 - minutes < 30:
        return "Ungefähr viertel vor " + str(hours + 1) + "!"
    elif 60 - minutes < 45:
        return "Ungefähr halb " + str(hours + 1) + "!"
    else:
        return "Ungefähr viertel nach " + str(hours) + "!"


# Tests
print(vageUhrzeit("05:13"))  # Ungefähr viertel nach 5!
print(vageUhrzeit("11:30"))  # Ungefähr halb 12!
print(vageUhrzeit("11:25"))  # Ungefähr halb 12!
print(vageUhrzeit("15:31"))  # Ungefähr viertel vor 16!
