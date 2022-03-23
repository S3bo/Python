#Biorąc pod uwagę 2 ciągi, s1 i s2 zwróć nowy ciąg złożony z pierwszego, środkowego i ostatniego znaku każdego ciągu wejściowego
#Dane:
#s1 = "America"
#s2 = "Japan"
#Oczekiwany wynik:
#AJrpan

s1 = "America"
s2 = "Japan"

first_char = s1[0] + s2[0]
middle_char= s1[int(len(s1)/2)] + s2[int(len(s2)/2)]
last_char = s1[-1] + s2[-1]
#jedno rozwiazanie
# print(first_char + middle_char + last_char)
#drugie rozwiazanie z przypisaniem nazwy dla wyniku
res = first_char + middle_char + last_char
print("Mix String to: ", res)