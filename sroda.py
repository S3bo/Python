#
#
# #  range(start,stop,[step])
# '''
# for val in "string":
#     if val == "i":
#         break
#     print(val)
#
# print("koniec!")
#
#
#
# liczby = list()  # []
# i = 2
# while i < 11:
#     liczby.append(i)
#     i += 2
# print(liczby)  # [2, 4, 6, 8, 10]
#
#
# for i in range(1, 4):
#     print(i)
# else:  # Wykonane, ponieważ nie ma break w for
#     print("Bez break")
#
# for n in range(2, 100):
#     for x in range(2, n):
#         if n % x == 0:
#             break
#     else: # normalny koniec pętli
#         print(n, 'jest liczbą pierwszą')
#
#
#
# #Dzielenie
#
# a= int(input("Podaj pierwszą liczbę: "))
# b= int(input("Podaj drugą liczbę: "))
# wynik_dzielenia = a/b
# print("Wynik dzielenia to: " , wynik_dzielenia)
#
#
# #Modulo
# wynik_modulo= a%b
# print("Wynik modulo to: " , wynik_modulo)
#
#
#
# #dzielenie_calkowite
# wynik_dzielenia_calkowitego = a//b
# print("Wynik dzielenia calkowitego to: " ,wynik_dzielenia_calkowitego)
#
#
# #and
#
#
#
# x= int(input("Podaj liczbę x: "))
# print("Warunek do sprawdzenia x > 3 i x < 10")
# print("Twoja liczba to: ", x)
# print(x>3 and x<10)
#
#
#
# #or
# #Zwróć wartość True, jeśli jedno ze stwierdzeń jest prawdziwe
# #x > 4 lub x < 3
# #Spróbuj!
#
# x= int(input("Podaj liczbę x: "))
# print("Warunek do sprawdzenia x > 4 lub x < 3")
# print("Twoja liczba to: ", x)
# print(x > 4 or x < 3)
#
#
#
# #not
# x= int(input("Podaj liczbę x: "))
# print("Warunek do sprawdzenia x > 3 not x < 10")
# print("Twoja liczba to: ", x)
# result= not(x > 3 and x < 10)
# print(result)
#
#
# Przypisz 8 do zmiennej x i 15 do zmiennej y
# Utwórz 2 instrukcje warunkowe
# Niech pierwsza wypisze: „Co najmniej jeden z warunków jest spełniony”,
# jeśli x jest większe niż 3 lub y jest parzyste
# Niech drugi wypisze „Żaden warunek nie jest spełniony”,
# jeśli x jest mniejsze lub równe 3, a y jest nieparzyste
# Zmień wartości przypisane do x i y i ponownie uruchom komórkę,
# aby sprawdzić, czy kod nadal działa
#
#
# #szybkie odwrocenie(x,y-y,x)
# #x=8
# #y=15
# x= int(input("Podaj liczbę x: "))
# y= int(input("Podaj liczbę y: "))
# if x>=3 or y%2 == 0:
#     print("Co najmniej jeden z warunków jest spełniony")
# if x>=3 and y%2 != 0:
#     print("Żaden warunek nie jest spełniony")
#
#
#
#
# list = ["marta", "mikolaj","adam", "alicja", "andrzej", "dominik","hania",
#         "katarzyna","krzysztof","lukasz","malgorzata","rafal","sebastian",
#         "anka","dominik","martyna","tymoteusz"]
#
# list.sort()
# b=0
# print("Osób w całej grupie jest: ",len(list))
# for osoba in list:
#     if osoba[-1] == "a":
#         b+=1
# print("Kobiet w grupie jest: ",b )
#
#
# #a przykład następująca pętla zostanie wykonana bez żadnego
# #przerwania:
#
# for i in range(5):
#     print(i)
# else:
#     print("Gotowe!")
#
#
# #Ćwiczenie
# #Poniżej znajdują się dwie listy.
# #Napisz program w Pythonie konwertujący je na słownik
# #w taki sposób, że pozycja z listy 1 jest kluczem,
# #a pozycja z listy 2 jest wartością
# #Oczekiwany wynik:
# #{'Dziesieć': 10, 'Dwadzieścia': 20, 'Trzydzieści': 30}
#
# keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
# values = [10, 20, 30]
#
# slownik = dict()
# for i in range(len(keys)):
#     slownik.update({keys[i]:values[i]})
# print(slownik)
#
#
#
# #Ćwiczenie
# #Zobaczmy ćwiczenie, które pomoże lepiej zrozumieć instrukcję pass
# #Umieść instrukcję pass, aby blok if nie zgłaszał błędu
#
# name = input("Proszę wpisać swoje imię.")
# # Wpisz swoją odpowiedź tutaj.
#
# if len(name) > 0:
#     print(name)
# else:
#     pass
#
#
#
# Znajdź liczby, które są podzielne przez 7 i są wielokrotnością 5 w zakresie
# Napisz program w Pythonie, aby znaleźć liczby podzielne przez 7
# i będące wielokrotnością 5 między 1500 a 2700 (obie uwzględnione)
#
#
#
# for numbers in range(1500,2701):
#     if (numbers%7 == 0 and numbers%5 == 0):
#         print(numbers)
#
# '''
#
#  nl = []
#  for x in range(1500, 2701):
#      if x % 7 == 0 and x % 5 == 0:
#         nl.append(str(x))
#   print(nl)
#   print(';'.join(nl))
#
#

#
# Ćwiczenie: Oblicz sumę wszystkich liczb od 1 do podanej liczby
# Napisz program akceptujący liczbę od użytkownika i obliczający
# sumę wszystkich liczb od 1 do podanej liczby
# Na przykład, jeśli użytkownik wpisał 10,
# wynik powinien wynosić 55 (1+2+3+4+5+6+7+8+9+10)
# Oczekiwany wynik:
#
# Wpisz numer 10
#
# Suma to: 55

