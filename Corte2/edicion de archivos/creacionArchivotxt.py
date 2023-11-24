#se le debe asignar un nombre al arcihvo que se desea crear
nombre_archivo = "hola.txt"

# posteriroemtente se debe escribir el contenido de este archivo
contenido = "Este es el contenido que se escribirá en el archivo de texto."

# Se abre como si se tratara de escribir  ("w" significa escribir)
with open(nombre_archivo, "w") as archivo:
    archivo.write(contenido)

print(f"Se ha creado el archivo '{nombre_archivo}' con el contenido deseado.")
