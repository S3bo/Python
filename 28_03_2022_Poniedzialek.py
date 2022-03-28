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
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
myfile = open('abc.txt', "w")
for c in color:
    myfile.write(str(c) + "\n")
myfile.close()

content = open('colors.txt')
print(content.read())
