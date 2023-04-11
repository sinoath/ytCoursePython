# Data collections in python

# print numbers divisible by 3 inside the list
numbers = [1, 2, 23, 44, 12, -6, -33, -4, 6]

for number in numbers:
    if number % 3 == 0:
        print(number, end="  ")
else:
    print()

# print only the cities with an even number of letters in the tuple
cities = ("Milano", "Catania", "Roma", "Venezia", "Brescia", "Ragusa")

for city in cities:
    if city.__len__() % 2 == 0:
        print(city, end=" ")
else:
    print(end="\n")


# print only the common elements in odds (set) and numbers (list)
odds = {1, 3, 5, 7, 9, 11, 13}
integers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for odd in odds:
    for integer in integers:
        if integer == odd:
            print(integer, end=" ")
else:
    print(end = "\n")
# a better for cycle could be:
# for odd in odds:
#     if odd in integers:
#         print(odd)


# print the elements inside the dictionary with a value >5
custom_dictionary = {
        "one": 1,
        "eleven" : 11,
        "four" : 4,
        "twenty" : 20,
        "five" : 5
}

for key in list(custom_dictionary.keys()):
    if custom_dictionary[key] > 5:
        print(key + " : " + str(custom_dictionary[key]), end="   ")
else:
    print(end="\n")

# a better for cicle could be:
# for key, value in custom_dictionary.items():
#     if value > 5:
#         print(key, value)


# list of tuple: print only the tuple with the first element starting with 'a'

list_of_tuple = [
        ("Milano", "Lombardia"),
        ("Catania", "Sicilia"),
        ("Roma", "Lazio"),
        ("Agrigento", "Sicilia"),
        ("Venezia", "Veneto"),
        ("Ancona", "Marche")
]

for inside_list in list_of_tuple:
    if inside_list[0][0] == "A":
        print(inside_list, end="   ")
else:
    print(end="\n")


# set of tuple: print the tuple if the sum of integer elements is even
set_of_tuple = {
        (1, 1),
        (1, 2),
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 2),
        (3, 3)
}

for element in set_of_tuple:
     if (element[0] + element[1]) % 2 == 0:
         print(element, end="   ")
else:
    print(end="\n")
