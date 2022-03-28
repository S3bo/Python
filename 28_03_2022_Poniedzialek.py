# def longest_word(filename):
#     with open(filename, "r", encoding="utf-8") as file:
#         text = file.read().split()
#         #print(text)
#         lword = text[0]
#         for i in text:
#             if len(lword)<len(i):
#                 lword = i
#         return lword
# print(longest_word("python.txt"))
#

#------------------------------------------------------------------------------------------------------

#zapisywanie listy do pliku

#napisz program, który zapisze listę do pliku.
#color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']


# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# myfile = open('abc.txt', "w")
# for c in color:
#     myfile.write(str(c) + "\n")
# myfile.close()
#
# content = open('abc.txt')
# print(content.read())

#Zadanie
# Napisz program, który otworzy plik sonety.txt i sprawdzi liczbę słów w całym tekście
# Dodatkowo, napisz funkcję, która zlicza słowa tylko w co 7 linijce tekstu

# def opcount(filename):
#     f = open(filename, "r")
#     wlist = f.read().split()
#     len(wlist)
#     print(wlist)
# opcount("sonety.txt")

# from math import sin
# print(sin(1))

import fruit
# from fruit import lemon

fruit.lemon(5)
# lemon(5)
