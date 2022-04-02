# x =4
# print(type(x))
#
# x = "hello"
# print(type(x))
#
#
# x = 3.14159
# print(type(x))
#
# a=4
# print(id(a))
#
# b = "hello"
# print(id(b))
#
# c = 3.14159
# print(id(c))
#
# print(id(a))
# print(id(b))

# """Dokumentacja modułu"""
#
# class MyClass:
#     """Dokumentacja klasy"""
#
#     def my_method(self):
#         """Dokumentacja metody"""
#
# def my_function():
#     """Dokumentacja funkcji"""
#
# help(MyClass)
#
#
# Ćwiczenie: Klasa o nazwie MyClass z atrybutem o nazwie x
# No to jeszcze raz! Utwórz klasę o nazwie MyClassz atrybutem o nazwie x = 5.
# Teraz użyj klasy o nazwie MyClass do stworzenia obiektu.
# Utwórz obiekt o nazwie p1 i wydrukuj wartość x.

#
# class MyClass:
#     x=5
# p1=MyClass()
#
# print(p1.x)


# class KontoBankowe:
#     def __init__(self, nazwa, stan = 0):
#         self.nazwa = nazwa
#         self.stan = stan
#
#     def info(self):
#         print("nazwa:", self.nazwa)
#         print("stan:", self.stan)
#
#     def wyplac(self, ilosc):
#         self.stan -= ilosc
#
#     def wplac(self, ilosc):
#         self.stan += ilosc
#
#
# jk = KontoBankowe("Jan Kowalski", 1000)
#
# jk.info()
#
# jk.wplac(2000)
#
# jk.info()
#
# class Vehicle:
#     pass

# class Jets:
#
#
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#
#
#
# first_item = Jets("F16", "USA")
#
# print(first_item.name)
#
# class Jets:
#     model = None
#     country = 0
#
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
#
#
#
# first_item = Jets("F16", "USA")
#
# a=first_item.name
# b=first_item.origin
#
#
# print(a,b)

# Klasa Vehicle z atrybutami instancji max_speed i mileage
# Stwórz obiekt i w trakcie inicjacji przypisz jego atrybutom (odpowiednio) wartości 240 i
# Wydrukuj te atrybuty.


# class Vehicle:
#     def __init__(self, max_speed, milage):
#         self.max_speed = max_speed
#         self.milage = milage
# BMW = Vehicle(169, 2_000_202)
#
# print(BMW.max_speed, BMW.milage)

#
# class Car:
#     def __init__(self, color, milage):
#         self.color = color
#         self.milage = milage
# first_car = Car("Niebieski", 20_000)
# second_car = Car("Czerwony", 30_000)
#
# print(first_car.color + " samochód ma " + str(first_car.milage) + " kilometrów przebiegu.")
# print(second_car.color + " samochód ma " + str(second_car.milage) + " kilometrów przebiegu.")

# Ćwiczenie
# Stwórz nowe instancje od pierwszej do szóstej pozycji w tej kolejności:
# F14, SU 33, AJS37, Mirage 2000, Mig 29, A10. Możesz sprawdzić Podpowiedź 1, aby sprawdzić origin.
# SU33: Rosja
# AJS37: Szwecja
# Mirage2000: Francja
# F14: USA
# Mig29: ZSRR
# A10: USA
#

class Jets:
    def __init__(self, name, country):
        self.name = name
        self.origin = country



first_item= Jets("SU33", "Rosja")
second_item=Jets("AJS37", "Szwecja")
third_item=Jets("Mirage2000", "Francja")
fourth_item=Jets("F14", "USA")
fifth_item=Jets ("Mig29", "ZSRR")
sixth_item=Jets("A10", "USA")


first_army=[first_item.name,second_item.name,third_item.name,fourth_item.name,fifth_item.name,sixth_item.name]


print(first_army)