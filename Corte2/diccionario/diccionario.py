sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}# se le asigna a cada palabra clave un valor
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)
# la palabra clave puedendeser numero y los valores estrinhg
translations = {"mountain":	"orod", "bread":	"bass", "friend":	"mellon", "horse":	"roch" }
print(translations)
subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}
print(subtotal_to_total)
#tambien s epede tener listas como valores, pero no como palabra clave
#ademas cada listas como valor peud varia su tamaño
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"],"geografica":"lucas"}
print(students_in_classes)
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"],"geografica":"lucas",5:3,7:"hola"}
print(students_in_classes)
#Num={[1,2,3]:3,[3,4,5]:4}#esta liena de codigo ejemplifica el erro de tenr listas como palabras claves
Nuedic={}# se creo un diccionario basio
print(Nuedic)
# para agregar un elemento al diccioanrio se llama al diccionario y en llaves se pone la palabra clave y cluego con el igual se le asigna el valor
Nuedic["perro"]="perseo"
print(Nuedic)
Nuedic["gato"]="merlin"
print(Nuedic)
#para eliminar una palabra clave y sus valores  se usa  la funcionn del , se llama la lsia y en corchete la palabra clave que se va a eliminar 
del Nuedic["perro"]
print(Nuedic)
#cuando se queire agregar mas de un elemento ala vez se utiliza la funcion update
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print(oscar_winners)
oscar_winners.update({"Supporting Actress": "Viola Davis"})
print(oscar_winners)
oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)
oscar_winners["Animated Feature"] = "No te metas con zohan"
print(oscar_winners)
#para crear un diccionario con una lista para las palbras calves y un lsita para los valores
#NOTA: solo se crearia el diciconario con los valores y plabars claves que tengan pareja si hay uan lista mayor que la otra, se tendra el numeor de elementos de la lista mas corta
pal_Clave=["obj1","obj2","obj3"]
valores=[1,2,3]
ziped_nuevo=zip(pal_Clave,valores)
Nuevodic={key:value for key, value in ziped_nuevo}
print(Nuevodic)
# experimetos:
#para cambiar le valor d euna palabra clave se realia llamando del diccionario y de la palabra  al acual se le queira cambiar su valor
#students_in_classes["cartography"]="diego"
#print(students_in_classes)
#students_in_classes["Historia"]="juan"
#print(students_in_classes)
#x=input("digite el nombre clave")
#y=input("digite el valor")
#Nuedic[x]=y
#print(Nuedic)
