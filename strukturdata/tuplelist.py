number = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
buah = ("apel","banana","orange")
print (type(number))
print (len(number))

print (type(buah))
print (len(buah))

print (buah[2])

buah_list = list (buah)
buah_list.append ("watermelon")
print (buah_list)
buah = tuple(buah_list)
print (buah)