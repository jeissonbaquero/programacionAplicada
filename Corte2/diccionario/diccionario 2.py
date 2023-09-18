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
