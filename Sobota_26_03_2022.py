#Fibbonaci

# def fibbonaci_numbers(n):
#
#     wynik = []
#     a, b = 0, 1
#     while len(wynik) < n:
#         wynik.append(a)
#         a, b = b, a+b
#     return wynik
#
# x = fibbonaci_numbers(10)
#
# print(x)

#
# def chain_lenght(n):
#     count = 0
#     for i in n:
#         count += 1
#     return count
# print(chain_lenght())

# def sum_elements(n):
#     count = 0
#     for i in n:
#         count += i
#     return (count)
#
#
# print(sum_elements([1,2,-8]))

# def multiplication_result(n):
#     count = 1
#     for i in n:
#         count *= i
#     return (count)
#
# print(multiplication_result([2,2,2,2]))


# ZADANIE
#
# wyświetl największą liczbę ze zbioru
#(dodatkowo wprowadzanie liczb przez użytkownika)
# a = int(input("Wprowadź numer: "))
# b = int(input("Wprowadź drugi numer: "))
# c = int(input("Wprowadź trzeci numer: "))
#
# n = (a,b,c)
#
# def highest_number(n):
#     highest = n[0]
#     for x in n:
#         if x > highest:
#             highest = x
#     return highest
# print(highest_number(n))


#ZADANIE

# Napisz funkcję w Pythonie, który zlicza liczbę znaków (częstotliwość znaków) w ciągu tekstowym.
# Przykładowy ciąg tekstowy: google.com
# Oczekiwany wynik: {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
# Podpowiedź : istnieje metoda dict.keys( ), którą możemy wykorzystać aby sprawdzić czy dany klucz znakduje się w słowniku
#
#
# def count_sign(string):
#     dict = {}
#     for i in string:
#         if i in dict.keys():
#             dict[i] += 1
#         else:
#             dict[i] = 1
#
#     return(dict)
# print(count_sign("google.com"))


# ZADANIE


# Napisz funkcję w Pythonie, który zlicza ciągi znaków, w których długość ciągu wynosi 2 lub więcej,
# a pierwszy i ostatni znak są takie same z podanej listy ciągów.
# Przykładowa lista : ['abc', 'xyz', 'aba', '1221']
# Oczekiwany wynik: 2

# def strings_of_characters(a):
#     count = 0
#     for i in a:
#         if len(i) >2 and i[0] == i[-1]:
#             count += 1
#     return count
# print(strings_of_characters(['abc', 'xyz', 'aba', '1221']))


# def last(n):
#     return n[-1]
#
# def sort_list_last(tuples):
#     return sorted(tuples, key=last)
#
# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

#___________________________________________________________
# ćwiczenie
# def string(item):
#     if len(item) < 2:
#         return ""
#     else:
#         return item[0:2] + item[-2:]
#
# print(string(item))

#
# Napisz program, policzy silnię dla liczby n tj.
# n! = 1*2*3*4...*(n-2)*(n-1)*n
# Zrób to przez napisanie funkcji, która rekurencyjne będzie się odwoływała do samej siebie do momentu gdy będzie liczyła silnie dla 1, która wynosi 1.


#  def silnia(n):
#      if n == 0:
#          return = 1
#      else:
#          return n * silnia(n-1)
#
#  print(silnia(5))
#
# do poprawienia




# ciąg Fibbonaciego

# def fibbonaci_numbers(n):
#
#     wynik = []
#     a, b = 0, 1
#     while len(wynik) < n:
#         wynik.append(a)
#         a, b = b, a+b
#     return wynik
#
# x = fibbonaci_numbers(10)
#
# print(x)

#                                    rekurencyjny ciąg Fibbonaciego:
#
# def rek_fibbonaci_numbers(n):
#     if n <= 1:
#         return n
#     else:
#         return rek_fibbonaci_numbers(n-1) + rek_fibbonaci_numbers(n-2)
#
# print(rek_fibbonaci_numbers(40))

import plik.txt
print(plik.txt)
















