# pitagoras = lambda a, b:  ((a * a) + (b * b)) ** 0.5
# print(pitagoras(3, 4))

# temperatury = [
#     37.6, 35.8, 37.6, 33.4, 34.1, 37.1, 35.9, 34.1, 37.1, 40.5, 38.5, 37.6,
#     35.8, 34.5, 36.4, 38.3, 37.5, 37.7, 34.0, 35.3, 35.7, 38.9, 34.8, 34.1,
#     39.6, 35.4, 34.7, 37.6, 38.4, 36.4, 39.8, 39.1, 37.1, 35.6, 36.8, 37.6,
#     36.7, 40.0, 38.0, 34.1, 35.5, 38.5, 36.1, 32.6, 32.9, 34.5, 41.0, 38.3,
#     33.7, 38.7, 36.9, 36.2, 33.7, 38.3, 35.3, 38.3, 40.1, 39.3, 38.2, 37.6,
#     39.1, 37.1, 34.4, 38.7, 35.8, 38.2, 38.2, 33.1, 37.8, 36.5, 37.6, 37.4,
#     34.3, 37.7, 36.0, 37.5, 37.6, 36.5, 31.3, 37.7, 40.3, 39.5, 35.7, 38.1,
#     34.7, 36.5, 34.3, 38.0, 37.0, 38.5, 39.4, 37.6, 41.7, 40.0, 38.4, 38.9,
#     34.2, 40.2, 34.3, 35.3
# ]

# wynik = list(filter(lambda x: x >= 40.0, temperatury))
# print(wynik)
# wynik_sort = sorted(wynik)
# print(wynik_sort)

# from statistics import mean
# sr_temp = mean(temperatury)
# print(sr_temp)
#
# odch = list(map(lambda x: x - sr_temp, temperatury))
# print(odch)
#
# odch = list(map(lambda x: round(x - sr_temp, 1), temperatury))
# print(odch)

# from functools import reduce
# nums = [1, 2, 3, 4, 5]
# print(reduce(lambda a, b: a + b, nums))
#
# print(reduce(lambda a, b: a * b, [1, 2, 3, 4]))


#pierwsza lambda

# Ćwiczenie na rozgrzewkę
# Utwórz funkcję lambda, która przyjmuje jeden parametr (a) i zwraca go

# first_l = lambda s:s
# print(first_l(2))

# dodawanie = lambda s:s + 15
# print(dodawanie(5))



# multiply = lambda a,b : a * b
# print(multiply(5,6))

#Napisz program w Pythonie wsparcia sortowania listy krotek za pomocą lambda po drugim elemencie

# subject_marks = [('Język angielski', 88),
#                  ('Nauka',           90),
#                  ('Matematyka',      97),
#                  ('Nauki społeczne', 82)]
#
# wynik_sort = sorted(subject_marks, key = lambda x : x[1])
# print(wynik_sort)

#Napisz program w Pythonie, aby posortować za pomocą lambda listę słowników po kluczu model lub kolor.

# models = [{'marka': 'Nokia',   'model': '3310',   'kolor': 'Czarny'},
#           {'marka': 'Apple',   'model': '11',     'kolor': 'Złoty'},
#           {'marka': 'Samsung', 'model': 'Galaxy', 'kolor': 'Srebrny'}]
#
# sort_by_model = sorted(models, key = lambda x : x["model"])
# print(sort_by_model)

# Ćwiczenie
# Napisz program w Pythonie, aby sprawdzić, czy dany ciąg (str) zaczyna się od znaku ‘P’, używając lambda
# Podpowiedź: skorzystaj z funkcji (metody) startswith()

# sort_by_first_letter = lambda x: x.startswith("P")
# print(sort_by_first_letter("Papuga"))

# Napisz program w Pythonie, aby wyodrębnić rok, miesiąc, dzień i godzinę za pomocą lambda
# Podpowiedź: skorzystaj z modułu datetime:
# now = datetime.datetime.now() - przypisuje do nowaktualną lokalną datę i godzinę.
# now.year - wyodrębnia i zwraca rok z now.
# now.month - wyodrębnia i zwraca miesiąc z now.
# now.day - wyodrębnia i zwraca dzień z now.
# now.time() - wyodrębnia i zwraca godzinę z now.

# from datetime import datetime
# now = datetime.now()
# year = lambda x:x.year
# month =lambda x:x.month
# day = lambda x:x.day
# time = lambda x:x.time
# print(year(now))
# print(month(now))
# print(day(now))
# print(time(now))


# Ćwiczenie
# Napisz program w Pythonie, aby sprawdzić, czy dany ciąg jest liczbą, czy nie, używając lambda
# Podpowiedź: przydatna metoda to
# string.replace(oldvalue, newvalue, count)
# Składnia parametrów:
# oldvalue – Wymagany; ciąg do wyszukania
# newvalue – Wymagany; ciąg znaków, który ma zastąpić starą wartość
# count – Opcjonalny; liczba określająca, ile wystąpień starej wartości chcesz zastąpić; domyślnie są to wszystkie wystąpienia

# cw_8 = lambda x: x.replace(".", "", 1).isdigit()
# prework = lambda x: cw_8(x) if x[0] != "-" else cw_8(x[1:1])
# print(prework("678"))
# print(prework("7.56"))
# print(prework("-7.56"))
#
# is_num = lambda q: q.replace('.', '', 1).isdigit()
# print(is_num('26587'))
# print(is_num('4.2365'))
# print(is_num('-12547'))
# print(is_num('00'))
# print(is_num('A001'))
# print(is_num('001'))
# print("\nWydrukuj liczby kontrolne:")
# is_num1 = lambda r: is_num(r[1:]) if r[0] == '-' else is_num(r)
# print(is_num1('-16.4'))
# print(is_num1('-24587.11'))

# Napisz program w Pythonie do filtrowania listy liczb parzystych i nieparzystych całkowitych za pomocą lambda i filter
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ćwiczenie
# Napisz program w Pythonie do filtrowania listy liczb parzystych i nieparzystych całkowitych za pomocą lambda i filter
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 8:53
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Oryginalna lista liczb całkowitych:")
# print(nums)
# print("\nParzyste liczby ze wspomnianej listy:")
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)
# print("\nNieparzyste liczby ze wspomnianej listy:")
# odd_nums = list(filter(lambda x: x % 2 != 0, nums))
# print(odd_nums)

Ćwiczenie
Napisz program w Pythonie, aby znaleźć przecięcie dwóch podanych list za pomocą lambda i filter
array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]