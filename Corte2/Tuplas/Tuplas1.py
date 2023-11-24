

###############TUPLAS###############
####################################
# Corresponde a una estructura similar a las listas, la diferencia esta
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("################################")
print("################################")
print("################################")
print("#############TUPLAS#############")
my_tupla = tuple(my_lista)
print()
print()
print("my_tuple: ", my_tupla)

print(my_tupla[0])
print(my_tupla[2])


#Evaluar si un elemento esta contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla)
print(my_tupla.count('Rojo'))

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)

#Empaquetado de tupla, tupla sin parentesis
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, ano = my_tupla
print(nombre)
print(dia)
print(mes)
print(ano)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Ano: ", ano)

#Convertir una tupla en una lista
my_lista2=list(my_tupla)
print(my_lista2)
