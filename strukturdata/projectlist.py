print ("my favorite food")
print (f"{10 * '='}")
favorite_food = []

while True:
    food = input ("makanan favorit kamu(ketik 'sudah' jika selesai menginput makanan favorit): ")
    if food.lower() == "sudah":
        break 
    favorite_food.append(food)

    print(f"makanan favorit ku adalah : {favorite_food}")