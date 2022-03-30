# num1 = float(input("Podaj pierwsza liczbe: "))
# num2 = float(input("Podaj druga liczbe: "))
#
# print(num1 + num2)

#rozmnażanie sie królików

# def chain_lenght(x):
#     count = 0
#     for i in x:
#         count += 1
#     return count
# print(chain_lenght("python"))


#Napisz funkcję w Pythonie, która zsumuje wszystkie elementy na liście.

# def sum_elements(n):
#     sum = 0
#     for i in n:
#         sum += i
#     return(sum)
#
# print(sum_elements([1,23,64,5432]))

# def mult_numbers(n):
#     multiply_result = 1
#     for i in n:
#         multiply_result *= i
#     return multiply_result
#
# print(mult_numbers([2,5,6,8]))


#napisz program w pythonie, który zwróci najwiekszy element
#
# def highest_number(n):
#     max_mumber = n[0]
#     for i in n:
#         if i > max_mumber:
#             max_mumber = i
#     return max_mumber
#
#
# print(highest_number([2,5,6,8]))

#Napiszx funkcję w Pythonie, króra zliczy liczbę znaków(częstotliwość znaków) w ciągiu znaków

# def count_sign(string):
#     dict = {}
#     for i in string:
#         if i in dict.keys():
#             dict[i] += 1
#         else:
#             dict[i] = 1
#     return(dict)
# print(count_sign("google.com"))
#
# arg = "sprawdzenie.txt"
# try:
#     f = open(arg, "r")
# except IOError as err:
#     print("Błąd: ",err)
# else:
#     print("Twój plik", arg, "ma liczbę wierszy", len(f.readline()))
#     f.close()

#
# arg = "nowy_plik.txt"
# try:
#     f = open(arg, "w")
#     f.write("Lorem ipsum")
# except IOError:
#     print("Nie można zapisać do pliku: '{}'".format(arg))
# else:
#     f.close()

# korzystanie z modułów
# from time import sleep
# print("dobranoc")
# sleep(2)
# print("dzien dobry")
#

#import fruit
from fruit import lemon
#print(fruit.lemon(5))
lemon(5)
