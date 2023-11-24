#{"name": "victor"}.get("name")
#returns  "victor"

dict1={'color':'blue','shape':'circle'}
dict2={'color':'red','number':42}
print("before", dict1)
dict1.update(dict2)# con la funcion update podemos actualizar  los (como se peude ver en la palabra clave color) dato e incluso combinar diccionarios, cabe acarar qeu los datos se guardara ene diccionario a la cual se l esta realizazndo la funcion
print (dict1)
print("after",dict1)

print(dict1.keys())#con esat funcioon llamamos la palbras calve del  dcicionario
print(dict1.items())# aqui separamos  las palbara con sus valores

# sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
# num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

# print(sensors)
# print(num_cameras)
# translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }
# print(translations)

##ejemplo error debido a que una lista no puede ser una palabra clave:
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
# # print(powers)

##locorrecot esque las palabras claves nunca sena listas, el contenido si puede ser
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
print(children)

my_empty_dictionary = {}
print(my_empty_dictionary)

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
menu["cheesecake"] = 8
print("After", menu)
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"horses": 2}
print(animals_in_zoo)


##Para agregar varias palabras clave
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
print("Before", sensors)

##Si quisieramos agregar 3 nuevas habitaciones, podriamos usar:
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print("After", sensors)

###
# user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
# print(user_ids)
# user_ids.update({"theLooper": 138475, "stringQueen": 85739})
# print(user_ids)

## Sobrescribir valores ##Sabemos que podemos agregar una clave usando la siguiente sintaxis:
menu["banana"] = 3
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
menu["oatmeal"] = 5
print("After", menu)

## El valor de la palabra clave oatmeal se cambiado a 5.

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print("Before", oscar_winners)
print()
oscar_winners.update({"Supporting Actress": "Viola Davis"})
print("After1", oscar_winners)
print()
oscar_winners["Best Picture"] = "Moonlight"
print("After2", oscar_winners)


##Para combinanr dos siccionarios se segiuita el sigueinte ejmplo


names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

#se crear un diccionario usando un dictado de comprension, con esta sintaxis:

zipStudents = zip(names, heights)
print("zipStudents: ", zipStudents)


## zip() combina dos listas en un iterador de tuplas con los elementos de la lista emparejados. Este dictado de comprensión:

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks)

drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)
plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})
print("After: ", plays)
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)
