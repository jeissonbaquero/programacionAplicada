my_list=['rojo','azul','negro','morado','blanco']

print(my_list)
print(type(my_list))
print(my_list[0])
print(my_list[0:3])
#len imprime la longitu de la lista
print("my_list sixe", len(my_list))
#los arreglos no se peden cambiar de tamaño encmabo las listas si
my_list.append('Naranja')
print(my_list)
my_list.insert(3,'amarillo')
print(my_list)
my_list.extend(['marron','amarillo'])
print(my_list)
my_list.remove('rojo')
print(my_list)
my_list.insert(0,'rojo')
print(my_list)

print(my_list.pop())
my_list_3=my_list*3
print("my_list_3", my_list_3)
print("sort")
print()
my_listsort=my_list.sort()
print(my_listsort)

my_numlist=[10,9,8,7,6,5,4,3,2,1]
print("ordering my_numlist")
my_numlist.sort()
print(my_list)
