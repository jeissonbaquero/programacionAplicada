#con este codigo obtenidremos un numeor aleatorio que se escribira en una rchivo
import random
import csv
#se llama al archivo donde se quere guardar los numeros
archivo= 'NumeorAle.csv'

while True:
    # se generar un número pseudoaleatorio entre 0 y 1
    numero = random.uniform(0, 1)

    # posterieoemte se guarda el numeor escrbineod este sobre el archivo anteiremte escrito
    with open(archivo, 'a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([numero])

    print(f'Se ha escrito el número {numero} en el archivo {nombre_archivo_csv}.')
