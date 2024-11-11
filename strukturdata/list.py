number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
buah = ["apel", "pisang", "melon"]
car = ["honda", "toyota", "tesla"]
name = ["haris", "habib", "reza", "faris"]

print (type(number))
print (len(number))

print (type(buah))
print (len(buah))

print (type(name))
print (len(name))

print (number[5])
print (buah[2])
print (f"{name[3]} and {name[0]}")

car.append ("mercedez")
print (car) 
name[0] = "queen"
print (name) 

buah.remove("apel")
print (buah)
buah.clear()
print (buah)