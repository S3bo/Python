s1 = "FullStack"
s2 = "Python"

middleIndex = len(s1)//2
print("Oryginalne ciągi są to: " ,s1, s2)
middleThree = s1[:middleIndex] +s2 +s1[middleIndex:]
print("Po dołączeniu nowego ciągu w środku: ", middleThree)
